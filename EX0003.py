# Project : show me the code
# Author : puorc
import EX0001
import redis

r_server = redis.Redis('localhost')
for i in EX0001.result:
    r_server.rpush('code', i)

