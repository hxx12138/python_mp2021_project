from multiprocessing import Queue
import requests
from bs4 import BeautifulSoup
import re
from threading import Thread, currentThread
import queue
import urllib.request
import time
import aiofiles
import asyncio
import aiohttp

save_path = 'info/'
img_path = 'cover/'
produce_num = 0
consumer_num = 0

headers_1 = {
            'Connection': 'close',
            'Referer': 'https://music.163.com/',
            'Host': 'music.163.com',
            'cookie':'_iuqxldmzr_=32; _ntes_nnid=ed265e26829a49b91cc5111998ed40b5,1638765175886; _ntes_nuid=ed265e26829a49b91cc5111998ed40b5; NMTID=00OeDId2k5TPc6LUE5hvvk_T8n1WUYAAAF9jgQksw; WEVNSM=1.0.0; WNMCID=cwsnfi.1638765176193.01.0; WM_NI=ZINn8RyZmWmcTWz1GYW9YqCyQQOglSdjV8gfEa%2BcASZ0mkJeAwR%2BJs%2Brr%2F%2FvqcwUIvYVRrtg1rI78eJ6yM8Oewu6jxpPsZavNHO8haOiIhFW9MrR5ATvimTT66xVxbPPbUY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ad264b29500b0d74a91968fb7c14e829a9babf479f88dc0b6d75f9bb88a82b82af0fea7c3b92a9a97828fbb5abb86a3b8f0699889b6d2c65395e79792c273938f8188ef59a8b69ad9e66e87bfe584c4599af0a38cc96f83a99eccc979e9aebed0ae7eb3bdb9b6cc7e9b8a9e93f76df3ae87d8bb6f8aeab7aebb45a7a9bbd7e974b490bdbbe47e8e9881d9eb6b8db78789c55dfb93beb3b84b98aaa78ed760f6eab8b7fb6a9490aeb6dc37e2a3; WM_TID=7gbQGeFMm5pBAQEAQQJ%2FtpXtRTBdlBK9; __csrf=e07368def95ca885b1d6ff1a4eef01b9; MUSIC_U=9de0b492647e4661440c5416dc69d1ba6498a5abc5c28ddae42fcf9a08ec2b76194671dccbe0aa2318da7799f7fc9a395d804606272b563e22fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; ntes_kaola_ad=1; JSESSIONID-WYYY=Ep8fVncpMRPyDy7lFfOIWfDs6%2FSr9d3Q6dyId0vHhzuIIqen6N%2F7%2F9HKB4%2BGbDKXdaBDTFlpAetxDm3vpm9DtwMfF2uwbdtbdpwbmOUpzdDYY%2Fah%2B9kaeGjtlr12c5q3J1pbMzKSt49zHdJqjZjpiBDTdABEwMPvR6b1HUkHuhrWFZtt%3A1638797589866',
            "Accept-Encoding": "identity",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
           }

headers_2 = {
            'Connection': 'close',
            'Referer': 'https://music.163.com/',
            'Host': 'music.163.com',
            'cookie':'_iuqxldmzr_=32; _ntes_nnid=ed265e26829a49b91cc5111998ed40b5,1638765175886; _ntes_nuid=ed265e26829a49b91cc5111998ed40b5; NMTID=00OeDId2k5TPc6LUE5hvvk_T8n1WUYAAAF9jgQksw; WEVNSM=1.0.0; WNMCID=cwsnfi.1638765176193.01.0; __csrf=e07368def95ca885b1d6ff1a4eef01b9; MUSIC_U=9de0b492647e4661440c5416dc69d1ba6498a5abc5c28ddae42fcf9a08ec2b76194671dccbe0aa2318da7799f7fc9a395d804606272b563e22fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; ntes_kaola_ad=1; JSESSIONID-WYYY=gt9DxQeq+7Gv64k/sIGVdKnIUTPNN39ScrsFPZIIj6HBgPK/MHxqpe2fCBPkCONgdw/csT1q0FxS/yONqIN3x38jQmR\nDK26dxUr0D0ReTHOkousJ+YsKQ1a2EMujhyOM\38fb5T9wVZ\d9IXFMjacnYH948h9b\Tbh2Z8u1u0+j+Ny:1639554585199',
            "Accept-Encoding": "identity",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
           }

