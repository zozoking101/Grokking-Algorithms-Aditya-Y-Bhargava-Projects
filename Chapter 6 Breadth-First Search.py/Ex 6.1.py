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

# Example usage
# Construct a linked list representing the shape
node_s = Node("S")
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

node_s.neighbors = [node_a, node_b]
node_a.neighbors = [node_s, node_c, node_d]
node_b.neighbors = [node_s, node_e]
node_c.neighbors = [node_a]
node_d.neighbors = [node_a, node_f]
node_e.neighbors = [node_b]
node_f.neighbors = [node_d]

result = shortest_path_length(node_s, node_f)

if result != -1:
    print(f"The length of the shortest path between S and F is: {result}")
else:
    print("No path found.")