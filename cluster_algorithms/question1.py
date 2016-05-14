"""
implementation of the clustering algorithm for computing a max-spacing k-clustering.
run the clustering algorithm and the target number k of culsters is set to 4.
what is the maximum spacing of a 4-clustering?
"""

from kruskal import Weighted_graph

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
graph = Weighted_graph(edges, weights)
graph.kruskal()


