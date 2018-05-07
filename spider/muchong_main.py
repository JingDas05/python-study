#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-05-07 07:58:37
# Project: main

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=1)
    def on_start(self):
        self.crawl('http://muchong.com/bbs', callback=self.index_page, cookies={
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
        context = response.doc
        for first_area in context.find("div.forum_Box.bg_global.xmc_line_lr.xmc_line_bno").items():
            self.handle_first_area(first_area("h2 strong").text(), first_area("table"))

    # 处理一级板块
    def handle_first_area(self, first_area_name, second_area_table):
        second_area = second_area_table.find("td")
        for each_second_area in second_area.items():
            second_area_link = each_second_area.find("div.xmc_fl.xmc_forum_width h4.xmc_blue a")
            second_area_name = second_area_link.text()
            second_area_href = second_area_link.attr("href")
            self.handle_second_area(first_area_name, second_area_name, second_area_href)

    # 处理二级板块
    def handle_second_area(self, first_area_name, second_area_name, second_area_href):
        if first_area_name != "" and second_area_name != "" and second_area_href != "":
            self.crawl(second_area_href, callback=self.second_index_page(first_area_name), cookies={
                "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
                "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
                "_discuz_pw": "9a1449a8990d49a6",
                "_discuz_uid": "3302227",
                "_emuch_index": "1",
                "_ga": "GA1.2.1902872401.1522564172",
                "_gat": "1"
            })

    def second_index_page(self, response, first_area_name):
        # print(response.doc)
        print(first_area_name)