# 以爬取网易云歌单为例，练习多线程的使用。 

def download_img(path,title,src):
    title = title.replace('/',' ')
    with open(path+title+'.jpg','wb+') as f:
        response = urllib.request.urlopen(src)
        img = response.read()
        f.write(img)


# 编写爬虫函数
async def get_id(url):
    async with aiohttp.Clientsession(headers = headers_1) as session:
        async with session.get(url) as response:
            return response


# 1. 获取一个分类下的所有歌单的id。
# 观察url可以发现其页码规律：https://music.163.com/#/discover/playlist/?order=hot&cat=%E8%AF%B4%E5%94%B1&limit=35&offset=35。
# offset是本页开始的数据位置，第1页是0，第2页是35。分类参数是utf-8编码后的汉字"说唱"，使用str.encode可以处理。


class produce_id(Thread):

    def __init__(self,pages,q):
        super().__init__()
        self.pages = pages
        self.q = q
        self.num = 0

    def run(self):
        print(f'the no{currentThread().name} process_id has started')
        #for i in self.pages:
        for i in range(1):
            time.sleep(1)
            path = 'https://music.163.com'
            url = 'https://music.163.com/discover/playlist/?order=hot&cat=说唱&limit=35&offset=' + str(i)
            try:
                while True:
                    #response = requests.session().get(url=url,headers=headers_1)
                    response = get_id(url)
                    time.sleep(1)
                    if response != []:
                        break
            except:
                print('网络请求错误')
            html = response.content.decode('utf-8')

            playlist_ids = []
            playlist_ids.extend(re.findall(r'playlist\?id=(\d+?)" class="msk"',response.text))
            #print(playlist_ids)

            soup = BeautifulSoup(html, 'html.parser')

            #test = soup.find('ul')
            #print(test)
            text = soup.find('ul',class_='m-cvrlst f-cb')
            #print(len(text))
            #print(text)
            id_list = []
            id_text = soup.select(".dec a")
            for i in range(len(id_text)):
                id_list.append(id_text[i]['href'])
            print(id_list)

            #print(title)

            #title_list = soup.select("#m-pl-container li")
            #print(title_list)
            self.q.put(id_list)


# 2. 对每个id，获取歌单的详细信息，至少包括：
# 歌单的封面图片（需把图片保存到本地）、歌单标题、创建者id、创建者昵称、介绍、歌曲数量、播放量、添加到播放列表次数、分享次数、评论数。
# 可以自行实现其他信息的获取。基本信息汇总到同一张表中，以csv文件保存。https://music.163.com/playlist?id=3037221581 

