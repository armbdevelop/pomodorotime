import redis


def get_redis_conn() -> redis.Redis:
    return redis.Redis(
        host='localhost',
        port=6379,
        db=0
    )
