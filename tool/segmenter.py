#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba
import re

def segment(sentence, cut_all=True):
    # jieba.load_userdict(file_name)
    sentence = sentence.replace('\n', '').replace('\u3000', '').replace('\u00A0', '')
    # sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all))
    # sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all,HMM=True))
    sentence = ' '.join(jieba.cut_for_search(sentence, HMM=True)) #搜索模式 发现更多的词汇
    return re.sub('[a-zA-Z0-9.。:：,，)）(（！!??”“\"]', '', sentence).split()

def segment_no_jieba(sentence, cut_all=True):
    # jieba.load_userdict(file_name)
    sentence = sentence.replace('\n', '').replace('\u3000', '').replace('\u00A0', '')
    # sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all))
    # sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all,HMM=True))
    #sentence = ' '.join(jieba.cut_for_search(sentence, HMM=True)) #搜索模式 发现更多的词汇
    return re.sub('[a-zA-Z0-9.。:：,，)）(（！!??”“\"]', '', sentence).split()
