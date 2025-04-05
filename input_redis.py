from redis_wrapper import RedisWrapper

redis_db = RedisWrapper()

key = input("enter value:")
value = redis_db.get(key)
if value is None:
    print("value is null. try again")
else:
    print(f"value saved. key : {key}, value: {value}")


