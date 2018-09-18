# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/09/18 上午8:17
describe: 二分搜索 在有序alist 中查找value
"""

def half_search(alist,value):
    l ,r= 0,len(alist)-1

    while l <= r:
        mid = (l+r) // 2
        if alist[mid] <value:
            l = mid +1
        elif alist[mid]>value:
            r = mid -1
        else:
            return mid+1
    return -1

if __name__ == "__main__":
    ll = [x for x in range(3,40,2)]
    print(half_search(ll,7))

