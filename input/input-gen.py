import random

random.seed(201120848)

with open('BACKINGSTORE.bin', 'w') as f:
    for _ in range(256*256):
        r = int(random.random()*256)
        f.write('%c' % r)

with open('linear-access.txt', 'w') as f:
    for it in range(10000, 20000):
        f.write('%d\n' % it)

with open('random-access.txt', 'w') as f:
    for _ in range(5000):
        f.write('%d\n' % int(random.random()*60000))
