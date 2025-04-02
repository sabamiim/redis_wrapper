from redis_wrapper import RedisWrapper


redis_db = RedisWrapper()



redis_db.set("test_key","hello redis",ex=10)
value = redis_db.get("test_key")
print("value:",value)


redis_db.set("user:1",{"name":"ali","age":30})
print(redis_db.get("user:1001"))



print(redis_db.search_keys("user:*"))