# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/09/18 上午12:58
describe: 快速排序
"""

def quicksort(alist):
    if len(alist) <=1 :
        return  alist
    else :
        return quicksort([lt for lt in alist[1:] if lt <alist[0]]) + alist[0:1]+ \
               quicksort([lt for lt in alist[1:] if lt >= alist[0]])


if __name__ == "__main__":
    from  random import randint
    ll = [randint(1,300) for x in range(50)]
    print(quicksort(ll))
