# #T074 Krishna Ai Pract 2 Recursive Best-First Search (RBFS)

import matplotlib.pyplot as plt

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

coords = {
    'MVLU College': (1, 8),
    'Ghatkopar': (3, 7),
    'Chembur': (2, 5),
    'Thane': (5, 9),
    'Vashi': (4, 5),
    'Taloja': (7, 4),
    'Panvel': (6, 1)
}

def rbfs_search(start, goal):
    success, path, cost, _ = rbfs(start, goal, g=0, f_limit=float('inf'), path=[start])
    return path, cost

def rbfs(node, goal, g, f_limit, path):
    if node == goal:
        return True, path, g, g

    neighbors = graph[node]
    if not neighbors:
        return False, [], 0, float('inf')

    successors = []
    for neighbor, distance in neighbors.items():
        if neighbor not in path:
            next_g = g + distance
            next_f = max(next_g + heuristics[neighbor], g + heuristics[node])
            successors.append([next_f, neighbor, next_g])

    if not successors:
        return False, [], 0, float('inf')

    while True:
        successors.sort(key=lambda x: x[0])
        best = successors[0]

        if best[0] > f_limit:
            return False, [], 0, best[0]

        alternative_f = successors[1][0] if len(successors) > 1 else float('inf')

        success, result_path, total_g, returned_f = rbfs(
            best[1], goal, best[2], min(f_limit, alternative_f), path + [best[1]]
        )

        best[0] = returned_f

        if success:
            return True, result_path, total_g, returned_f

path, total_dist = rbfs_search('MVLU College', 'Panvel')

print(f"--- Execution Output for T074 Krishna ---")
print(f"Optimal RBFS Path: {' -> '.join(path)} ({total_dist} km)")
print(f"----------------------------------------")

plt.figure(figsize=(10, 8))

for node, neighbors in graph.items():
    x1, y1 = coords[node]
    for neighbor, dist in neighbors.items():
        x2, y2 = coords[neighbor]
        is_path = node in path and neighbor in path and path.index(neighbor) == path.index(node) + 1
        color, width = ('#2ecc71', 3) if is_path else ('#bdc3c7', 1.5)
        
        plt.plot([x1, x2], [y1, y2], color=color, linewidth=width, zorder=1)
        plt.text((x1+x2)/2, (y1+y2)/2, f"{dist}km", color='red', fontsize=9, ha='center')

for node, (x, y) in coords.items():
    color = '#f1c40f' if node in path else '#3498db'
    plt.scatter(x, y, color=color, s=900, zorder=2)
    plt.text(x, y, f"{node}\nh={heuristics[node]}", ha='center', va='center', color='white', fontsize=8, fontweight='bold')

plt.title(f"RBFS Complete Grid Network Map (Total: {total_dist}km)\nStudent: T074 Krishna", fontsize=12, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
