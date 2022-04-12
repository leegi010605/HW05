#!/usr/bin/python

import sys
import re
import operator

txtf=str(sys.argv[1])
num=int(sys.argv[2])

print(sys.argv[1],sys.argv[2])

f=open(txtf,'r')
dic={}

lines=f.readlines()

for i in lines:
    i = re.sub("[-=+,#/\?:^.@*\"※~ㆍ!]", "", i) 
    words=i.split()
    for cnt in words:
        dic[cnt]=dic.get(cnt,0)+1

Sorted_dic=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)

for j in range(0,num,1):
    print(Sorted_dic[j][0].ljust(10),Sorted_dic[j][1].rjust(5))

f.close()
