import networkx as nx
import random
import time
import math

def prim(graph):
    mst = nx.Graph()
    
    if not graph.nodes():
        return mst
    
    start_node = random.choice(list(graph.nodes()))
    mst.add_node(start_node)
    
    while len(mst) < len(graph):
        edges_with_weights = [(edge[0], edge[1], edge[2]['weight']) for edge in graph.edges(data=True)]
        
        if not edges_with_weights:
            break  # No more edges to add
        
        edge = min(edges_with_weights, key=lambda e: e[2])
        
        if edge[0] in mst.nodes() and edge[1] not in mst.nodes():
            mst.add_node(edge[1])
            mst.add_edge(edge[0], edge[1], weight=edge[2])
        elif edge[1] in mst.nodes() and edge[0] not in mst.nodes():
            mst.add_node(edge[0])
            mst.add_edge(edge[0], edge[1], weight=edge[2])
        
        graph.remove_edge(edge[0], edge[1])
    
    return mst

def generate_random_graph(num_nodes, edge_prob_range=(0.1, 1.0), weight_range=(1, 10)):
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(i)
    num_edges = (num_nodes/2)*(num_nodes-1)
    num_edges = math.floor(num_edges)
    for i in range(num_edges):
        for j in range(i + 1, num_nodes):
            if random.uniform(0, 1) < random.uniform(*edge_prob_range):
                weight = random.randint(*weight_range)
                graph.add_edge(i, j, weight=weight)
    
    print("\nRandom Graph:")
    print(f"Edges: {list(graph.edges(data=True))} For {num_nodes} nodes")
    return graph

if __name__ == "__main__":
    num_nodes = 5  # Change this to the desired number of nodes
    # random.seed(42)  # Set a seed for reproducibility

    # Generate a random graph
    random_graph = generate_random_graph(num_nodes)

    # Measure the runtime of Prim's algorithm
    start_time = time.time()
    minimum_spanning_tree = prim(random_graph)
    end_time = time.time()
    runtime = end_time - start_time

    # Print the generated graph, minimum spanning tree, and runtime
    print("\nMinimum Spanning Tree (Prim's Algorithm):")
    print(minimum_spanning_tree.edges(data=True))
    print("\nRuntime:", runtime, "seconds")
