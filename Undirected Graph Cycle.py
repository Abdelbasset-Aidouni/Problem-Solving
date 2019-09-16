# Given an undirected graph, determine if a cycle exists in the graph

from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.v 		= vertices
		self.graph 	= defaultdict(list)

	def add_edge(self,e1,e2):
		self.graph[e1].append(e2)
		self.graph[e2].append(e1)

	def cycle_until(self,node,visited,parent_node):
		visited[node]	= True
		for v in self.graph[node]:
			if not visited[v]:
				if self.cycle_until(v,visited,node):
					return True
			elif parent_node != v:
				return True
		return False


	def contain_cycle(self):
		visited		= [False]*self.v
		for k in self.graph:
			print(self.graph)
			if not visited[k]:
				if self.cycle_until(k,visited,-1):
					return True
		return False


g = Graph(5) 
g.add_edge(1, 0) 
g.add_edge(0, 2) 
g.add_edge(2, 1)
g.add_edge(0, 3) 
g.add_edge(3, 4)

if g.contain_cycle():
	print(" g contains cycle")
else:
	print(" g doesn't contains cycle")

