def recursive_count(arr):
    """
    Count the number of items in a list using recursion.

    Parameters:
    - arr: The list.

    Returns:
    - The number of items in the list.
    """
    # Base case: if the list is empty, return 0
    if not arr:
        return 0
    # Recursive case: count 1 for the current item and the count in the rest of the list
    else:
        return 1 + recursive_count(arr[1:])

# Example usage
my_list = [1, 2, 3, 4, 5]
result = recursive_count(my_list)
print("Number of items in the list:", result)
