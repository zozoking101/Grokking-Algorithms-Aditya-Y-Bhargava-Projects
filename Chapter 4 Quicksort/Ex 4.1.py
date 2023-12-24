def recursive_sum(arr):
    """
    Calculate the sum of elements in a list using recursion.

    Parameters:
    - arr: The list of numbers.

    Returns:
    - The sum of elements in the list.
    """
    # Base case: if the list is empty, return 0
    if not arr:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the list
    else:
        return arr[0] + recursive_sum(arr[1:])

# Example usage
my_list = [1, 2, 3, 4, 5]
result = recursive_sum(my_list)
print("Sum of the list is:", result)
