# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/10/02 上午9:24
describe:利用二分搜索树实现集合
"""
from bst import BinarySearchTree
import chardet
import re
class MySet:
    """
    利用二分搜索树实现集合
    """
    def __init__(self):
        self.bst = BinarySearchTree()
    def add(self,e):
        self.bst.add(e)
    def remove(self,e):
        self.bst.remove(e)
    def contains(self, e):
        return self.bst.contains(e)
    def getsize(self):
        return self.bst.size
    def isEmpty(self):
        return True if self.bst.size == 0 else False


if  __name__ == "__main__":
    myset  = MySet()
    with open("Les Miserables.txt",'r') as f:

        lines = f.readlines()
        for line in lines:
            line = line.decode('EUC-JP')
            #print(line.strip())
            line = line.strip().replace(',',' ').replace(';',' ').replace('"',' ').replace('.',' ').replace('?',' ')
            line = re.sub("['!-]","",line)
            words = line.strip().split(' ')
            for word in words:
                print(str(word).lower())
                myset.add(str(word).lower())
    print(myset.getsize())


        #print(text)



        # for line in txt:
        #     print(line.strip())
        #print("type",type)
        # for line in txt:
        #      print(line)