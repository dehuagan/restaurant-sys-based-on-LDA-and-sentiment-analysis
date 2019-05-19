#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim import corpora, models


import jieba
import jieba.analyse
#去停用词

jieba.load_userdict('/Users/gandehua/Desktop/论文＋毕设/raw_data/specdict.txt')

def stopwordlist():
    stopwords = [line.strip() for line in open('/Users/gandehua/Desktop/论文＋毕设/raw_data/chinese_cut.txt', encoding='utf-8').readlines()]
    return stopwords

def seg_depart(sentence):
    # print('cutting words...')
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordlist()
    outlist = []
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t' and word != '\n':
                outlist.append(word)

    return outlist

filename = "/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/日韩料理/日韩料理pos/阪尚皇pos.txt"
outfilename = "/Users/gandehua/Desktop/论文＋毕设/raw_data/all_raw_data/日韩料理/newfiltwords.txt"

pos = []
for line in open(filename):
    pos.append(seg_depart(line))





print(pos)
pos_dict = corpora.Dictionary(pos)
pos_corpus = [pos_dict.doc2bow(i) for i in pos]
pos_lda = models.LdaModel(pos_corpus, num_topics=1, id2word=pos_dict)
for i in range(1):
    print(pos_lda.print_topic(i))  # 输出每个主题

# print(neg[2])