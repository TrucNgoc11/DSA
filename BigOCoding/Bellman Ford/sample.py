import queue

def topological_sort(graph, indegree, ordering):
    zero_indegree = queue.Queue()

    for u in range(26):
        if indegree[u] == 0:
            zero_indegree.put(u)

    while zero_indegree.qsize():
        u = zero_indegree.get()
        ordering.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)

    for u in range(26):
        if indegree[u] != 0:
            return False

    return True

names = []
n = int(input())
for _ in range(n):
    names.append(input())

indegree = [0] * 26
graph = [[] for _ in range(26)]
shorter_comes_first = True

for i in range(n - 1):
    name_1, name_2 = names[i], names[i + 1]
    is_prefix = True

    for j in range(min(len(name_1), len(name_2))):
        u = ord(name_1[j]) - ord('a')
        v = ord(name_2[j]) - ord('a')
        if u != v:
            graph[u].append(v)
            indegree[v] += 1
            is_prefix = False
            break

    if is_prefix and len(name_1) > len(name_2):
        shorter_comes_first = False
        break

ordering = []
if shorter_comes_first and topological_sort(graph, indegree, ordering):
    for character_ascii in ordering:
        print(chr(character_ascii + ord('a')), end='')
    print()
else:
    print('Impossible')