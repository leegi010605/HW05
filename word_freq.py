#!/usr/bin/python

import sys
import re

txtf=str(sys.argv[1])
num=int(sys.argv[2])

print(sys.argv[1],sys.argv[2])

f=open(txtf,'r')

lines=f.readlines()

for i in lines:
    i = re.sub("[-=+,#/\?:^.@*\"※~ㆍ!]", "", i) 
    words=i.split()
    #for word in words:

print(words)

#for i in range(0,len(sep),1):
   # if t_rmv in sep:
        

f.close()
