# coding=utf-8
import csv
import time
from lxml import etree
import codecs
import requests
import json
from pyquery import PyQuery as pq
from lxml import html

#爬取数据
def crow():
    filename = '/Users/gandehua/Desktop/论文＋毕设/raw_data/小吃快餐/遵义羊汁羊味羊肉粉.csv'  ######<==========================改这里（你的文件目录，你多建几个比如xx1..xx2然后到时复制粘贴到一个文件）

    with open(filename, 'w', encoding='gb18030')as f:
        # write = csv.writer(f)
        # f.write(codecs.BOM_UTF8)
        for i in range(1, 101):
            print('正在爬第'+str(i)+'页')
            url = 'https://i.meituan.com/poi/63127715/feedbacks/page_'+str(i)
            cookie = '__mta=50137497.1550482500496.1550546585687.1550546670266.6; _lxsdk_cuid=167a0b93ac7c8-0b6f1ee3f24191-35617600-13c680-167a0b93ac8c8; lat=23.275846; lng=113.816503; rvct=20; mtcdn=K; u=269038410; n=EMS216856095; lt=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; lsu=; token2=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; uuid=dba70c8292774026b87f.1550480685.2.0.0; unc=EMS216856095; JSESSIONID=x6rirwsjgiirwuep9jxa21jp; IJSESSIONID=x6rirwsjgiirwuep9jxa21jp; iuuid=CA5BFE93F02E195F9E978182931247C314C8A051DB9063A77678CFBEF96397FD; isid=B9C18F76653E215BBD11F72368C5158C; oops=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; logintype=normal; _lxsdk=CA5BFE93F02E195F9E978182931247C314C8A051DB9063A77678CFBEF96397FD; webp=1; ci3=1; __utmc=74597006; p_token=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; _hc.v=446edf2d-c755-780f-5375-d96063eadff7.1550482505; _lx_utm=utm_source%3Dblog.csdn.net%26utm_medium%3Dreferral%26utm_content%3D%252Fxing851483876%252Farticle%252Fdetails%252F81842329; latlng=; __mta=50137497.1550482500496.1550540598913.1550540626340.4; ci=20; cityname=%E5%B9%BF%E5%B7%9E; __utma=74597006.1525354767.1550482502.1550543510.1550546586.4; __utmz=74597006.1550546586.4.4.utmcsr=meishi.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/i/poi/42159431; i_extend=C_b1Gimthomepagecategory11H__a100173__b4; _lxsdk_s=1690397e7ed-84e-370-81%7C%7C47; __utmb=74597006.3.9.1550546693088'
            head = {'Host': 'i.meituan.com',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Upgrade - Insecure - Requests': '1',
                    'Referer': 'https://meishi.meituan.com/i/?ci=30&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
                    'Cookie':cookie
                    }
            r = requests.get(url, headers=head, timeout=3)
            r.encoding = 'utf-8'
            doc = pq(r.text)
            # 解析每条评论
            pinglunLi = doc("div.comment").items()
            for data in pinglunLi:
                aa = data("p").text()
                f.write(aa+'\n')
    # print(type(pinglunLi))


if __name__ == '__main__':
    crow()