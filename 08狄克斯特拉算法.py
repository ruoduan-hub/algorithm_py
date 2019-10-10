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

costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf')
}

# 储存父节点的字典
parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

# 处理过的节点
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # 如果当前节点开销更低且为处理过
            lowest_cost = cost  # 将其视为开销最低的节点
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra():
    node = find_lowest_cost_node(costs)  # 在末梢的节点找出开销最小的节点

    while node is not None:  # 所有节点被处理过后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # 遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # 如果经当前节点前往该节点邻居更近，
                costs[n] = new_cost  # 就更新该邻居的开销
                parents[n] = node  # 同时将该领奖的父节点设置为当前节点

        processed.append(node)  # 将当前节点标记为处理过
        node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点并循环


dijkstra()

print(costs)

print(parents)

print(processed)
