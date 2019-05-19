#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import emoji
#****************去重************

def duplicate(file):
    print('正在处理'+file)
    new_list = []
    count = 0
    for i in open(file):
        count += 1
        if i not in new_list:
            new_list.append(i)
        else:
            continue

    print('原来有'+str(count)+'条数据')
    print('去重后有'+str(len(new_list))+'条数据')
    print('=================')
    newtxt = "".join(new_list)
    f = (open(file,"w"))
    f.write(newtxt)
    f.close()



if __name__ == '__main__':

    # duplicate('/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/粤菜/点都德聚福楼.txt')
    # duplicate('/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/粤菜/富盈酒家.txt')
    # duplicate('/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/粤菜/广州酒家.txt')
    # duplicate('/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/粤菜/桃园明宴.txt')
    # duplicate('/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/粤菜/喜鹊茶餐厅.txt')
    kkk = emoji.demojize('这个巧克力好好吃 ⭐️')
    print(kkk)



