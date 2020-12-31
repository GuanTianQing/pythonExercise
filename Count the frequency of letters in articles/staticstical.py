# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:41:28 2020

@author: 秦观天
"""
import matplotlib.pyplot as plt
import pandas as pd

def word_statistics(filename):
    #读入文章
  
    f=open(filename,"rt",encoding='utf-8')
    file2str=f.read()
    '''查看key是否在字典中，在的话对应的变量加一，
不再的话就新增加一个key并使其的值为一'''
''''当以指定“键”为下标给字典对象赋值时，若该“键”存在则表示修改该“键”对应的“值”，
若不存在则表示为字典对象添加一个新的“键-值对”。
''''
    w_dic = {}
    for c in file2str:        
        if( ( ord('A') <= ord(c) <=ord('Z') ) or
            ( ord('a') <= ord(c) <=ord('z') ) ) :            
            c=c.upper()
            if c in w_dic:
                w_dic[c]=w_dic[c]+1
            else:
                w_dic[c]=1
    #字典按关键字排序 
    d=sorted(w_dic.items(), key=lambda d: d[0], reverse=False)  
    w_dic=dict(d) 
    #print(w_dic)
    return w_dic

def getWordFrenquency(w_dic):    
     totalN=0
     for i in w_dic:
         totalN+=w_dic[i]
     print('totalN',totalN)
     
     for i in w_dic:
         #print(w_dic[i])
         l=[]
         l.append(w_dic[i])
         w_f=w_dic[i]/totalN
         l.append(w_f)
         w_dic[i]=l
     return w_dic     
  
def get_CSV(w_dic,outputpath):
    df1=pd.DataFrame(columns=('字母','频数','频率'))
    
    c=0
    for i in w_dic:
        data=[{'字母':i, '频数':w_dic[i][0], '频率':w_dic[i][1]}]
        df2=pd.DataFrame(data,index=[str(c)],columns=('字母','频数','频率'))
        df1=df1.append(df2)
        c+=1
        
    df1.to_csv(outputpath,sep=',',index=False,header=False)
    
def data_visualization(w_dic):
     for i in w_dic:
        print(i,' ',w_dic[i][0],' ',w_dic[i][1])
    
     #用于显示中文（windows系统适用）     
     plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
     plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号  
     
     plt.title('英文文献中26字母词频统计结果图',fontsize=25)
     
     x=list(w_dic.keys())
     y=[]
     for i in w_dic:
         y.append(w_dic[i][1])
     #y=list(w_f.values())   
     plt.ylabel('26英文字母',fontsize=15)
     plt.xlabel('字母在文献中出现的频率',fontsize=15)
     # 添加数据标签，也就是给柱子顶部添加标签
     for a, b in zip(x, y):
         plt.text(b+0.009, a, '%.4f'%b, ha='right', 
                  va='center', fontsize=25)
     plt.barh(x,y)
     
     plt.show()











               
