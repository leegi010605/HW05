#!/usr/bin/python

import sys

txtf=str(sys.argv[1])
num=int(sys.argv[2])

print(sys.argv[1],sys.argv[2])

f=open(txtf,'r')

lines=f.readlines()
for line in lines:
    print(line)

f.close()
