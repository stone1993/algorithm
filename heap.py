# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/09/16 下午9:46
describe:
"""
from random import randint
#构建最小堆
class HeapSort:
    def __init__(self):
        self.heap_list =[0]
        self.currentsize = 0

    def purUp(self,index):
        while index //2 >0:
            if self.heap_list[index] < self.heap_list[index//2]:
                self.heap_list[index],self.heap_list[index//2] = self.heap_list[index//2],self.heap_list[index]
                index = index//2
            else:
                break

    def insert(self,value):
        self.heap_list.append(value)
        self.currentsize +=1
        self.purUp(self.currentsize)

    def delMin(self):
        res_val = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.currentsize]
        self.currentsize -= 1
        self.purDown(1)
        self.heap_list.pop()
        return res_val

    def purDown(self,index):
        while index*2 <self.currentsize:
            min_child = self.getMinChild(index)
            if self.heap_list[min_child] < self.heap_list[index]:
                self.heap_list[min_child],self.heap_list[index] = self.heap_list[index],self.heap_list[min_child]
                index = min_child
            else:
                break

    def isEmpty(self):
        return self.currentsize == 0


    def getMinChild(self,index):
        if index *2 +1 > self.currentsize:
            return index*2
        else:
            if self.heap_list[index*2] < self.heap_list[index*2+1]:
                return index*2
            else:
                return index*2+1

    def buildHeap(self,alist):
        index = len(alist)//2
        self.currentsize = index
        self.heap_list = [0]+ alist[:]
        while (index >0):
            self.purDown(index)
            index-=1
        return self.heap_list



if __name__ == "__main__":

        ll = [randint(1,500) for x in range(100)]
        heap = HeapSort()
        for temp in ll:
            heap.insert(temp)

        while not heap.isEmpty():
            print(heap.delMin())
