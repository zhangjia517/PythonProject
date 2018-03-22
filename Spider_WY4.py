import requests
import urllib

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "vjuids=-8b8614a5.1620343c754.0.f655f821f7c76; _ntes_nnid=2d7c7a25c33f0aa45b82d3dd8a4cb190,1520473196383; _ntes_nuid=2d7c7a25c33f0aa45b82d3dd8a4cb190; __gads=ID=75ee827e4f95385c:T=1520473198:S=ALNI_MaxiunyyCsI6Ll1XvNlGxQ6zpYA1w; NTES_PASSPORT=cQ5rPQaIFjApGdhd4uslD.c2mVX1V2dZW.rkn4MCZURONK67NXivTdlvFqXnN7LdsasNdpkv.9R0.ay_94iUncEHvA_0eRNfnn8Agnl_a_9uny7k9S2WIpNdPWh96xBfdFmcLqVr46WzBb7XM151chJaVsD6yuEndun86ET06tx7bfCTDdCCpIuUv; P_INFO=m18600062650@163.com|1520824055|1|mail163|00&99|bej&1519869536&mail163#bej&null#10#0#0|186650&1|163&mail163|18600062650@163.com; nts_mail_user=undefined:-1:0; _iuqxldmzr_=32; Province=010; City=010; UM_distinctid=1621e11f82dec-0687afc810a72f-b353461-1fa400-1621e11f82e443; vjlast=1520473196.1520922919.11; mail_psc_fingerprint=92d645db4608e4f5e13935dff2ff5193; NTES_CMT_USER_INFO=50639063%7C%E6%80%82%E8%8A%B1%E8%9B%8B%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2844157ef90d476dbe844c589b36d70f20170420131526.jpg%7Cfalse%7CbTE4NjAwMDYyNjUwQDE2My5jb20%3D; vinfo_n_f_l_n3=e631ae6f0094f5cf.1.2.1520473196389.1520835794348.1520929656764; usertrack=ezq0plqpy+VSJwjmDvNdAg==; _ga=GA1.2.1705416657.1521077213; JSESSIONID-WYYY=fdViFnkE1msA8nzbmVV%2By4lWuh0fnD8O2Pi95TYvcqadpy%5Ch0%5CfZkKC2bgzyf2wf007%5Ch4KEem2k%2BkKob95Pw4KgakH%5CPl7cy3WQu4P5Z%2FNOusiDcW3swCJT%5CnY3oBUBSdXDnpMeRb79XtFkhiaXuHqpzonOv2FOKvlKisKCeFpn0B%5CQ%3A1521680023384",
    "Host": "music.163.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",

    # "Cache-Control": "max-age=0",
    # "Upgrade-Insecure-Requests": "1",
}

r = requests.get(
    "http://music.163.com/api/playlist/detail?id=3778678", headers=headers)  # 云音乐热歌榜

arr = r.json()['result']['tracks']

for i in range(2):
    name = str(i+1) + '_' + arr[i]['name'] + '.jpg'
    link = arr[i]['album']['picUrl']
    urllib.request.urlretrieve(link, 'E:\\Spider\\WY4\\' + name)
    print(name+'下载完成')

print('全部下载完成')
