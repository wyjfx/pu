# -*- coding: UTF-8 -*-
import requests
import http.cookiejar
from bs4 import BeautifulSoup

puSeesion = requests.session()
puSeesion.cookies = http.cookiejar.LWPCookieJar(filename="Cookies")

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
header = {
    "UserAgent": userAgent,
    'Host': 'pocketuni.net',
    'Pragma': 'no-cache',
    'Referer': "hhttps://pocketuni.net/index.php?app=event&mod=Front&act=doAddUser&id=4962871",
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
}


def topu(puid):
    def gethash():
        hashtext = puSeesion.get(url=f"https://pocketuni.net/index.php?app=event&mod=Front&act=join&id={puid}",
                                 headers=header,
                                 cookies=puSeesion.cookies.load('Cookies')).text
        soups = BeautifulSoup(hashtext, 'html.parser').select('input')[2]
        value = str(soups)
        return value[value.index('value=') + 7:-3]

    def go():
        puSeesion.put(url=f"https://pocketuni.net/index.php?app=event&mod=Front&act=doAddUser&id={puid}",
                      data={'__hash__': str(gethash())},
                      headers=header,
                      cookies=puSeesion.cookies.load('Cookies')
                      )

    num=0
    while True:
        go()
        num+=1
        print(num)
