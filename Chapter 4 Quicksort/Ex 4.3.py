def recursive_max(arr):
    """
    Find the maximum number in a list using recursion.

    Parameters:
    - arr: The list of numbers.

    Returns:
    - The maximum number in the list.
    """
    # Base case: if the list is empty, return None
    if not arr:
        return None
    # Recursive case: compare the first element with the maximum in the rest of the list
    else:
        rest_max = recursive_max(arr[1:])
        if rest_max is None or arr[0] > rest_max:
            return arr[0]
        else:
            return rest_max

# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = recursive_max(my_list)
print("Maximum number in the list:", result)
