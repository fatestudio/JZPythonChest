from collections import OrderedDict


class LRUCache:

    def __init__(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        # Return the value if the key is in the cache and move it to the end to mark it as recently used
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1  # Cache miss

    def put(self, key, value):
        # Add the key-value pair to the cache
        if key in self.cache:
            # If the key already exists, move it to the end to mark it as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        # If the cache exceeds the max size, pop the first item (the least recently used one)
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)


if __name__ == '__main__':
    # Example usage of the LRUCache
    lru_cache = LRUCache(max_size=3)

    lru_cache.put(1, 'one')
    lru_cache.put(2, 'two')
    lru_cache.put(3, 'three')
    print(
        lru_cache.cache)  # OrderedDict([(1, 'one'), (2, 'two'), (3, 'three')])

    # Access key 1, which moves it to the end as most recently used
    print(lru_cache.get(1))  # Outputs: 'one'
    print(
        lru_cache.cache)  # OrderedDict([(2, 'two'), (3, 'three'), (1, 'one')])

    # Add another item, which causes the oldest (key 2) to be evicted
    lru_cache.put(4, 'four')
    print(lru_cache.cache
          )  # OrderedDict([(3, 'three'), (1, 'one'), (4, 'four')])
