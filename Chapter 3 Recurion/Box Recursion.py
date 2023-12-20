# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not None:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")

            
class Item:
    def __init__(self, name):
        self.name = name

    def is_a_box(self):
        return isinstance(self, Box)

    def is_a_key(self):
        return self.name == "key"

class Box(Item):
    def __init__(self, name, items=None):
        super().__init__(name)
        self.items = items if items is not None else []

# Function to look for the key in boxes
def look_for_key(box):
    for item in box.items:
        if item.is_a_box():
            print(f"Not a key: {item.name}")
            look_for_key(item)  # Recursion!
        elif item.is_a_key():
            print("Found the key!")

# Example usage
box1 = Box("box1", [Item("book"), Item("pen"), Box("box2", [Item("apple"), Item("key")])])
box2 = Box("box3", [Item("notebook"), Box("box4", [Item("umbrella"), Item("key")])])
main_box = Box("main_box", [box1, box2])

# Look for the key in the main box
look_for_key(main_box)
