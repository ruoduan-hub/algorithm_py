# coding=UTF-8
def quicksort(arr):
    """ 快速排序算法

    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        print arr
        return quicksort(less) + [pivot] + quicksort(greater)


print quicksort([10, 5, 2, 3, 99])


"""推导 归纳证明
99 10 5 2 3 11  17

5 2 3 [10] 99 11 17

2 3  [5] [] |  11 17 [99] []

拼接： 2 3 5 11 17 99

"""

"""
归纳证明是一种证明算法行之有效的的方式， 它分2步：基线条件和归纳条件。

例如：爬梯子
归纳条件：
    如果我站在一个横档上，我能就将脚放到上一个横档上。换言之 如果我站在2、3、4 ... 我就能爬上3 ... 。

基线条件：
    我已经站在第一个横档上，因此我每次怕一个横档，我就能到梯子的最顶端
"""
