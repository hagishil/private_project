
from collections import deque
def solution(n:int,lost:list,reserve:list)->int:



    tmp=[x for x in lost for y in reserve if x==y]
    if len(tmp)!=0:
        for i in tmp:
            lost.pop(lost.index(i))
            reserve.pop(reserve.index(i))
    if len(lost)!=0 and len(reserve)!=0:
        if lost[0]<=reserve[0]:
            tmp=[[x,y] for x in lost for y in reserve if x-y==-1]
            for i in tmp:
                lost.pop(lost.index(i[0]))
                reserve.pop(reserve.index(i[1]))
        else:
            tmp=[[x,y]for x in lost for y in reserve if x-y==1]
            for i in tmp:
                lost.pop(lost.index(i[0]))
                reserve.pop(reserve.index(i[1]))

    return n-len(lost)







import collections


def solution_2(nums):
    tmp = (','.join([str(x) for x in nums])).split(',')

    num_set = collections.defaultdict(list)
    for i in tmp:
        num_set[i[0]].append(i)

    tmp = collections.defaultdict(list)
    for (key, value) in sorted(num_set.items(), reverse=True):
        tmp[key] = value

    for j in tmp.keys():
        tmp[j].sort(reverse=True)

        check=-1
        for i in range(0,len(tmp[j])):
            back=[]
            if(tmp[j][i]==j):
                check=i
            if(tmp[j][i][1]<j):
                back.append(tmp[j][i])
        if(check>0):
            tmp[j]=[]


        tmp[j] = ''.join(tmp[j]).split()

    result = ''
    for j in tmp.keys():
        result = result + tmp[j].pop()
    return result


import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def f_fun(a=1, b=1, c=1) -> str:
    fun = defaultdict(int)
    fun['x^2'] = a
    fun['x'] = b
    fun['c'] = c
    return fun


def df_fun(a: f_fun):
    df_dx = defaultdict(int)

    for (i, j) in a.items():
        if i == 'x^2':
            df_dx['x'] = 2 * j
        if i == 'x':
            df_dx['c'] = j

    return df_dx



