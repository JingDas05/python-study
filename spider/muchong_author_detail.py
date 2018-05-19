#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-04-03 20:28:16
# Project: root_spider

from pyspider.libs.base_handler import *
import hashlib
from pyspider import database


class Handler(BaseHandler):
    crawl_config = {
    }

    author_projectdb = database.connect_database('elasticsearch+projectdb://127.0.0.1:9200/?index=author')
    flower_projectdb = database.connect_database('elasticsearch+projectdb://127.0.0.1:9200/?index=flower')

    @every(minutes=1)
    def on_start(self):
        self.crawl('http://muchong.com/bbs/space.php?uid=3583297', callback=self.handle_author, cookies={
            "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
            "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
            "_discuz_pw": "9a1449a8990d49a6",
            "_discuz_uid": "3302227",
            "_emuch_index": "1",
            "_ga": "GA1.2.1902872401.1522564172",
            "_gat": "1"
        })

    @config(age=1)
    def handle_author(self, response):
        hl_md5 = hashlib.md5()
        # 作者信息字典
        author = {}
        # 获取整个doc
        context = response.doc
        # 查找基本信息，class 是userinfo base的table
        basic_information = context("table.userinfo.base")
        # 注册时间
        register_time = basic_information("td:eq(0)").text()
        if register_time:
            author["register_time"] = register_time
        # 其他基本信息(有三个class 为userinfo的table, 选取第二个)
        basic_information = context("table.userinfo:eq(1)")
        author["id"] = basic_information("tr:eq(0) td:eq(0)").text()
        author["name"] = context("div.space_index").find("a:eq(0)").text()
        author["sex"] = basic_information("tr:eq(4) td:eq(0)").text()
        birthday_time = basic_information("tr:eq(4) td:eq(2)").text()
        if (not birthday_time == "0000-00-00") and (not birthday_time == ""):
            author["birthday_time"] = birthday_time
        author["coin_num"] = basic_information("tr:eq(1) td:eq(1)").text()
        author["major"] = basic_information("tr:eq(3) td:eq(2)").text()
        author["help_num"] = basic_information("tr:eq(0) td:eq(2)").text()
        author["grant_num"] = basic_information("tr:eq(1) td:eq(2)").text()
        note_num_src = basic_information("tr:eq(2) td:eq(1)").text()
        note_num_desc = basic_information("tr:eq(2) td:eq(1) font").text()
        author["note_num"] = note_num_src.replace(note_num_desc, "").replace("\n","").replace(" ", "")
        hl_md5.update(author["id"].encode(encoding='utf-8'))
        es_author_id = hl_md5.hexdigest()
        composite_info = context("div.space_index table tr").find("div:last").text()
        # 截取,切片字符串
        composite_info = composite_info[composite_info.find("听众"):].split("\xa0")
        # 分组存储
        #if len(composite_info) > 0 and not composite_info[0] == "":
        #    author["fans_num"] = composite_info[0][composite_info[0].find(":")+1:].replace(" ", "")
        #    print(author["fans_num"])
        #if len(composite_info) > 1 and not composite_info[1] == "":
        #    author["flower_num"] = composite_info[1][composite_info[1].find(":")+1:].replace(" ","")
        #    print(author["flower_num"])
        # 查看获取的红花
        flowers = context("table.userinfo:eq(2)").find("table")("tr td")
        # flower_num = 0
        for flower_row in flowers.items():
            hl_md5_flower = hashlib.md5()
            flower = {}
            flower["owner_id"] = author["id"]
            flower["owner_name"] = author["name"]
            flower["sender_name"] = flower_row("a").text()
            flower_num = flower_row("font").text()[1:-1]
            flower["flower_num"] = "1" if flower_num=="" else flower_num
            raw_index_id = flower["owner_id"]+flower["sender_name"]
            hl_md5_flower.update(raw_index_id.encode(encoding='utf-8'))
            flower_es_id = hl_md5_flower.hexdigest()
            #flower_num = flower_num+ int(flower["flower_num"])
            print(flower_es_id)
            print(flower)
            self.flower_projectdb.es.index("flower", "project", flower, flower_es_id)
        #author["flower_num"] = flower_num
        self.author_projectdb.es.index("author", "project", author, es_author_id)