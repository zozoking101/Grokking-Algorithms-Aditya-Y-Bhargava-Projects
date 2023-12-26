class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

class HashTable:
    def __init__(self):
        # Initialize an array of linked lists
        self.table = [LinkedList() for _ in range(26)]

    def hash_function(self, key):
        # Use the ASCII value of the first character to determine the slot
        return ord(key[0]) - ord('a')

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].insert(key, value)

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index].search(key)

# Example usage
book = HashTable()
book.insert("apple", 0.67)
book.insert("milk", 1.49)
book.insert("avocado", 1.49)

# Search for items
print("Price of apple:", book.search("apple"))
print("Price of milk:", book.search("milk"))
print("Price of avocado:", book.search("avocado"))
