# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/10/01 下午5:16
describe: 二分搜索树 实现二分搜索树的增加、删除（最大、最小、任意节点）,
    前序、中、后序递归方式遍历二分搜索树
    前序非递归方式遍历二分搜索树
    层序遍历二分搜索树
    查找二分搜索树的最大值 最小值
    此二分搜索树满足性质 任意节点左子树总比 该节点小 右子树总比该节点大 
    此二叉树不可包含重复元素
"""
from random import randint
from Queue import Queue



class Node:
    def __init__(self,e):
        self.left = None
        self.right = None
        self.e = e

    def __lt__(self, other):
        return True  if self.e < other else False

    def __gt__(self,other):
        return True  if self.e > other else False

    def __le__(self,other):
        return True if self.e <= other else False

    def __ge__(self, other):
        return True if self.e >= other else False
    def __eq__(self, other):
        return True if self.e == other else False

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self,e):
        self.root = self.add_child(self.root,e)
    #以node为根的二分搜索树插入 元素e
    #返回插入节点后 新的二分搜索树的根
    def add_child(self,node,e):
        if node == None:
            self.size += 1
            return Node(e)
        if node > e:
            node.left = self.add_child(node.left,e)
        elif node < e:
            node.right = self.add_child(node.right,e)
        return node


    def _contains(self,node,e):
        if node.e == None:
            return False
        elif node == e:
            return True
        if node > e:
            return  self.contains(node.left,e)
        elif node < e:
            return self.contains(node.right,e)

    def contains(self,e):
        return self._contains(self.root,e)
    #前序 中序 后序 按照值 被访问顺序
    #前序 递归写法第一次就访问
    #中序 递归写法第二次就访问
    #后序 递归写法第三次就访问
    #三种遍历 都属于深度优先遍历


    def preOrder(self):
        """
        前序遍历递归写法  中 左 右
        :return:
        """
        self._preOrder(self.root)
    def _preOrder(self,node):
        if node == None:
            return
        print(node.e)
        self._preOrder(node.left)
        self._preOrder(node.right)


    def preOrderNR(self):
        """
        前序遍历 非递归写法 No recursion 运用栈技术
        :return:
        """
        stack = []
        stack.append(self.root)
        while len(stack):
            cur = stack.pop()
            print(cur.e)
            if cur.right  != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)




    def inOrder(self):
        """
        中序遍历递归写法  左 中 右
        :return:
        """
        self._inOrder(self.root)
    def _inOrder(self,node):
        if node == None:
            return
        self._inOrder(node.left)
        print(node.e)
        self._inOrder(node.right)

    def postOrder(self):
        """
        后序遍历递归写法 左 右 中
        :return:
        """
        self._postOrder(self.root)
    def _postOrder(self,node):
        if node == None:
            return
        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.e)


    def levelOrder(self):
        """
        二分搜索树的层序遍历      属于 广度优先遍历
        :return:
        """
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            cur = queue.get()
            print(cur.e)
            if cur.left != None:
                queue.put(cur.left)
            if cur.right != None:
                queue.put(cur.right)

    def minimum(self):
        """
        查找二分搜索树最小值
        :return:
        """
        if self.size == 0:
            raise  ValueError(r'Binary Search Tree is Empty')
        return self._minium(self.root).e
    def _minium(self,node):
        """
        返回以node为根节点,二分搜索树最小值节点
        :param node:
        :return:
        """
        if node.left == None:
            return node
        return self._minium(node.left)

    def maximum(self):
        """
        查找二分搜索树最小值
        :return:
        """
        if self.size == 0:
            raise  ValueError(r'Binary Search Tree is Empty')
        return self._maxium(self.root).e
    def _maxium(self,node):
        """
        返回以node为根节点,二分搜索树最大值节点
        :param node:
        :return:
        """
        if node.right == None:
            return node
        return self._maxium(node.right)

    def removeMin(self):
        """
        返回当前二分搜索树最小值
        :return:
        """
        min_v = self.minimum()
        self.root = self._removeMin(self.root)
        return min_v

    def _removeMin(self,node):
        """
        删除掉以node为根的二分搜索树的最小节点
        :return: 返回删除节点后 新的二分搜索树根
        """
        if node.left == None:
            right_node = node.right
            node.right = None
            self.size -=1
            return right_node
        node.left =self._removeMin(node.left)
        return node
    def removeMax(self):
        """
        返回当前二分搜索树最大值
        :return:
        """
        max_v = self.maximum()
        self.root = self._removeMax(self.root)
        return max_v
    def _removeMax(self,node):
        """
        删除掉以node为根的二分搜索树的最小节点
        :return: 返回删除节点后 新的二分搜索树根
        """
        if node.right == None:
            left_node = node.left
            node.right = None
            self.size -=1
            return left_node
        node.right = self._removeMax(node.right)
        return node
    #二分搜索树中删除 元素e
    def remove(self,e):
        self.root = self._remove(self.root,e)

    #删除以node为根的树中元素e
    #返回删除节点后 新的二分搜索树根
    def _remove(self,node,e):
        if node == None:
            return None
        if node > e:
            node.left =  self._remove(node.left,e)
        elif node < e:
            node.right = self._remove(node.right,e)
        else: #相等
            if node.left == None:
                right_node = node.right
                node.right = None
                self.size -= 1
                return right_node
            if node.right == None:
                left_node = node.left
                node.right = None
                self.size -= 1
                return left_node

            # 左右子树都不为空 取右子树的最小值节点 覆盖 要删除的节点
            # 也可以取 左子树的最大值覆盖
            else:
                successor = self._minium(node.right)
                successor.right = self._removeMin(node.right)
                successor.left = node.left
                node.left = node.right = None
                return successor





if __name__ == "__main__":

   #        28
   #    16      32
   #  13  22  29   42

    ll = [randint(1,2200) for x in range(200)]
    #ll = [28,16,13,32,22,42,29]
    print(ll)
    bst = BinarySearchTree()
    for x in ll:
        bst.add(x)
    #bst.preOrderNR()
    #bst.preOrder()
    # print(bst.maximum())
    while bst.size:
        print(bst.removeMin())


    

