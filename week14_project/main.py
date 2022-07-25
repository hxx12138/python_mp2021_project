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
FROM_ADDR = ''
PASSWD = ''
TO_ADDR = ''

# 以Bilibili热榜为例，练习协程与非关系数据库的使用


# 1. 获取某一分区视频的排行榜信息，并从中解析出前 10000 条视频信息。
# 可使用协程爬取数据。注意协程应用的方式：发送http请求后，可以跳转到数据处理的函数中，
# 而不要跳到发送另一个http请求的函数中，因为由于b站的风控较为严格，短时间大量的请求可能会导致ip被封禁。

class BiliHotCrawler():
    def __init__(self,cate,limit=10000):
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
            'time_from':20211117,
            'time_to':20211124
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
                title = str(item["title"]).replace('\n','。').replace(',',' ')
                description = str(item["description"]).replace('\n','。').replace(',',' ')
                # 分类 排名 bv号 时长 播放量 弹幕 标题 封面 评论 收藏 描述 直链
                f.write(f'{self.cate_id},{item["rank_offset"]},{item["bvid"]},{item["duration"]},{item["play"]},{item["video_review"]},{title},{item["pic"]},{item["review"]},{item["favorites"]},{description},{item["arcurl"]}'.replace("\n"," ").encode('utf-8', 'replace').decode('utf-8'))
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


# 2. 将视频信息存入MongoDB数据库，并记录此视频当时的排名和数据创建时间。


# 3. 爬取同一分区一周之后的热榜，并从中解析出前 10000 条视频信息。
# 对比两次结果并更新数据库，要求第一次结果需从数据库中取出。
# 根据以下规则更新数据库：对于仅在第二次排行榜中的视频，将信息存入数据库；
# 对于仅在第一次排行榜中的视频，将信息从数据库中删除；
# 对于两次排行榜都存在的视频，更新数据库，保留创建时间，增加更新时间字段，并更新排名。



# 4.（附加）可否从数据库中查询出两次排行榜中上升和下降排名前10的视频信息？



# 5.（附加）由于数据量比较大，数据库处理的时间可能较长，
# 可以考虑使用SMTP协议在数据库处理完成时通过邮件的形式通知你。相关链接：