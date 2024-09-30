import bisect

# Sample sorted list
sorted_list = [1, 3, 4, 4, 7, 8]

# Using bisect_left
position_left = bisect.bisect_left(sorted_list, 4)
print(f"bisect_left: The leftmost position to insert 4 is at index"
      f" {position_left}")  # Output: 2

# Using bisect_right
position_right = bisect.bisect_right(sorted_list, 4)
print(f"bisect_right: The rightmost position to insert 4 is at index"
      f" {position_right}")  # Output: 4

# Using bisect (alias for bisect_right)
position = bisect.bisect(sorted_list, 4)
# Output: 4
print(f"bisect: The rightmost position to insert 4 is at index {position}")

# Inserting using insort_left
bisect.insort_left(sorted_list, 5)
# Output: [1, 3, 4, 4, 5, 7, 8]
print(f"List after insort_left(5): {sorted_list}")

# Inserting using insort_right
bisect.insort_right(sorted_list, 6)
# Output: [1, 3, 4, 4, 5, 6, 7, 8]
print(f"List after insort_right(6): {sorted_list}")

# Bisection is effective for searching ranges of values.
# For locating specific values, dictionaries are more performant.
# The insort() functions are O(n) because the logarithmic search step is
# dominated by the linear time insertion step.
