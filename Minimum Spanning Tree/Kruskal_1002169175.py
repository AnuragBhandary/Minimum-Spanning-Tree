import networkx as nx
import random
import time

def kruskal(graph):
    edges = []
    for edge in graph.edges(data=True):
        edges.append((edge[0], edge[1], edge[2]['weight']))

    edges = sorted(edges, key=lambda edge: edge[2])
    mst = nx.Graph()

    for edge in edges:
        try:
            if nx.shortest_path_length(mst, edge[0], edge[1]) > 0:
                continue
        except (nx.NodeNotFound, nx.NetworkXNoPath):
            pass
        mst.add_edge(edge[0], edge[1], weight=edge[2])

    return mst

def generate_random_graph(num_nodes, edge_prob_range=(0.1, 1.0), weight_range=(1, 10)):
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(i)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.uniform(0, 1) < random.uniform(*edge_prob_range):
                weight = random.randint(*weight_range)
                graph.add_edge(i, j, weight=weight)

    return graph

if __name__ == "__main__":
    num_nodes = 5  # Change this to the desired number of nodes
    random.seed(42)  # Set a seed for reproducibility

    # Generate a random graph
    random_graph = generate_random_graph(num_nodes)

    # Measure the runtime of Kruskal's algorithm
    start_time = time.time()
    minimum_spanning_tree = kruskal(random_graph)
    end_time = time.time()
    runtime = end_time - start_time

    # Print the generated graph, minimum spanning tree, and runtime
    print("Random Graph:")
    print(random_graph.edges(data=True))
    print("\nMinimum Spanning Tree:")
    print(minimum_spanning_tree.edges(data=True))
    print("\nRuntime:", runtime, "seconds")

