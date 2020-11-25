# Модуль для реализации модели публикации-подписки на основе Redis
# Публикатор
import redis
import random

conn = redis.Redis()
cats = ['siam', 'pers', 'maine', 'norwegian']
hats = ['stove', 'bowler', 'tam-o-shanter', 'fedora']
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print("Publish: %s wears %s" % (cat, hat))
    conn.publish(cat, hat)

