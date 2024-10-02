import time
from functools import lru_cache


# Define a function to simulate an expensive computation
@lru_cache(maxsize=3)  # Cache up to 3 unique calls
def expensive_function(x):
    print(f"Computing expensive_function({x})...")
    time.sleep(2)  # Simulate a time-consuming operation
    return x * x


# Call the function multiple times
if __name__ == "__main__":
    print(expensive_function(2))  # This will be computed and cached
    print(expensive_function(3))  # This will be computed and cached
    print(expensive_function(2))  # This will use the cached result
    print(expensive_function(4))  # This will be computed and cached
    print(
        expensive_function(5)
    )  # This will be computed and cached, LRU cache evicts the oldest entry (for x=2)
    print(expensive_function(
        2))  # This will be computed again (no longer in cache)
