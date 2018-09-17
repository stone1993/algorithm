# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/09/17 下午9:46
describe:
"""



def fixDown(a, k, n):  # 自顶向下堆化，从k开始堆化
    while 2 * k <= n:
        if 2*k +1> n:
            max_child = 2*k
        else:
            if a[2*k+1] <a[2*k]:
                max_child = 2*k
            else:
                max_child =2*k+1
        if a[max_child] >a[k]:
            a[max_child],a[k] = a[k],a[max_child]
            k = max_child
        else:
            break


def heapSort(l):
    l = [0]+l #经典模式
    n = len(l) - 1
    for i in range(n // 2, 0, -1):
        fixDown(l, i, n)
    while n > 0:
        l[1], l[n] = l[n], l[1]
        n -= 1
        fixDown(l, 1, n)
    return l[1:]


l = [26, 5, 77, 1, 61, 11, 59, 15, 48, 19]  # 第一个元素不用，占位

res = heapSort(l)
print(res)