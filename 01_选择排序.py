#  coding=UTF-8

""" O(n2)
每次从原始列表中拿找到最（大/小）的值返回 index ， 用index 找到这个值 pop 用 index 删除，用返回的值添加到一个新数组中

"""


def find_min (arr):
    min = arr[0]  # 储存最小的值
    min_index = 0  # 储存最小值的索引
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i

    return min_index


def select_sort(arr):  # 对数组进行排序
    new_arr = []
    for i in range(len(arr)):
        min_nub = find_min(arr)  # 找出数组中最小的元素 将其加入到新数组中
        new_arr.append(arr.pop(min_nub))
    return new_arr


print(select_sort([1, 99, 123, 5, 6, 8]))
