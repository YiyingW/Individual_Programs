

class Weighted_graph:
	"""
	Implement a weighted graph with a 2d list and a corresponding weight list
	Vertices are represented by elements (eg. 1,2,3) in the graph list and edges are represented by a list collection of
	each 2 vertices (eg. [1,2])
	"""

	edges = []
	weight = []
	vertices = []

	def __init__(self, edge_list, weight):
		self.edges = edge_list
		self.weight = weight

	def add(self, edge_list, weight):
		"""
		add an edge (defined by 2 vertices in a list) and its corresponding weight to edges
		"""
		self.edges.append(edge_list)
		self.weight.append(weight)

	def print_graph(self):
		"""
		print each set of edges in a graph and its corresponding edges
		"""
		print self.edges
		print self.weight
		print self.vertices

	def __sort(self):
		"""
		sorts both edges and weight lists in nondecreasing order of weight list elements
		"""
		if len(self.edges) != len(self.weight):
			return
		for i in range(1, len(self.weight)):
			print i
			temp_weight = self.weight[i]
			temp_edge = self.edges[i]
			current = i - 1
			while current >= 0 and temp_weight < self.weight[current]:
				self.weight[current+1] = self.weight[current]
				self.edges[current+1] = self.edges[current]
				current -= 1
			self.weight[current+1] = temp_weight 
			self.edges[current+1] = temp_edge


	def __makeset(self):
		"""
		initialize each vertex to its own component
		"""
		for i in range(len(self.edges)):
			for j in range(len(self.edges[i])):
				if self.edges[i][j] not in self.vertices:
					self.vertices.append(self.edges[i][j])

		for k in range(len(self.vertices)):
			self.vertices[k] = [self.vertices[k]]

	def __findset(self, vertex):
		"""
		find and return the index to which vertex belongs in vertices list
		"""
		for i in range(len(self.vertices)):
			for element in self.vertices[i]:
				if element == vertex:
					return i
		return None 

	def __union(self, vertex1, vertex2):
		"""
		join 2 vertex together
		"""
		index1 = self.__findset(vertex1)
		index2 = self.__findset(vertex2)
		for element in self.vertices[index2]:
			self.vertices[index1].append(element)
		self.vertices.pop(index2)


	def kruskal(self):
		self.__sort()
		print "sorting is done"
		self.__makeset()
		print "set is initiated"
		count, i = 0, 0
		while len(self.vertices) > 1:
			if self.__findset(self.edges[i][0])!= self.__findset(self.edges[i][1]):
				print "(%d %d) edge selected." % (self.edges[i][0], self.edges[i][1])
				count += 1
				self.__union(self.edges[i][0], self.edges[i][1])
			i += 1
			print i

"""
edges = [[3, 4], [1, 3], [5, 6], [1, 5], [3, 6], [1, 2], [2, 4], [3, 5], [4, 6]]
weight = [4,2,3,5,1,6,3,6,2]

graph1 = Weighted_graph(edges, weight)
graph1.print_graph()
graph1.kruskal()
graph1.print_graph()
"""

edges = []
weights = []
text_file = open("file1.txt", "r")
lines = text_file.readlines()
for nline in range(1, len(lines)):
	edge_weight_list = lines[nline].rstrip().split(" ")
	edge = [int(edge_weight_list[0]), int(edge_weight_list[1])]
	weight = int(edge_weight_list[2])
	edges.append(edge)
	weights.append(weight)
print "reading data is done"
graph = Weighted_graph(edges, weights)
print "graph is created"
graph.kruskal()












