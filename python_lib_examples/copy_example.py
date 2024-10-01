if __name__ == '__main__':
    import copy

    # Original nested list
    original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Shallow copy using copy.copy()
    shallow_copy = copy.copy(original_list)

    # Deep copy using copy.deepcopy()
    deep_copy = copy.deepcopy(original_list)

    # Modify the original list
    original_list[0][0] = 99

    # Display the lists
    print("Original List:", original_list)
    print("Shallow Copy: ", shallow_copy)
    print("Deep Copy:    ", deep_copy)

    # Original List: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Shallow Copy:  [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Deep Copy:     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
