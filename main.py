from redis_wrapper import RedisWrapper

if __name__ == "__main__":
    redis_db = RedisWrapper()



    redis_db.set("name","saba",ex=120)
    print(redis_db.get("name"))

    redis_db.set("user:1",{"name":"ali","age":22})
    print(redis_db.get("name"))

    redis_db.set_with_collection("users", "1001", {"name": "saba", "email": "smoradi682@gmail.com"})
    print(redis_db.get_from_collection("users", "1001"))

    redis_db.batch_set({"key1": "value1", "key2": "value2"})
    print(redis_db.batch_get(["key1", "key2"]))

    print(redis_db.search_keys("user:*"))