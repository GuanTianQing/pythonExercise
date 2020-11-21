# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:14:33 2020

@author: 秦观天
"""
import MidTermExam as MTE
w_dic=MTE.word_statistics('He_Deep_Residual_Learning_CVPR_2016_paper.txt')
w_dic=MTE.getWordFrenquency(w_dic)
MTE.data_visualization(w_dic)
outputpath='test.csv'
MTE.get_CSV(w_dic,outputpath)


    
    