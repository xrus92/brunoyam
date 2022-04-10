graph = {'0': ['1', '2'],
'1': ['0', '3', '4'],
'2': ['0'],
'3': ['1'],
'4': ['2', '3']}

q = []
def bfs(graph, start, visited=[]):
	visited.append(start)
	global q
	q.append(start)
	while q:
		curr = q.pop(0)
		print(curr, end=' ')
		for v in graph[curr]:
			if v not in visited:
				visited.append(v)
				q.append(v)

bfs(graph, '3')