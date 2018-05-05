#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-04-03 20:28:16
# Project: root_spider

from pyspider.libs.base_handler import *
import hashlib


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=1)
    def on_start(self):
        self.crawl('http://muchong.com/t-12233935-1', callback=self.index_page, cookies={
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
        hl_md5 = hashlib.md5()
        # 作者信息字典
        note = {}
        # 获取整个doc
        context = response.doc
        for each_note in context("tbody[id^='pid']"):
            print(1)
        first_note = context("tbody[id='pid3']")
        author = first_note.find("div[class='pls_user'] h3 a")
        author_link = author.attr("href")
        # 楼层及创建时间块
        floor_time_area = first_note.find("div[class='pls_info']")
        create_time = floor_time_area("em").text()
        # 一楼是1楼，二楼是沙发，三楼是板凳，四楼是4楼
        floor = floor_time_area("span a").text()
        raw_id = author.text() + create_time + floor
        hl_md5.update(raw_id.encode(encoding='utf-8'))
        note["id"] = hl_md5.hexdigest()
        # 帖子内容区域
        content_area = context.find("td[class='plc_mind'] div[class='plc_Con']")
        # 帖子内容?????
        note["content"] = content_area("div[class='t_fsz'] td").text()
        # 发布设备
        note["device"] = content_area.find("font[class='gray_ext'] a")
        # 楼主主题
        note["title"] = content_area.find("h1").text()
        # 回复的目标帖子id,包含了发帖人虫名， 发帖时间，以及楼层
        note["reply_target_content_id"] = content_area.find("fieldset div").text()
        print(note)