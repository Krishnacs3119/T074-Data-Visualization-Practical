#T074 Krishna Ai Pract 2 A* Search 

import heapq
import matplotlib.pyplot as plt
import networkx as nx

graph = {
    'MVLU College': {'Chembur': 15, 'Ghatkopar': 10},
    'Ghatkopar': {'Thane': 14, 'Chembur': 6}, 
    'Chembur': {'Vashi': 12},
    'Thane': {'Taloja': 13},
    'Vashi': {'Panvel': 18},
    'Taloja': {'Panvel': 9},
    'Panvel': {}
}

heuristics = {
    'MVLU College': 35,
    'Ghatkopar': 30,
    'Chembur': 26,
    'Thane': 20,
    'Vashi': 16,
    'Taloja': 8,
    'Panvel': 0
}

node_positions = {
    'MVLU College': (1, 8),
    'Ghatkopar': (3, 7),
    'Chembur': (2, 5),
    'Thane': (5, 9),
    'Vashi': (4, 5),
    'Taloja': (7, 4),
    'Panvel': (6, 1)
}

def a_star_search(graph, heuristics, start, goal):
    priority_queue = [(heuristics[start], start, [start], 0)]
    visited = set()

    while priority_queue:
        f_score, current, path, g_score = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, g_score

        for neighbor, edge_weight in graph[current].items():
            if neighbor not in visited:
                next_g = g_score + edge_weight
                next_f = next_g + heuristics[neighbor]
                heapq.heappush(priority_queue, (next_f, neighbor, path + [neighbor], next_g))

    return None, float('inf')

optimal_path, total_distance = a_star_search(graph, heuristics, 'MVLU College', 'Panvel')

print(f"--- Execution Output for T074 Krishna ---")
print("Optimal Path Discovered:")
print(" -> ".join(optimal_path))
print(f"Total Road Distance: {total_distance} km")
print(f"----------------------------------------")

G = nx.DiGraph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

plt.figure(figsize=(11, 8))
path_edges = list(zip(optimal_path, optimal_path[1:]))
normal_edges = [edge for edge in G.edges() if edge not in path_edges]

nx.draw_networkx_nodes(G, node_positions, node_size=2800, node_color="lightblue")
nx.draw_networkx_edges(G, node_positions, edgelist=normal_edges, width=1.5, edge_color="gray", arrows=True)
nx.draw_networkx_edges(G, node_positions, edgelist=path_edges, width=3.5, edge_color="darkorange", arrows=True)

node_labels = {node: f"{node}\nh(n) = {heuristics[node]}" for node in G.nodes()}
nx.draw_networkx_labels(G, node_positions, labels=node_labels, font_size=9, font_weight="bold")

edge_labels = nx.get_edge_attributes(G, "weight")
formatted_edge_labels = {edge: f"{weight} km" for edge, weight in edge_labels.items()}
nx.draw_networkx_edge_labels(G, node_positions, edge_labels=formatted_edge_labels, font_color="red")

plt.title("A* Complete Grid Network Map\nStudent: T074 Krishna | Orange Path = Evaluated Shortest Route", fontsize=13, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.show()
