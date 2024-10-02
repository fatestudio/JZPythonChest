if __name__ == '__main__':
    from cachetools import LRUCache

    # Create an LRU cache with a maximum size of 3
    cache = LRUCache(maxsize=3)

    # Add some items to the cache
    cache[1] = 'one'
    cache[2] = 'two'
    cache[3] = 'three'
    print(
        cache
    )  # LRUCache([(1, 'one'), (2, 'two'), (3, 'three')], maxsize=3, currsize=3)

    # Access an item (key 1), making it recently used
    print(cache[1])  # Outputs: 'one'
    print(
        cache
    )  # LRUCache([(2, 'two'), (3, 'three'), (1, 'one')], maxsize=3, currsize=3)

    # Add another item, causing the least recently used (key 2) to be evicted
    cache[4] = 'four'
    print(
        cache
    )  # LRUCache([(3, 'three'), (1, 'one'), (4, 'four')], maxsize=3, currsize=3)
