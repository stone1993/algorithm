# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/09/17 下午11:00
describe: 归并排序
时间复杂度： nlog n
"""

def mergesort(alist):
    if len(alist) >1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i,j,k = 0,0,0
        while i <len(lefthalf) and j <  len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i+=1
            else:
                alist[k] = righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i,k = i+1,k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            alist[k] = righthalf[j]
            j,k = j+1,k+1

if __name__ == "__main__":
    from  random import randint
    ll = [randint(1,300) for x in range(50)]
    mergesort(ll)
    print(ll)
