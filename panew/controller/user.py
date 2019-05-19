#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request,render_template,flash,abort,url_for,redirect,Flask,session
import json
from flask import jsonify
from panew import db
import sys
from sqlalchemy import and_, or_
reload(sys)

sys.setdefaultencoding("utf8")
from panew import app
from panew.model.dessert import dessert
from panew.model.canton import canton
from panew.model.chuanxiang import chuanxiang
from panew.model.fastfood import fastfood
from panew.model.good_rate import good_rate
from panew.model.hotpot import hotpot
from panew.model.jk import jk
from panew.model.western_food import western_food




def insert_sort(arr):
    for i in range(1,len(arr)):
        print arr[i]
        if(arr[i]['score']<arr[i-1]['score']):
            tmp = arr[i]
            j = i-1
            while(j>=0 and tmp<arr[j]['score']):
                arr[j+1] = arr[j]
                j -=1
            arr[j+1] = tmp
    return arr


@app.route('/test')
def get_dessert():
    a = dessert.query.all()
    datalist = []
    for i in a:
        datadict = {}
        print i
        datadict["name"] = i.res_name
        datadict["good"] = i.good
        print type(i.good)
        datalist.append(datadict)
    msg = datalist
    response = {'data': msg}
    return jsonify(response)


@app.route('/rate',methods=['GET','POST'])
def get_rate():
    b = good_rate.query.all()
    datalist = []
    for i in b:
        datadict = {}
        print i
        datadict["name"] = i.res_name
        datadict["rate"] = i.rate

        datalist.append(datadict)
    msg = datalist
    response = {'data': msg}
    return jsonify(response)

@app.route('/spec',methods=['GET','POST'])
def get_spec():
    if request.method == 'POST':
        print 'success'
        print request.get_data()
        data = json.loads(request.get_data())
        print data
        sort = data["sort"]
        tags = data["tags"]
        query_str = 'SELECT * FROM `'+sort + '` WHERE `'
        for i in tags:
            query_str += i
            query_str += '` !=0 AND `'
        query_last = query_str[:-5]
        spec = db.session.execute(query_last)
        datalist = []
        for i in spec:  #循环搜索所得的餐厅
            ratedata = good_rate.query.filter_by(res_name=i.res_name).first()
            rate = ratedata.rate      #得到好评率
            count = 0
            for j in tags:
                count += i[j]    #得到相应的tag的权重
            score = rate*0.6+count*0.4  #得到最后总得分
            datadict = {}
            datadict["name"] = i.res_name
            datadict["score"] = score
            datalist.append(datadict)
        msg = insert_sort(datalist)#排序
        response = {'data': msg}
        return jsonify(response)