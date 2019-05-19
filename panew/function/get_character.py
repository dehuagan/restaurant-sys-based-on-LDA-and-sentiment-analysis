#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
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

corpus = []
for i in open('/Users/gandehua/Desktop/论文＋毕设/raw_data/negative.txt'):

    corpus.append(seg_depart(i))

# print(corpus)


vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
word = vectorizer.get_feature_names()
print(word)