"""
队列 Queue
在 Python 的标准库中，有两个类实现了队列

第一个是 Queue 类，这是一个同步实现，意味着多个进程可以同时访问同一个
对象。（并发用）
第二个是 Deque 类，（Double Ended Queue 双向队列）
"""

import queue


class OurQueue(object):
    """
    用两个栈实现基本队列
    """
    def __init__(self):
        self.in_stack = []         # 队列的尾部
        self.out_stack = []        # 队列的头部

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:     # 队列头为空
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()