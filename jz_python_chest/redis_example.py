if __name__ == '__main__':
    import redis

    # Step 1: Connect to Redis
    # Assuming Redis is running locally on the default port (6379)
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Step 2: Set a key-value pair in Redis
    r.set('name', 'John Doe')

    # Step 3: Retrieve the value of the key
    name = r.get('name')
    print(f"Name from Redis: {name.decode('utf-8')}"
          )  # Decode the result to get a string

    # Step 4: Use Redis to increment a counter
    r.set('counter', 0)
    r.incr('counter')
    counter_value = r.get('counter')
    print(f"Counter value: {counter_value.decode('utf-8')}")

    # Step 5: Storing complex data like lists
    r.rpush('fruits', 'apple', 'banana', 'cherry')
    fruits = r.lrange('fruits', 0, -1)  # Get all list elements
    print("Fruits from Redis:", [fruit.decode('utf-8') for fruit in fruits])

    # Step 6: Set key with expiration (e.g., 5 seconds)
    r.set('temp_key', 'temp_value', ex=5)
    print(f"Temp key: {r.get('temp_key').decode('utf-8')}")
