# 表示图的字典
graph = {
    # 起点到达邻居的权
    'start': {
        'a': 6,
        'b': 2,
    },
    # a点到达邻居的权
    'a': {
        'fin': 1
    },
    # b点到达邻居的权
    'b': {
        'a': 3,
        'fin': 5
    },
    # 终点没有邻居
    'fin': {}
}

# 储存父节点的字典
parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

# 处理过的节点
processed = []

