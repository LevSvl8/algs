def find_lowest_cost(costs):
    min =  float("inf")
    min_node = None
    for node in costs:
        cur_cost = costs[node]
        if min > cur_cost and node not in processed:
            min = cur_cost
            min_node = node
    return min_node




if __name__ == '__main__':
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["end"] = 5

    graph["a"] = {}
    graph["a"]["end"] = 1
    graph["end"] = {}

    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["end"] = float("inf")

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["end"] = None

    processed = []

    node = find_lowest_cost(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost(costs)

    print costs
