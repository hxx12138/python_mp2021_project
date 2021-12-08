# -*- coding:utf-8 -*-
import requests,os,json
from bs4 import BeautifulSoup

print(
    '''
    --------------------------------------

              网易云音乐歌单下载

                            by:冷溪凌寒
                                 V 1.1
    --------------------------------------
    '''
)


headers = {
    'Connection': 'close',
    'Referer': 'https://music.163.com/',
    'Host': 'music.163.com',
    'cookie':'_iuqxldmzr_=32; _ntes_nnid=ed265e26829a49b91cc5111998ed40b5,1638765175886; _ntes_nuid=ed265e26829a49b91cc5111998ed40b5; NMTID=00OeDId2k5TPc6LUE5hvvk_T8n1WUYAAAF9jgQksw; WEVNSM=1.0.0; WNMCID=cwsnfi.1638765176193.01.0; WM_NI=ZINn8RyZmWmcTWz1GYW9YqCyQQOglSdjV8gfEa%2BcASZ0mkJeAwR%2BJs%2Brr%2F%2FvqcwUIvYVRrtg1rI78eJ6yM8Oewu6jxpPsZavNHO8haOiIhFW9MrR5ATvimTT66xVxbPPbUY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ad264b29500b0d74a91968fb7c14e829a9babf479f88dc0b6d75f9bb88a82b82af0fea7c3b92a9a97828fbb5abb86a3b8f0699889b6d2c65395e79792c273938f8188ef59a8b69ad9e66e87bfe584c4599af0a38cc96f83a99eccc979e9aebed0ae7eb3bdb9b6cc7e9b8a9e93f76df3ae87d8bb6f8aeab7aebb45a7a9bbd7e974b490bdbbe47e8e9881d9eb6b8db78789c55dfb93beb3b84b98aaa78ed760f6eab8b7fb6a9490aeb6dc37e2a3; WM_TID=7gbQGeFMm5pBAQEAQQJ%2FtpXtRTBdlBK9; __csrf=e07368def95ca885b1d6ff1a4eef01b9; MUSIC_U=9de0b492647e4661440c5416dc69d1ba6498a5abc5c28ddae42fcf9a08ec2b76194671dccbe0aa2318da7799f7fc9a395d804606272b563e22fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; ntes_kaola_ad=1; JSESSIONID-WYYY=Ep8fVncpMRPyDy7lFfOIWfDs6%2FSr9d3Q6dyId0vHhzuIIqen6N%2F7%2F9HKB4%2BGbDKXdaBDTFlpAetxDm3vpm9DtwMfF2uwbdtbdpwbmOUpzdDYY%2Fah%2B9kaeGjtlr12c5q3J1pbMzKSt49zHdJqjZjpiBDTdABEwMPvR6b1HUkHuhrWFZtt%3A1638797589866',
    "Accept-Encoding": "identity",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
}
s = requests.session() # 保持已登录状态
format = '{0:<10}\t{1:{3}<10}\t{2:<10}' # 输出规则

def get_list(url): # 获取歌单列表
    try:
        response = s.get(url, headers=headers,verify=False).content # 获取网页
        soup = BeautifulSoup(response, 'html.parser') # html格式
        lis = list(soup.find('ul')) # 寻找ul标签
        father_list = [str(soup.find('h2').string)] # 获取歌单名字到表[0]
        for i in lis:
            son_list = []
            son_list.append(str(len(father_list)) + '.') # 序号
            son_list.append(i.a.string) # 歌曲名称
            son_list.append(str(i.a.get('href'))[str(i.a.get('href')).find('=') + 1:-1] + str(i.a.get('href'))[-1]) # 歌曲链接
            father_list.append(son_list) # 添加到列表

    except:
        print("\n\t歌曲链接输入错误") # 错误情况
        exit('ERROR!')

    print("从'{}'中找到了{}条歌曲".format(str(soup.find('h2').string), len(father_list) - 1))
    return father_list


