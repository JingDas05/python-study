#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-04-03 20:28:16
# Project: root_spider

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=1)
    def on_start(self):
        self.crawl('http://muchong.com/bbs/space.php?uid=5111829', callback=self.index_page, cookies={
            "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
            "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
            "_discuz_pw": "9a1449a8990d49a6",
            "_discuz_uid": "3302227",
            "_emuch_index": "1",
            "_ga": "GA1.2.1902872401.1522564172",
            "_gat": "1"
        })

    @config(age=1)
    def index_page(self, response):
        # 作者信息字典
        author = {}
        # 获取整个doc
        context = response.doc
        # 查找基本信息，class 是userinfo base的table
        basic_information = context("table.userinfo.base")
        # 注册时间
        author["registerTime"] = basic_information("td:eq(0)").text()
        # 其他基本信息(有三个class 为userinfo的table, 选取第二个)
        basic_information = context("table.userinfo:eq(1)")
        author["insectNum"] = basic_information("tr:eq(0) td:eq(0)").text()
        author["name"] = context("div.space_index").find("a:eq(0)").text()
        author["sex"] = basic_information("tr:eq(4) td:eq(0)").text()
        author["birthdayTime"] = basic_information("tr:eq(4) td:eq(2)").text()
        author["coinNum"] = basic_information("tr:eq(1) td:eq(1)").text()
        author["major"] = basic_information("tr:eq(3) td:eq(2)").text()
        author["helpNum"] = basic_information("tr:eq(0) td:eq(2)").text()
        author["grantNum"] = basic_information("tr:eq(1) td:eq(2)").text()
        composite_info = context("div.space_index").find("div:last").text()
        # 截取,切片字符串
        composite_info = composite_info[composite_info.find("听众"):].split("\xa0")
        # 分组存储
        author["fansNum"] = composite_info[0][composite_info[0].find(":"):]
        author["flowerNum"] = composite_info[1][composite_info[1].find(":"):]
        author["noteNum"] = composite_info[3][composite_info[3].find(":"):]
        # 查看获取的红花
        flowers = context("table.userinfo:eq(2)").find("table")("tr td")
        for flower_row in flowers.items():
            # 送红花的人
            print(flower_row("a").text())
            # 朵数
            print(flower_row("font").text()[1:-1])
        print(author)
