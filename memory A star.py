import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}
heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 3,
    'E': 4, 'F': 4, 'G': 0
}
MEMORY_LIMIT = 4 # Simulated memory limit
def sma_star(start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], 0, start, [start])) # (f, g, node, path)
    while frontier:
        frontier.sort() # Keep the queue sorted by f(n)
        if len(frontier) > MEMORY_LIMIT:
            removed = frontier.pop() # Remove worst node
            print(f"Removed due to memory limit: {removed[2]}")
        f, g, node, path = heapq.heappop(frontier)
        if node == goal:
            return path
        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))
    return None
path = sma_star('A', 'G')
print("Path found:", path)