def mkdir(dir):#创建文件夹
    dir = dir.translate({ord(i): None for i in '/\\:*?"<>|'}) # 将 /\:*?"<>| 文件不能命名的符号去除

    isExists=os.path.exists(dir)#判断是否创建了文件夹
    if not isExists:
        os.makedirs(dir)#创建文件夹
        print("创建文件夹'%s'，将图片放入'%s'文件夹内。"%(dir,dir))
    else:
        print("已经有'%s'文件夹，将图片放入'%s'文件夹内。"%(dir,dir))


def download(list):#根据歌曲列表下载歌曲
    print('---------------------------------------------------------------------------------------------------')
    print('序号            歌曲名称                歌曲链接')
    for i in list:
        if list.index(i)==0:
            continue
        else:
            i[1] = i[1].translate({ord(i): None for i in '/\\:*?"<>|'}) # 将 /\:*?"<>| 文件不能命名的符号去除

            print(format.format(i[0], i[1], 'http://music.163.com/song/media/outer/url?id=' + i[2] + '.mp3', chr(12288))) # 排版
            # song_url = "https://link.hhtjim.com/163/" + i[2] + ".mp3" # 外链地址

            temp_url = "https://api.imjad.cn/cloudmusic/?type=song&id=" + i[2] # 外链地址
            temp_jsons = requests.get(temp_url).text
            temp_list=json.loads(temp_jsons).get('data')
            song_url=temp_list[0]["url"]
            song = requests.get(song_url).content # 获取歌曲源
            with open(list[0] +'/'+ i[1] + '.mp3', 'wb') as f: # 写入文件夹
                f.write(song)
                f.close()

    print('---------------------------------------------------------------------------------------------------')
    print('下载结束！')

def download_song(id,url):#根据歌曲列表下载歌曲
    response = s.get(url, headers=headers).content # 获取网页
    soup = BeautifulSoup(response, 'html.parser') # html格式
    name = str(soup.find('em').string) # 获取歌曲名
    print('---------------------------------------------------------------------------------------------------')
    name = name.translate({ord(i): None for i in '/\\:*?"<>|'}) # 将 /\:*?"<>| 文件不能命名的符号去除
    print(format.format(1, name, 'http://music.163.com/song/media/outer/url?id=' + id + '.mp3', chr(12288))) # 排版

    temp_url = "https://api.imjad.cn/cloudmusic/?type=song&id=" + id # 外链地址
    temp_jsons = requests.get(temp_url).text
    temp_list=json.loads(temp_jsons).get('data')
    song_url=temp_list[0]["url"]
    song = requests.get(song_url).content # 获取歌曲源
    with open(name + '.mp3', 'wb') as f: # 写入文件夹
        f.write(song)
        f.close()

    print('---------------------------------------------------------------------------------------------------')
    print('下载结束！')

'''choose=input("请选择下载模式\n1为根据歌单ID下载列表歌曲\n2为根据歌曲ID下载单首歌曲\n")
if(choose=="1"):
    search=input("请输入歌单ID:")
    url="https://music.163.com/playlist?id="+search # 歌单地址
    music_list=get_list(url) # 获取歌单列表
    mkdir(music_list[0]) # 创建文件夹
    download(music_list) # 通过歌单列表下载音乐
elif(choose=="2"):
    search=input("请输入歌曲ID:")
    url="https://music.163.com/song?id="+search # 歌曲地址
    download_song(search,url)
else:
    print("输入错误！")'''


'''for i in range(0,1300,35):
    url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E8%AF%B4%E5%94%B1&limit=35&offset=' + str(i)
    music_list=get_list(url) # 获取歌单列表
    mkdir(music_list[0]) # 创建文件夹
    download(music_list) # 通过歌单列表下载音乐
    break'''

id = 2695101341
search=input("请输入歌单ID:")
url="https://music.163.com/playlist?id="+search # 歌单地址


music_list=get_list(url) # 获取歌单列表
mkdir(music_list[0]) # 创建文件夹
# download(music_list) # 通过歌单列表下载音乐