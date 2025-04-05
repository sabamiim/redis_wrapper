from redis_test import redis_db
from redis_wrapper import RedisWrapper

redis_db = RedisWrapper()


key = input("Enter key :")
value = input("Enter value: ")

redis_db.set(key, value)
print(f"Value saved ! key: {key}, value:{value}")


print("stored saved :" , redis_db.get(key))


