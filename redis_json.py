import json
from redis_wrapper import RedisWrapper
redis_db = RedisWrapper()

key = input("Enter key :")
value = input("Enter value: {'name':'ALi','age':'22'}:  ")

try:
    value = json.loads(value)
    redis_db.set(key, value)
    print(f"json saved! key:{key}, value: {value}")
except json.JSONDecodeError:
    print("invalid value and format")


