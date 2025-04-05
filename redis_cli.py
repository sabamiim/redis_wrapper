from redis_wrapper import RedisWrapper
import json
redis_db = RedisWrapper()


key = input("Enter key :")
value = input("Enter value: ")

redis_db.set(key, value)
print(f"Value saved ! key: {key}, value:{value}")


print("stored saved :" , redis_db.get(key))

#json


try:
    value = json.loads(value)
    redis_db.set(key, value)
    print(f"json saved! key:{key}, value: {value}")
except json.JSONDecodeError:
    print("invalid value and format")


