#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
#去停用词

jieba.load_userdict('/Users/gandehua/Desktop/论文＋毕设/raw_data/specdict.txt')

def stopwordlist():
    stopwords = [line.strip() for line in open('/Users/gandehua/Desktop/论文＋毕设/raw_data/chinese_cut.txt', encoding='utf-8').readlines()]
    return stopwords

def seg_depart(sentence):
    print('cutting words...')
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordlist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

filename = "/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/日韩料理/pos.txt"
outfilename = "/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/日韩料理/newfiltwords.txt"

# outputs = open(outfilename, 'w')
with open(outfilename, 'w') as f:
    for line in open(filename):
        line_seg = seg_depart(line)
        f.write(line_seg+'\n')