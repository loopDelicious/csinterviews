# Cache -
#
# Hardware
# - hard disk
# - main memory
#
# LRU Cache
#
# 5 1 2 3
#
# Implement an LRU Cache
#
# 1,2,3,4
# {}Main memory
# Hard Disk => look in Main Memory {1: [timestamp, data],2,3,4}
#
# function (data)
# is data in main memory
# if not
#     find last accessed data, kick out of main
#     add data from hard disk
#
# d = {}
# d['foo'] = 'bar'
# del d['foo']

class Cache:
    def __init__(self):
        self.cache = {}
        self.maxsize = 30

    def search(self, key):
        if key in self.cache:
            return self.cache[key]

    def add(self, key):
        if self.count() < self.maxsize:
            val = HardDisk.get(key)
            self.cache[key] = val
            return val
        else:
            key = self.leastUsed()
            del self.cache[key]()
            val = HardDisk.get(key)
            self.cache[key] = val
            return val
            # add timestamp too

    def count(self):
        return len(self.cache)

def leastUsed(self):
    timestamp = self.cache[key][0]
    target = None
    for key, val in self.cache.items():
        potential = self.cache[key][0]
        if potential < timestamp:
            target = key
    return target

