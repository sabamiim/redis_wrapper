from redis_wrapper import RedisWrapper
redis_db = RedisWrapper()
key = input("Enter key: ")
value = input("Enter value: ")
redis_db.set(key, value)
print(f"Value saved! Key: {key}, Value: {value}")
print("Stored Value:", redis_db.get(key))

