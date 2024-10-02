import multiprocessing


# Function to modify the shared data in a process
def update_shared_data(shared_array, shared_value):
    for i in range(len(shared_array)):
        shared_array[i] += 1  # Increment each element in the shared array
    shared_value.value += 5  # Increment the shared value


if __name__ == "__main__":
    # Create a shared array and shared value
    shared_array = multiprocessing.Array('i',
                                         [1, 2, 3, 4])  # 'i' means integers
    shared_value = multiprocessing.Value('i', 10)  # Shared integer value

    # Print initial values
    print(f"Initial array: {shared_array[:]}")
    print(f"Initial value: {shared_value.value}")

    # Create two processes that modify the shared data
    p1 = multiprocessing.Process(target=update_shared_data,
                                 args=(shared_array, shared_value))
    p2 = multiprocessing.Process(target=update_shared_data,
                                 args=(shared_array, shared_value))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    # Print the modified shared data
    print(f"Modified array: {shared_array[:]}")
    print(f"Modified value: {shared_value.value}")