class consumer(Thread):

    def __init__(self,q):
        super().__init__()
        self.q = q
        self.num = 0

    def run(self):
        print(f'the no{currentThread().name} pconsumer has started')
        while True:
            id_list = self.q.get()
            print(id_list)
            if id_list == []:
                break
            path = 'https://music.163.com'
            for i in range(len(id_list)):
                time.sleep(1)
                id = id_list[i][-10:]
                url = path+id_list[i]
                try:
                    count = 1
                    while True:
                        response = requests.session().get(url=url,headers=headers_1)
                        html = response.content.decode('utf-8')
                        soup = BeautifulSoup(html, 'html.parser')
                        time.sleep(count)
                        if soup.find('p',class_='intr f-brk') != None:
                            break
                        response = requests.session().get(url=url,headers=headers_2)
                        html = response.content.decode('utf-8')
                        soup = BeautifulSoup(html, 'html.parser')
                        time.sleep(count)
                        if soup.find('p',class_='intr f-brk') != None:
                            break
                        count += 1
                except:
                    print(soup.find('p',class_='intr f-brk'))
                    print('网络超时')
                #html = response.content.decode('utf-8')
                #soup = BeautifulSoup(html, 'html.parser')
                #print(soup)

                # 歌单的封面图片（需把图片保存到本地）、歌单标题、创建者id、创建者昵称、介绍、歌曲数量、播放量、添加到播放列表次数、分享次数、评论数。

                # 歌单标题
                title = soup.find('h2',class_ = 'f-ff2 f-brk').text
                #print(title)

                # 图片下载
                img_info = soup.find('div',class_='cover u-cover u-cover-dj')
                img_url = img_info.find('img',class_='j-img')['data-src']
                img_id = id_list[i][-10:]

                download_img(img_path,title,img_url)
                #print(img_url)

                # 创建者昵称
                create_name = soup.find('span',class_='name').text.strip('\n')
                #print(create_name)
                
                # 创建者id
                create_id = soup.find('span',class_='name').select('a')[0]['href'][14:]
                #print(create_id)

                # 介绍
                describe = soup.find('p',class_='intr f-brk').text.replace('\n','\t').replace(',','，')
                #print(describe)

                # 歌曲数量
                song_num = soup.find('span','sub s-fc3').find('span').text
                #print(song_num)

                # 播放量
                play_num = soup.find('strong','s-fc6').text
                #print(play_num)

                # 添加到播放列表次数
                add_num = soup.find('a','u-btni u-btni-fav')['data-count']
                #print(add_num)

                # 分享次数
                share_num = soup.find('a','u-btni u-btni-share')['data-count']
                #print(share_num)

                # 评论数
                comment_num = soup.find('a','u-btni u-btni-cmmt').find('span').text
                #print(comment_num)

                with open(save_path+'说唱.csv','a+') as f:
                    f.write(id+','+title+','+create_name+','+create_id+','+str(describe)+','+song_num+','+play_num+','+add_num+','+share_num+','+comment_num+'\n')



# 3. 要求使用生产者-消费者模式实现，要求1作为生产者，每次请求后产生新的任务交给消费者，消费者执行要求2。


if __name__ == '__main__':

    q = queue.Queue()
    producer_list = []
    consumer_list = []
    with open(save_path+'说唱.csv','a+') as f:
        f.write('歌曲ID'+','+'歌单标题'+','+'创建者昵称'+','+'创建者id'+','+'介绍'+','+'歌曲数量'+','+'播放量'+','+'添加到播放列表次数'+','+'分享次数'+','+'评论数'+'\n')

    sheet = list(range(0,1300,35))
    p_t = produce_id(sheet,q)
    p_t.start()
    p_t.join()
    thread_num = 1
    '''num = len(sheet)//thread_num

    for i in range(thread_num-1):
        p_t = produce_id(sheet[num*i:num*(i+1)],q)
        producer_list.append(p_t)
    p_t = produce_id(sheet[num*(thread_num-1):],q)
    producer_list.append(p_t)'''

    for i in range(thread_num):
        c_t = consumer(q)
        consumer_list.append(c_t)

    '''for p in producer_list:
        p.start()
    for p in producer_list:
        p.join()'''
    for c in consumer_list:
        c.start()
    #p_t.join()
    for c in consumer_list:
        c.join()


    '''produce_thread = produce_id([0],q)
    produce_thread.start()
    produce_thread.join()

    consumer_thread = consumer(q)
    consumer_thread.start()
    consumer_thread.join()'''


# 4.（附加）爬虫程序往往需要稳定运行较长的时间，因此如果你的程序突然中 断或异常（比如网络或被封），如何能够快速从断点重启？

# 保留断点处的信息，包括断点处的文件保存路径，以及接下来要爬的网页地址，和其他在程序中需要保留的所有变量，并且在每一次成功执行后都进行一次更新。


# 5.（附加）爬虫程序往往需要比较友好的状态输出，因此可否专门有一个线程 动态地进行输出更新，来显示当前的状态，
# 比如程序连续运行的时长，要完成的 总页面数，其中有多少已被爬取，已收集的文件占用了多少空间，大概还需要多少时间才能完成，预计需要耗费多少硬盘空间等。

