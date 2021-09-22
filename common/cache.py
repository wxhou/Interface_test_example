"""
缓存类
"""

class CachePool(object):
    """全局变量池"""

    def __init__(self):
        self.pool = {}

    def __getitem__(self, key):
        return self.pool[key]

    def __setitem__(self, key, value):
        self.pool[key] = value

    def __delitem__(self, key):
        return self.pool.pop(key, None)

    def __len__(self):
        return len(self.pool)

    def __bool__(self):
        return bool(self.pool)

    def __contains__(self, key):
        return key in self.pool

    def get(self, key):
        return self.pool.get(key)

    def set(self, key, value=None):
        self.pool.setdefault(key, value)

    def has(self, key):
        return key in self.pool



cache = CachePool()

if __name__ == '__main__':
    print(len(cache))
