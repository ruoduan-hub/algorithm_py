#  coding=UTF-8


def greet(name):
    print('hello' + name)
    greet2(name)
    print('say bye')
    bye(name)


def greet2(name):
    print('2')


def bye(name):
    print('886' + name)


greet('小明')


# 递归调用栈
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))


# 尾递归
def tail_recursion(n, total=0):
     if n == 0:
         return total
     else:
         return tail_recursion(n-1,  total+n)


print(tail_recursion(10))
