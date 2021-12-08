import requests
from bs4 import BeautifulSoup
import re

headers = {
            'Connection': 'close',
            'Referer': 'https://music.163.com/',
            'Host': 'music.163.com',
            'cookie':'_iuqxldmzr_=32; _ntes_nnid=ed265e26829a49b91cc5111998ed40b5,1638765175886; _ntes_nuid=ed265e26829a49b91cc5111998ed40b5; NMTID=00OeDId2k5TPc6LUE5hvvk_T8n1WUYAAAF9jgQksw; WEVNSM=1.0.0; WNMCID=cwsnfi.1638765176193.01.0; WM_NI=ZINn8RyZmWmcTWz1GYW9YqCyQQOglSdjV8gfEa%2BcASZ0mkJeAwR%2BJs%2Brr%2F%2FvqcwUIvYVRrtg1rI78eJ6yM8Oewu6jxpPsZavNHO8haOiIhFW9MrR5ATvimTT66xVxbPPbUY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ad264b29500b0d74a91968fb7c14e829a9babf479f88dc0b6d75f9bb88a82b82af0fea7c3b92a9a97828fbb5abb86a3b8f0699889b6d2c65395e79792c273938f8188ef59a8b69ad9e66e87bfe584c4599af0a38cc96f83a99eccc979e9aebed0ae7eb3bdb9b6cc7e9b8a9e93f76df3ae87d8bb6f8aeab7aebb45a7a9bbd7e974b490bdbbe47e8e9881d9eb6b8db78789c55dfb93beb3b84b98aaa78ed760f6eab8b7fb6a9490aeb6dc37e2a3; WM_TID=7gbQGeFMm5pBAQEAQQJ%2FtpXtRTBdlBK9; __csrf=e07368def95ca885b1d6ff1a4eef01b9; MUSIC_U=9de0b492647e4661440c5416dc69d1ba6498a5abc5c28ddae42fcf9a08ec2b76194671dccbe0aa2318da7799f7fc9a395d804606272b563e22fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; ntes_kaola_ad=1; JSESSIONID-WYYY=Ep8fVncpMRPyDy7lFfOIWfDs6%2FSr9d3Q6dyId0vHhzuIIqen6N%2F7%2F9HKB4%2BGbDKXdaBDTFlpAetxDm3vpm9DtwMfF2uwbdtbdpwbmOUpzdDYY%2Fah%2B9kaeGjtlr12c5q3J1pbMzKSt49zHdJqjZjpiBDTdABEwMPvR6b1HUkHuhrWFZtt%3A1638797589866',
            "Accept-Encoding": "identity",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
           }

for i in range(0,1300,35):

    path = 'https://music.163.com'

    url = 'https://music.163.com/discover/playlist/?order=hot&cat=说唱&limit=35&offset=' + str(i)
    response = requests.session().get(url=url,headers=headers)
    html = response.content.decode('utf-8')

    playlist_ids = []
    playlist_ids.extend(re.findall(r'playlist\?id=(\d+?)" class="msk"',response.text))
    #print(playlist_ids)

    #patt=re.compile('<article.*</article>',re.S)
    #print(html)

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




    break