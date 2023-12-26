# Name - Anurag Bhandary
# UTA ID - 1002169175

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import numpy as np


class MSTComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MST Algorithm Comparison - 1002169175")
        self.root.geometry("800x600")

        self.graph_frame = ttk.Frame(root)
        self.graph_frame.pack(pady=10)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        self.create_graph_button = ttk.Button(self.button_frame, text="Generate Random Graph", command=self.generate_random_graph)
        self.create_graph_button.grid(row=0, column=0, padx=10)

        self.compare_button = ttk.Button(self.button_frame, text="Compare Algorithms", command=self.compare_algorithms)
        self.compare_button.grid(row=0, column=1, padx=10)

        self.result_label = ttk.Label(self.graph_frame, text="")
        self.result_label.pack(pady=10)

    def generate_random_graph(self):
        self.num_vertices = simpledialog.askinteger("Input", "Enter the number of vertices (maximum 6):", parent=self.root, minvalue=2)
        self.num_edges = simpledialog.askinteger("Input", "Enter the number of edges (maximum 8):", parent=self.root, minvalue=1)

        self.graph = nx.gnm_random_graph(self.num_vertices, self.num_edges, seed=42)

        for edge in self.graph.edges(data=True):
            edge[2]['weight'] = np.random.randint(1, 10)

        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', ax=plt.gca())
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in self.graph.edges(data=True)})
        plt.title("Random Graph with Edge Weights")
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def compare_algorithms(self):
        if hasattr(self, 'graph'):
            kruskal_start_time = time.time()
            kruskal_mst, kruskal_weight = self.kruskal_algorithm()
            kruskal_end_time = time.time()
            kruskal_runtime = kruskal_end_time - kruskal_start_time

            prim_start_time = time.time()
            prim_mst, prim_weight = self.prim_algorithm()
            prim_end_time = time.time()
            prim_runtime = prim_end_time - prim_start_time

            result_str = f"Kruskal MST: {kruskal_mst}\nKruskal MST Weight: {kruskal_weight}\n"
            result_str += f"Prim MST: {prim_mst}\nPrim MST Weight: {prim_weight}\n\n"
            result_str += f"Kruskal Runtime: {self.format_runtime(kruskal_runtime)}\n"
            result_str += f"Prim Runtime: {self.format_runtime(prim_runtime)}"

            self.result_label.config(text=result_str)
        else:
            messagebox.showwarning("Warning", "Please generate a random graph first.")

    def kruskal_algorithm(self):
        kruskal_edges = list(nx.minimum_spanning_edges(self.graph, algorithm='kruskal', data=True))
        kruskal_weight = sum(d['weight'] for u, v, d in kruskal_edges)
        return kruskal_edges, kruskal_weight

    def prim_algorithm(self):
        prim_edges = list(nx.minimum_spanning_edges(self.graph, algorithm='prim', data=True))
        prim_weight = sum(d['weight'] for u, v, d in prim_edges)
        return prim_edges, prim_weight

    def format_runtime(self, runtime):
        if runtime < 1e-6:
            return f"{runtime * 1e6:.5f} micro seconds"
        else:
            return f"{runtime:.6f} seconds"

if __name__ == "__main__":
    root = tk.Tk()
    app = MSTComparisonApp(root)
    root.mainloop()
