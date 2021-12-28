"""
一个简单的🌰，主要关于协程网络爬虫与邮件发送
务必使用py3.6及以上版本运行此文件

代码包含的内容:
- 协程爬取bilibili生活区5个小分区的热榜
- 爬取完成后发送邮件通知

请勿在作业中直接使用本代码，因为其存在以下已知问题：
- 不保证对热榜爬取的顺序
- 对于视频描述和标题中存在\n的情况没有处理，这将导致结果数据文件无法直接使用
- 邮件为私人邮箱，且有发信限制（每日上限450封，每秒上限200封），邮箱会在2022-01-01关闭STMP发信许可，请及时更换自己邮箱。
- 其他未知问题
"""

"""
名称  代号  tid 简介  url路由
生活(主分区) life    160     /v/life
搞笑  funny   138 各种沙雕有趣的搞笑剪辑，挑战，表演，配音等视频 /v/life/funny
家居房产    home    239 与买房、装修、居家生活相关的分享    /v/life/home
手工  handmake    161 手工制品的制作过程或成品展示、教程、测评类视频 /v/life/handmake
绘画  painting    162 绘画过程或绘画教程，以及绘画相关的所有视频   /v/life/painting
日常  daily   21  记录日常生活，分享生活故事   /v/life/daily
"""

import os
import time
import requests as rs
import asyncio
import aiohttp
import random
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

SAVE_PATH = './'
BASE_URL = 'https://s.search.bilibili.com/cate/search'
CATE_LIST = [138,239,161,162,21]
sleep_choice = [1,2,3,4,5]

# Email Configer
SMTP_SERVER = 'mail.buaa.edu.cn'
PORT = 465
FROM_ADDR = '19377184@buaa.edu.cn'
PASSWD = 'hexihexiang2000'
TO_ADDR = '19377184@buaa.edu.cn'

class BiliHotCrawler():
    def __init__(self,cate,limit=300):
        self.cate_id = cate
        self.limit = limit
        self.page = 1
        self.pagesize = 100
        self.bulid_param()
        self.url = BASE_URL
        
    def bulid_param(self):
        self.params = {
            'main_ver':'v3',
            'search_type':'video',
            'view_type':'hot_rank',
            'order':'click',
            'cate_id':self.cate_id,
            'page':self.page,
            'pagesize':self.pagesize,
            'time_from':20211110,
            'time_to':20211117
        }

    async def get_resp(self):
        time.sleep(random.choice(sleep_choice))
        self.bulid_param()
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url,params=self.params) as response:
                self.resp = await response.read()
        self.page += 1

    def save_resp(self):
        path = f"{SAVE_PATH}/{self.cate_id}.csv"
        with open(path,"a") as f:
            self.resp = eval(self.resp.decode('utf-8').replace('null','None').replace('false',"False").replace("true","True").replace("\n"," "))
            for item in self.resp["result"]:
                # 分类 排名 bv号 时长 播放量 弹幕 标题 封面 评论 收藏 描述 直链
                f.write(f'{self.cate_id},{item["rank_offset"]},{item["bvid"]},{item["duration"]},{item["play"]},{item["video_review"]},{item["title"]},{item["pic"]},{item["review"]},{item["favorites"]},{item["description"]},{item["arcurl"]}'.replace("\n"," ").encode('utf-8', 'replace').decode('utf-8'))
                f.write("\n")

    def log(self,isend=False):
        print(f"\rCrawlering {self.cate_id} {(self.page - 1)*self.pagesize}/{self.limit}",end="")
        if isend:
            print()

    async def start(self):
        while self.pagesize * self.page <= self.limit:
            self.log()
            await self.get_resp()
            self.save_resp()
        self.log(isend=True)


class BHCFactory():
    def __init__(self,cate_list):
        self.cate_list = cate_list

    def produce(self): # 相当于开了多个协程去分别爬取每个板块的热榜
        loop = asyncio.get_event_loop()
        tasks = [BiliHotCrawler(i).start() for i in self.cate_list]
        loop.run_until_complete(asyncio.wait(tasks))


class BiliNoticeMail:
    def __new__(cls, *args, **kwargs):
        if not hasattr(BiliNoticeMail, '_instance'):
            BiliNoticeMail._instance = object.__new__(cls, *args, **kwargs)
        return BiliNoticeMail._instance

    def __init__(self):
        self.server = SMTP_SSL(SMTP_SERVER, PORT)
        self.message = None
        pass

    def build_ready_message(self):
        self.message = MIMEText('下载完成', 'plain', 'utf-8')
        self.message['From'] = Header(FROM_ADDR, 'utf-8')
        self.message['To'] = Header(TO_ADDR, 'utf-8')
        self.message['Subject'] = Header('BiliReminder:Ready', 'utf-8')

    def notice(self):
        if self.message is None:
            raise ValueError('Message is none!')
        self.server.login(FROM_ADDR, PASSWD)
        self.server.sendmail(FROM_ADDR, [TO_ADDR], self.message.as_string())
        self.message = None
        self.server.quit()

    @classmethod
    def send_ready_mail(cls):
        noticer = cls()
        noticer.build_ready_message()
        noticer.notice()
        print("发信成功，请查收。")
        return noticer

def main():
    BHCFactory(CATE_LIST).produce()
    BiliNoticeMail.send_ready_mail()

if __name__ == '__main__':
    main()
