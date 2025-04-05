from redis_wrapper import RedisWrapper

redis_db = RedisWrapper()

key = input("enter key to delete : ")

if redis_db.get(key):
    redis_db.delete(key)
    print(f"deleted key:{key}")
else:
    print(f"not found {key}. try again")
