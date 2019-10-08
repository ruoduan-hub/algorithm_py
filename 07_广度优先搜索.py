from collections import deque
# 实现数据结构
# 散列表储存所有数组
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def search(name):
    """

    :param name: 要搜索的人
    :return: bool
    """
    search_queue = deque()  # 创建一个队列
    search_queue += graph['you']
    searched = []  # 存放搜索过的人

    while search_queue:  # 不为空
        person = search_queue.popleft()  # 取出第一个人
        if person_is(person):
            print('%s 找到了 ！' % person)
            return True
        else:
            search_queue += graph[person]  # 没找到吧这个人递归继续查找
            searched.append(person)  # 这个人标记为检查过了

    return False


def person_is(name):
    return name == 'jonny'


p = search('you')
if not p:
    print('查无此人')
