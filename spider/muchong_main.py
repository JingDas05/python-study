#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-05-07 07:58:37
# Project: main

from pyspider.libs.base_handler import *
import hashlib
import re
from pyspider import database


class Handler(BaseHandler):
    crawl_config = {

    }

    author_projectdb = database.connect_database('elasticsearch+projectdb://127.0.0.1:9200/?index=author')
    note_projectdb = database.connect_database('elasticsearch+projectdb://127.0.0.1:9200/?index=note')
    flower_projectdb = database.connect_database('elasticsearch+projectdb://127.0.0.1:9200/?index=flower')

    # 处理帖子内容的方法，获取 回帖target_id, 帖子内容，发帖客户端
    def handle_content(self, content_area, building_id):
        hl_md5 = hashlib.md5()
        # 原生帖子内容, eg: 引用回帖:4楼:Originallypostedby含笑木香at2018-04-0321:08:49比如我，最喜欢暴风雨的时候睡懒觉，
        # 我也很喜欢啊，别人怕暴风雨，我是遇到暴风雨就兴奋发自小木虫IOS客户端
        raw_content = content_area("div[class='t_fsz']").find("td:eq(0)").text().replace("\n", "").replace(" ", "")
        if (raw_content == ""):
            target_id = ""
            content = ""
            device = ""
            return target_id, content, device
        else:
            # 处理有引用回帖的情况
            if raw_content.startswith("引用回帖"):
                # 获取引用回帖的中的日期
                maybe_date = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\d{1,2}:\d{1,2}:\d{1,2})", raw_content)
                if not maybe_date:
                    target_id = ""
                    content = ""
                    device = ""
                    return target_id, content, device
                founded_date = maybe_date.group(0)
                # 对于引用回帖的内容进行截取，key1=引用回帖: key2=at
                reference_str = raw_content[raw_content.find("引用回帖:") + 5:raw_content.find(founded_date) - 2]
                # 获取虫名 以及 楼层，还有上面的日期，拼接raw_id
                raw_id = reference_str[reference_str.find("Originallypostedby") + 18:] + founded_date + reference_str[
                                                                                                        :1]
                hl_md5.update(raw_id.replace(" ", "").encode(encoding='utf-8'))
                target_id = hl_md5.hexdigest()
                # 获取帖子内容
                content = raw_content[raw_content.find(founded_date) + 18:raw_content.find("发自小木虫")]
                # 获取客户端
                if raw_content.find("发自小木虫") != -1:
                    device = raw_content[raw_content.find("发自小木虫") + 5:raw_content.find("客户端")]
                else:
                    device = "PC"
                return target_id, content, device
            else:
                target_id = building_id
                content = raw_content[:raw_content.find("发自小木虫")]
                if raw_content.find("发自小木虫") != -1:
                    device = raw_content[raw_content.find("发自小木虫") + 5:raw_content.find("客户端")]
                else:
                    device = "PC"
                return target_id, content, device

    # 入口方法
    @every(minutes=2.5 * 24 * 60)
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

    # 单位是秒
    @config(age=36 * 60 * 60)
    def index_page(self, response):
        context = response.doc
        for each_area in context.find("div.forum_Box.bg_global.xmc_line_lr.xmc_line_bno").items():
            self.handle_first_area(each_area("h2 strong").text(), each_area("table"))

    # 处理一级板块，比如 网络生活区等
    def handle_first_area(self, first_area_name, second_area_table):
        second_area = second_area_table.find("td")
        for each_second_area in second_area.items():
            second_area_link = each_second_area.find("div.xmc_fl.xmc_forum_width h4.xmc_blue a")
            second_area_name = second_area_link.text()
            second_area_href = second_area_link.attr("href")
            self.handle_second_area(first_area_name, second_area_name, second_area_href)

    # 处理二级板块,比如 休闲灌水等，这个时候进入的是分页的首页 url: http://muchong.com/f-6-1
    def handle_second_area(self, first_area_name, second_area_name, second_area_href):
        if first_area_name != "" and second_area_name != "" and second_area_href != "":
            self.crawl(second_area_href, callback=self.second_index_page, cookies={
                "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
                "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
                "_discuz_pw": "9a1449a8990d49a6",
                "_discuz_uid": "3302227",
                "_emuch_index": "1",
                "_ga": "GA1.2.1902872401.1522564172",
                "_gat": "1"
            })

    # 统计二级分类下的全部帖子，分页爬取(首先获取总页数，拼接每一页应该爬取的url)
    def second_index_page(self, response):
        context = response.doc
        total_page = context.find("td.header:eq(1)").text()
        total_page = total_page[total_page.find("/") + 1:]
        basic_url = response.url
        if not total_page == "":
            total_page = int(total_page)
            if total_page > 200:
                total_page = 200
            # 循环遍历每页
            for page in range(total_page):
                each_page_url = basic_url[:basic_url.rfind("-") + 1] + str(page + 1)
                self.crawl(each_page_url, callback=self.handle_each_second_index_page, cookies={
                    "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
                    "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
                    "_discuz_pw": "9a1449a8990d49a6",
                    "_discuz_uid": "3302227",
                    "_emuch_index": "1",
                    "_ga": "GA1.2.1902872401.1522564172",
                    "_gat": "1"
                })

    # 爬取二级分类下的每一个帖子
    def handle_each_second_index_page(self, response):
        context = response.doc
        notes_titles = context.find("th.thread-name")
        for each_note in notes_titles.items():
            if each_note is not None:
                self.crawl(each_note("a.a_subject").attr("href"), callback=self.note_index, cookies={
                    "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
                    "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
                    "_discuz_pw": "9a1449a8990d49a6",
                    "_discuz_uid": "3302227",
                    "_emuch_index": "1",
                    "_ga": "GA1.2.1902872401.1522564172",
                    "_gat": "1"
                })

    # 统计帖子的总页数，分页爬取
    def note_index(self, response):
        context = response.doc
        total_page = context.find("td.header:eq(1)").text()
        total_page = total_page[total_page.find("/") + 1:]
        basic_url = response.url
        basic_url = basic_url[:basic_url.rfind("-") + 1]
        if not total_page == "":
            total_page = int(total_page)
            if total_page > 200:
                total_page = 200
            # 循环遍历每页
            for page in range(total_page):
                each_page_url = basic_url[:basic_url.rfind("-") + 1] + str(page + 1)
                self.crawl(each_page_url, callback=self.handle_note, cookies={
                    "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
                    "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
                    "_discuz_pw": "9a1449a8990d49a6",
                    "_discuz_uid": "3302227",
                    "_emuch_index": "1",
                    "_ga": "GA1.2.1902872401.1522564172",
                    "_gat": "1"
                })

    def handle_note(self, response):
        request_url = response.url
        building_id = request_url[request_url.rfind("/") + 1:request_url.rfind("-") + 1]
        page_sign = request_url[request_url.rfind("-") + 1:]
        # 获取整个doc
        context = response.doc
        for each_note in context("tbody[id^='pid']").items():
            # 这个md5对象，需要每次都新生成，否则生成的md5值会有问题
            hl_md5 = hashlib.md5()
            note = {}
            author = each_note.find("div.pls_user h3 a")
            # 作者链接
            author_link = author.attr("href")
            note["author_id"] = author_link[author_link.find("uid=") + 4:]
            author_actual_link = author_link.replace("muchong.com", "muchong.com/bbs")
            # 楼层及创建时间块
            floor_time_area = each_note.find("div[class='pls_info']")
            create_time = floor_time_area("em").text()
            note["create_time"] = create_time
            # 一楼是1楼，二楼是沙发，三楼是板凳，四楼是4楼
            raw_floor = floor_time_area("span a").text()
            floor = "2楼" if raw_floor == "沙发" else ("3楼" if raw_floor == "板凳" else raw_floor)
            note["floor"] = floor[:-1]
            raw_id = author.text() + create_time + floor[:-1]
            hl_md5.update(raw_id.replace(" ", "").encode(encoding='utf-8'))
            note["id"] = hl_md5.hexdigest()
            # 帖子内容区域
            content_area = each_note.find("td[class='plc_mind'] div[class='plc_Con']")
            # 赋值全局变量楼主帖子id
            if note["floor"] == "1":
                note["title"] = content_area("h1").text()
                # 如果是帖子的第一页,第一楼为全局id
                if int(page_sign) == 1:
                    note["id"] = building_id
            if content_area:
                target_id, content, device = self.handle_content(content_area, building_id)
                note["target_id"] = target_id
                note["content"] = content
                note["device"] = device
            category_names = context.find("span.breadcrumb")
            # 一级分类名称
            note["first_category_name"] = category_names("a:eq(1)").text()
            # 二级分类名称
            note["second_category_name"] = category_names("a:eq(2)").text()
            # 三级分类名称
            note["third_category_name"] = category_names("a:eq(3)").text()
            note["building_id"] = building_id
            self.note_projectdb.es.index("note", "project", note, note["id"])
            # 爬取作者
            self.crawl(author_actual_link, callback=self.handle_author, cookies={
                "Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564279",
                "Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569": "1522564172",
                "_discuz_pw": "9a1449a8990d49a6",
                "_discuz_uid": "3302227",
                "_emuch_index": "1",
                "_ga": "GA1.2.1902872401.1522564172",
                "_gat": "1"
            })

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
        author["note_num"] = note_num_src.replace(note_num_desc, "").replace("\n", "").replace(" ", "")
        composite_info = context("div.space_index table tr").find("div:last").text()
        # 截取,切片字符串
        composite_info = composite_info[composite_info.find("听众"):].split("\xa0")
        # 分组存储
        # if len(composite_info) > 0 and not composite_info[0] == "":
        #    author["fans_num"] = composite_info[0][composite_info[0].find(":")+1:].replace(" ", "")
        #    print(author["fans_num"])
        # if len(composite_info) > 1 and not composite_info[1] == "":
        #    author["flower_num"] = composite_info[1][composite_info[1].find(":")+1:].replace(" ","")
        #    print(author["flower_num"])
        # 查看获取的红花
        flowers = context("table.userinfo:eq(2)").find("table")("tr td")
        # flower_num = 0
        for flower_row in flowers.items():
            flower = {}
            flower["owner_id"] = author["id"]
            flower["owner_name"] = author["name"]
            flower["sender_name"] = flower_row("a").text()
            flower_num = flower_row("font").text()[1:-1]
            flower["flower_num"] = "1" if flower_num == "" else flower_num
            # flower_num = flower_num+ int(flower["flower_num"])
            self.flower_projectdb.es.index("flower", "project", flower)
        # author["flower_num"] = flower_num
        hl_md5.update(author["id"].encode(encoding='utf-8'))
        self.author_projectdb.es.index("author", "project", author, hl_md5.hexdigest())


