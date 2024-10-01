import time

from tqdm import tqdm

if __name__ == '__main__':
    # Example: Processing a list with a progress bar
    numbers = list(range(1, 101))

    print("Processing numbers:")

    # Using tqdm to show progress
    for number in tqdm(numbers, desc="Progress", unit="item"):
        # Simulate some processing time
        time.sleep(0.05)
