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
def crow(post_data):
    filename = '/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/粤菜/喜鹊茶餐厅菜名.txt'  ######<==========================改这里（你的文件目录，你多建几个比如xx1..xx2然后到时复制粘贴到一个文件）

    with open(filename, 'w')as f:
        # write = csv.writer(f)
        # f.write(codecs.BOM_UTF8)
        # for n in range(1,10):
        url = 'https://meishi.meituan.com/i/api/dish/poi'
        cookie = '__mta=213692715.1550482505256.1551063591941.1551063700093.63; _lxsdk_cuid=167a0b93ac7c8-0b6f1ee3f24191-35617600-13c680-167a0b93ac8c8; rvct=20; mtcdn=K; u=269038410; n=EMS216856095; lt=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; lsu=; token2=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; uuid=dba70c8292774026b87f.1550480685.2.0.0; unc=EMS216856095; IJSESSIONID=x6rirwsjgiirwuep9jxa21jp; iuuid=CA5BFE93F02E195F9E978182931247C314C8A051DB9063A77678CFBEF96397FD; isid=B9C18F76653E215BBD11F72368C5158C; oops=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; logintype=normal; _lxsdk=CA5BFE93F02E195F9E978182931247C314C8A051DB9063A77678CFBEF96397FD; webp=1; ci3=1; __utmc=74597006; p_token=znvd2yySZoO0T8BzaMuCKfjJnS4AAAAA6QcAABzKf71CUXJGFrDSVukuck3UFzGsSnGJ1idyIkS962uck1EmFWlH4IlxJP4L-J-qDA; _hc.v=446edf2d-c755-780f-5375-d96063eadff7.1550482505; ci=20; cityname=%E5%B9%BF%E5%B7%9E; pgv_pvi=4054856704; pgv_si=s7566086144; PHPSESSID=kbps5hm3j9o5al9ji49s9siii4; noguide=1; __utmz=74597006.1550741336.6.6.utmcsr=i.meituan.com|utmccn=AffProg|utmcmd=wandie|utmctr=61452.cps.22156087|utmcct=i.meituan.com/; lat=23.100169; lng=113.327754; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; latlng=22.744478,113.5954,1551063588373; client-id=be45cc28-7c59-4dfe-ad4a-8a5438a7455c; i_extend=C_b0E141277655520303592144466014887689661385_e7896938209494422025_a%e7%83%a4%e5%ae%b4Gimthomepagecategory11H__a100173__b7; __utma=74597006.1525354767.1550482502.1551063588.1551073891.8; _lxsdk_s=169236c3d14-cf-22e-a89%7C%7C1'
        head = {'Host': 'meishi.meituan.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Upgrade - Insecure - Requests': '1',
                'Referer': 'http://m.dianping.com/shop/95240689/dishlist',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
                'Cookie':cookie
                }
        data = post_data
        r = requests.post(url, data=data, headers=head, timeout=3)
        r.encoding = 'utf-8'
        r = r.json()
        allname = (r["data"]["list"])
        print(allname)
        for item in allname:
            f.write(item["name"]+'\n')
            # doc = pq(r.text)
            # # 解析每条评论
            # pinglunLi = doc("div.tag-title").items()
            # print(pinglunLi)
            # for data in pinglunLi:
            #     # aa = data("p").text()
            #     f.write(data+'\n')
        # print(type(pinglunLi))


if __name__ == '__main__':
    post_data = {"uuid":"dba70c8292774026b87f.1550480685.2.0.0","version":"8.3.3","platform":3,"app":"","partner":126,"riskLevel":1,"optimusCode":10,"originUrl":"http://meishi.meituan.com/i/poi/1515128?ct_poi=141277655520303592144466014887689661385_e7116259242414335981_a%25e5%2596%259c%25e9%25b9%258a%25e8%258c%25b6%25e9%25a4%2590%25e5%258e%2585&cevent=imt%2Fpoilist%2Fitem","poiId":1515128}

    crow(post_data)