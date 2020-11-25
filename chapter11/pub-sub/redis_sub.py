# Подписчик Redis
import redis
conn = redis.Redis()
topics = ['maine', 'pers']
sub = conn.pubsub()
sub.subscribe(topics)
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: %s wears %s' % (cat, hat))
