"""
栈 Stack
Python 语言的基本类型 List（列表）实现了栈。
"""

"""
栈的两种基本操作，入栈和出栈
"""

stack_obj = list()

# Push 入栈
stack_obj.append(1)
print("stack: ", stack_obj)

# Pop 出栈
stack_obj.pop()
print("stack: ", stack_obj)