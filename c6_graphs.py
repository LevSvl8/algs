from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

def find_mango_seller(graph):
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print person + ' is a mango seller!'
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    graph = {}
    graph['you'] = ['bob','clar','alice']
    graph['clar'] = ['tom','johny']
    graph['alice'] = ['peggi']
    graph['bob'] = ['aunge','peggi']
    graph['johny'] = []
    graph['tom'] = []
    graph['aunge'] = []
    graph['peggi'] = []

    find_mango_seller(graph)

