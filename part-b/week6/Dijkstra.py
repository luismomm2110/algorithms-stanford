from WeightedGraph import WeightedGraph

def fill_graph(textFile, graph):
	f = open(textFile, "r")
	lines = f.readlines()

	for line in lines:
		line = line.split("\t")
		for edge in line[-1]:
			print(edge.split(","))


def main():
	g = WeightedGraph()

	fill_graph("graph.txt", g)

if __name__ == "__main__": 
	main()