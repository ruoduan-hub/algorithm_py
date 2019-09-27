#  coding=UTF-8
"""
编写涉及数组的递归时，基线条件通常是数组为空或者是只包含一个元素。陷入困境时，请检查基线条件是不是这样的。
"""

def count_down(i):
    print i
    if i <= 1:  # 基线条件 (base case)
        return
    else:  # 递归条件 (recursive csae)
        count_down(i - 1)


count_down(100)
