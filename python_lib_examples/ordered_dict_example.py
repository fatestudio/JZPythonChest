if __name__ == '__main__':
    from collections import OrderedDict

    # Create an OrderedDict
    ordered_dict = OrderedDict()

    # Adding items to the OrderedDict
    ordered_dict["apple"] = 1
    ordered_dict["banana"] = 2
    ordered_dict["orange"] = 3
    ordered_dict["grape"] = 4

    # Display the OrderedDict
    print("OrderedDict contents:")
    for key, value in ordered_dict.items():
        print(f"{key}: {value}")

    # Modify an item
    ordered_dict["banana"] = 5

    # Check if the order is maintained
    print("\nAfter modifying 'banana':")
    for key, value in ordered_dict.items():
        print(f"{key}: {value}")

    # Moving an item to the end
    ordered_dict.move_to_end("apple")

    print("\nAfter moving 'apple' to the end:")
    for key, value in ordered_dict.items():
        print(f"{key}: {value}")

    # Popping the last item
    ordered_dict.popitem()

    print("\nAfter popping the last item:")
    for key, value in ordered_dict.items():
        print(f"{key}: {value}")
