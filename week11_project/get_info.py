from os import name
from bs4.element import CharsetMetaAttributeValue
import requests
from bs4 import BeautifulSoup
import urllib.request

save_path = 'info/'

headers = {
            'Connection': 'close',
            'Referer': 'https://music.163.com/',
            'Host': 'music.163.com',
            'cookie':'_iuqxldmzr_=32; _ntes_nnid=ed265e26829a49b91cc5111998ed40b5,1638765175886; _ntes_nuid=ed265e26829a49b91cc5111998ed40b5; NMTID=00OeDId2k5TPc6LUE5hvvk_T8n1WUYAAAF9jgQksw; WEVNSM=1.0.0; WNMCID=cwsnfi.1638765176193.01.0; WM_NI=ZINn8RyZmWmcTWz1GYW9YqCyQQOglSdjV8gfEa%2BcASZ0mkJeAwR%2BJs%2Brr%2F%2FvqcwUIvYVRrtg1rI78eJ6yM8Oewu6jxpPsZavNHO8haOiIhFW9MrR5ATvimTT66xVxbPPbUY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ad264b29500b0d74a91968fb7c14e829a9babf479f88dc0b6d75f9bb88a82b82af0fea7c3b92a9a97828fbb5abb86a3b8f0699889b6d2c65395e79792c273938f8188ef59a8b69ad9e66e87bfe584c4599af0a38cc96f83a99eccc979e9aebed0ae7eb3bdb9b6cc7e9b8a9e93f76df3ae87d8bb6f8aeab7aebb45a7a9bbd7e974b490bdbbe47e8e9881d9eb6b8db78789c55dfb93beb3b84b98aaa78ed760f6eab8b7fb6a9490aeb6dc37e2a3; WM_TID=7gbQGeFMm5pBAQEAQQJ%2FtpXtRTBdlBK9; __csrf=e07368def95ca885b1d6ff1a4eef01b9; MUSIC_U=9de0b492647e4661440c5416dc69d1ba6498a5abc5c28ddae42fcf9a08ec2b76194671dccbe0aa2318da7799f7fc9a395d804606272b563e22fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; ntes_kaola_ad=1; JSESSIONID-WYYY=Ep8fVncpMRPyDy7lFfOIWfDs6%2FSr9d3Q6dyId0vHhzuIIqen6N%2F7%2F9HKB4%2BGbDKXdaBDTFlpAetxDm3vpm9DtwMfF2uwbdtbdpwbmOUpzdDYY%2Fah%2B9kaeGjtlr12c5q3J1pbMzKSt49zHdJqjZjpiBDTdABEwMPvR6b1HUkHuhrWFZtt%3A1638797589866',
            "Accept-Encoding": "identity",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
           }

def download_img(id,src):
    with open(id+'.jpg','wb+') as f:
        response = urllib.request.urlopen(src)
        img = response.read()
        f.write(img)
        

def main():
    sheet = 0
    with open(save_path+str(sheet)+'说唱.csv','a+') as f:
        f.write('歌曲ID'+','+'歌单标题'+','+'创建者昵称'+','+'创建者id'+','+'介绍'+','+'歌曲数量'+','+'播放量'+','+'添加到播放列表次数'+','+'分享次数'+','+'评论数'+'\n')
    id_list = ['/playlist?id=6952442013', '/playlist?id=2695101341', '/playlist?id=6862602894', '/playlist?id=6700242542', '/playlist?id=6970792582', '/playlist?id=5395488578', '/playlist?id=6654532835', '/playlist?id=4952648595', '/playlist?id=2875321368', '/playlist?id=5269453086', '/playlist?id=2394125021', '/playlist?id=4959088044', '/playlist?id=4867926094', '/playlist?id=2049779104', '/playlist?id=537367797', '/playlist?id=2841424429', '/playlist?id=3215209929', '/playlist?id=2873336061', '/playlist?id=5203647472', '/playlist?id=2679916677', '/playlist?id=5295292555', '/playlist?id=2834027258', '/playlist?id=6611168504', '/playlist?id=6663187462', '/playlist?id=5013820355', '/playlist?id=6610703103', '/playlist?id=2621595367', '/playlist?id=3097267488', '/playlist?id=2644743965', '/playlist?id=2523624603', '/playlist?id=5363801096', '/playlist?id=2689902290', '/playlist?id=2688991686', '/playlist?id=5206470585', '/playlist?id=6708035697']
    path = 'https://music.163.com'
    for i in range(len(id_list)):
        id = id_list[i][-10:]
        url = path+id_list[i]
        response = requests.session().get(url=url,headers=headers)
        html = response.content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)

        # 歌单的封面图片（需把图片保存到本地）、歌单标题、创建者id、创建者昵称、介绍、歌曲数量、播放量、添加到播放列表次数、分享次数、评论数。

        # 图片下载
        '''img_info = soup.find('div',class_='cover u-cover u-cover-dj')
        img_url = img_info.find('img',class_='j-img')['data-src']
        img_id = id_list[i][-10:]

        #download_img(img_id,img_url)
        print(img_url)'''

        # 歌单标题
        title = soup.find('h2',class_ = 'f-ff2 f-brk').text
        #print(title)

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

        with open(save_path+str(sheet)+'说唱.csv','a+') as f:
            f.write(id+','+title+','+create_name+','+create_id+','+str(describe)+','+song_num+','+play_num+','+add_num+','+share_num+','+comment_num+'\n')

main()