from collections import deque

class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors else []

def shortest_path_length(start, finish):
    queue = deque([(start, 0)])  # Each element is a tuple (node, path_length)
    visited = set()

    while queue:
        current_node, path_length = queue.popleft()

        if current_node == finish:
            return path_length

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in current_node.neighbors:
                queue.append((neighbor, path_length + 1))

    return -1

# Construct the linked list shaped like a right angle triangle beside a square
node_cab = Node("Cab")
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")
node_i = Node("I")
node_j = Node("J")
node_k = Node("K")
node_bat = Node("Bat")

node_cab.neighbors = [node_a, node_b]
node_a.neighbors = [node_cab, node_c, node_d]
node_b.neighbors = [node_cab, node_d, node_e]
node_c.neighbors = [node_a, node_b, node_f]
node_d.neighbors = [node_a, node_b, node_f, node_g]
node_e.neighbors = [node_b, node_g, node_h]
node_f.neighbors = [node_c, node_d, node_h, node_i]
node_g.neighbors = [node_d, node_e, node_i, node_j]
node_h.neighbors = [node_e, node_f, node_j, node_k]
node_i.neighbors = [node_f, node_g, node_k, node_bat]
node_j.neighbors = [node_g, node_h, node_k]
node_k.neighbors = [node_h, node_i, node_j, node_bat]
node_bat.neighbors = [node_i, node_k]

# Find the shortest path length between Cab and Bat
result = shortest_path_length(node_cab, node_bat)

if result != -1:
    print(f"The shortest path length between Cab and Bat is: {result}")
else:
    print("No path found.")