# -*- coding: utf-8 -*-
import os
import requests
from lxml import html

headers = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
    'Connection': 'Keep-Alive',
    'Cookie': 'aliyungf_tc=AQAAAJTSKDb6Fg8AI/Alas9Q0s62ZmS7; l_n_c=1; q_c1=8b6ca57326bd473e9067d92a24db9751|1521010610000|1521010610000; r_cap_id=ZTQxZDE5ZTZjZmM2NDRkODk5MGFmZWVkNjFjMThiZjA=|1521010610|379b42d39d5671f018ba689fc23de5492ef5ce3c; cap_id=M2IwODJmYzlmNWViNDMyMjkyYjFiNThjMmIxNTFlNDg=|1521010610|33e55947b39dd1971ea061ac1ce48b8769524df7; l_cap_id=OTU4NjFlOTVhYzIyNDZhYjg5NGZmODA3ZDk2NGUyMTA=|1521010610|37809e9eea8948abd3a403f0e7f39eb24ef2654a; n_c=1; __DAYU_PP=AYrjJI6Jjf6ibFmYbFEV321b6f025f0f; _xsrf=842a6c04-0343-4eeb-ab9b-57095ea82aa9; capsion_ticket=2|1:0|10:1521010612|14:capsion_ticket|44:M2U5ZDNkOTRiNGU1NDkyNzlkMjYxMzYxM2ViNTcwNTM=|1bd69b9e8b903852acf055e4cba161fe43b7aed945da0252e88683a533a38e38; _zap=f2605d33-fd8c-4464-a1f8-ce31fb60c858; z_c0=2|1:0|10:1521010623|4:z_c0|80:MS4xTkp3UEFBQUFBQUFtQUFBQVlBSlZUYjhWbGx0VDdWQTVzS3FRdG02ZWZaYm82YVpzV1hySWVRPT0=|0eb208924133f1c33cc6dd431f47b09ab42e37e66f3efd55d9479f24c7b02b6c; d_c0=AHBrqr7mSA2PThadFZpF44XNZ0Qg6Nsy5Vw=|1521010625; __utma=51854390.428498068.1521010657.1521010657.1521010657.1; __utmb=51854390.0.10.1521010657; __utmc=51854390; __utmz=51854390.1521010657.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signup; __utmv=51854390.100-1|2=registration_date=20130630=1^3=entry_date=20130630=1',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
}


def save(text, filename='temp', path='E:\\Spider\\ZhiHu\\Beauty\\'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'wb') as f:
        print('output:', fpath)
        f.write(text)


def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = image_url.split('zhimg.com/')[-1]
    save(page, filename)


def crawl(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    print(page)
    root = html.fromstring(page)

    image_urls = root.xpath('//img[@data-original]/@data-original')
    print(image_urls)
    for image_url in image_urls:
        save_image(image_url)


if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/27364360'
    crawl(url)
