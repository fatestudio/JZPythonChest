import multiprocessing
import time


def check_if_main_process():
    current_process = multiprocessing.current_process()
    if current_process.name == 'MainProcess':
        print("This is the main process.")
    else:
        print(f"This is a subprocess. Process name: {current_process.name}")


def my_function2():
    check_if_main_process()
    for i in range(10):
        print(f"Daemon process 2 is running: iteration {i}")
        time.sleep(1)  # Simulate work with sleep


# Define the function to be run as a daemon process
def my_function():
    check_if_main_process()
    for i in range(10):
        print(f"Daemon process is running: iteration {i}")
        p = multiprocessing.Process(target=my_function2)
        p.start()
        time.sleep(1)  # Simulate work with sleep


if __name__ == "__main__":
    # Create a daemon process
    daemon_process = multiprocessing.Process(target=my_function)
    daemon_process.daemon = False
    daemon_process.start()  # Start the daemon process
    check_if_main_process()
    print("Main process will exit in 5 seconds...")
    time.sleep(5)
    print("Main process is exiting. Daemon will stop.")

    # The daemon process will be terminated when the main process exits
