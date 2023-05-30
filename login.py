# -*- coding: UTF-8 -*-
import http.cookiejar

import requests

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"

puSeesion = requests.session()
postUrl = "https://pocketuni.net/index.php?app=home&mod=Public&act=doLogin"
header = {
    "UserAgent": userAgent,
    'Host': 'pocketuni.net',
    'Pragma': 'no-cache',
    'Referer': postUrl,
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
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',

}


def login(schoolid, number, password):
    puSeesion.cookies = http.cookiejar.LWPCookieJar(filename="Cookies")
    postData = {
        "sid": schoolid,
        "canRegister": "0",
        "number": number,
        "password": password
    }
    puSeesion.post(url=postUrl, data=postData, headers=header)
    puSeesion.cookies.save('Cookies')



