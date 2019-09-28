# coding=UTF-8
# 尾递归


def sum_number(arr, total=0):
    """ 递归求和

    :param arr: 数组
    :param total: 总和
    :return: total 总和
    """
    if len(arr) == 0:
        return total

    else:
        total += arr.pop(0)
        return sum_number(arr, total)


aa = sum_number([1, 2, 3])
print(aa)


def count_list(arr, count=0):
    """递归计算包含元素数

    :param arr: 数组
    :param count: 个数
    :return:  count 个数
    """
    if len(arr):
        del arr[0]
        return count_list(arr, count + 1)
    else:
        return count


print(count_list([1, 2]))


def find_max(arr, max=0):
    """  递归查找最大值

    :param arr: 数组
    :param max: 最大值
    :return: max 最大值
    """
    if len(arr):
        if arr[0] > max:
            max = arr[0]
        del arr[0]
        return find_max(arr, max)
    else:
        return max


print(find_max([1, 2, 123, 999, 123, 555, 666]))
