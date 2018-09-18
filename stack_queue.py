
__author__ = 'xl'
"""
__date__ = TIME： 2018/09/18 上午12:58
describe: 两个栈完成一个队列
"""

class Stack_To_Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,value):
        self.stack1.append(value)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

if __name__ == "__main__":
    P = Stack_To_Queue()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())