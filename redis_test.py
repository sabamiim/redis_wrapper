import pytest
from redis_wrapper import RedisWrapper

@pytest.fixture
def redis_db():
    return RedisWrapper()

def test_set_and_get(redis_db):
    redis_db.set("test_key", "Hello Redis!")
    assert redis_db.get("test_key") == "Hello Redis!"

def test_set_and_get_json(redis_db):
    data = {"name": "Ali", "age": 30}
    redis_db.set("user:1001", data)
    assert redis_db.get("user:1001") == data

def test_search_keys(redis_db):
    redis_db.set("test:1", "value1")
    redis_db.set("test:2", "value2")
    keys = redis_db.search_keys("test:*")
    assert len(keys) >= 2