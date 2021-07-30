# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:30:13 2021

@author: nitac
"""


def selecta():
     in_=int(input('進貨幾個蘋果?'))
     return in_
 
def selectb():
     out=int(input('賣了幾個蘋果?'))
     money=out*price
     print('應收:'+str(money))
     return out
n=int(input('有幾個蘋果?'))
price=int(input('一顆多少錢?'))

sel=''
sell=[]
while sel !='e':
    print('-----------------------')
    print('(a)進貨')
    print('(b)出貨')
    print('(c)顯示營業額')
    print('(d)顯示庫存')
    print('(e)離開系統')
    
    sel=input()
    print('-----------------------')
    
    if sel=='a':
        in_=selecta()
        n=in_+n
    elif sel=='b':
        out=selectb()
        if n-out<0:
            print('庫存不夠')
        else:
            n=n-out
            sell.append(out)
    elif sel=='c':
        if len(sell)==0:
            print('今天沒有交易')
        else:
            print('今天有',len(sell),'筆交易')
            print('今天交易如下:')
            for s in sell:
                print(str(s)+'個')
            print('共收'+str(sum(sell)*price))
    elif sel=='d':
        print('蘋果庫存')
        f=n-out
        print(f)
        
    else:
        print('離開系統')
    








