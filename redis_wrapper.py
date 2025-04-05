import json

import redis


class RedisWrapper:

    def __init__(self, host="localhost", port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def set(self, key, value, ex=None):
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        self.client.set(key, value, ex=ex)

    def get(self, key):
        value = self.client.get(key)
        try:
            return json.loads(value)
        except (TypeError, json.JSONDecodeError):
            return value

    def delete(self, key):
        self.client.delete(key)

    def exists(self, key):
        return self.client.exists(key)

    def expire(self, key, seconds):
        self.client.expire(key, seconds)

    def hset(self, name, key, value):
        self.client.hset(name, key, value)

    def hget(self, name, key):
        return self.client.hget(name, key)

    def hgetall(self, name):
        return self.client.hgetall(name)

    def hdel(self, name, key):
        self.client.hdel(name, key)

    def set_with_collection(self, collection, key, value, ex=None):
        full_key = f"{collection}:{key}"
        self.set(full_key, value, ex)

    def get_from_collection(self , collection, key):
        full_key = f"{collection}:{key}"
        self.get(full_key)

    def delete_from_collection(self , collection, key):
        full_key = f"{collection}:{key}"
        self.delete(full_key)

    def set_cache(self, key , value , cache_type="LRU", ttl=60):
        if cache_type not in ["LRU","LFU"]:
            raise ValueError("not supported")

        self.set(key, value , ex=ttl)

    def get_cache(self, key):
        return self.get(key)


    def batch_set(self, data):
        pipeline = self.client.pipeline()
        for key, value in data.items():
            pipeline.set(key, json.dumps(value))
        pipeline.execute()

    def batch_get(self, keys):
        values = self.client.mget(keys)
        return [json.loads(v) if v else None for v in values]

    def search_keys(self , pattern):
        return self.client.keys(pattern)


    def scan_keys(self, pattern , count=100):
        cursor = "0"
        keys = []
        while cursor !=0:
            cursor, found_key = self.client.scan(cursor=cursor , match=pattern,count=count)
            keys.extend(found_key)
        return keys

