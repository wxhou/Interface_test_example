"""
缓存类
"""
import typing as t


class CachePool(object):
    """全局变量池"""

    def __init__(self):
        self.pool = {}

    def __getitem__(self, key: t.Text):
        return self.pool[key]

    def __setitem__(self, key: t.Text, value: t.Any):
        self.pool[key] = value

    def __delitem__(self, key: t.Text):
        return self.pool.pop(key, None)

    def __len__(self):
        return len(self.pool)

    def __bool__(self):
        return bool(self.pool)

    def __contains__(self, key: t.Text):
        return key in self.pool

    def get(self, key: t.Text):
        return self.pool.get(key)

    def set(self, key: t.Text, value: t.Any=None):
        self.pool.setdefault(key, value)

    def has(self, key: t.Text):
        return key in self.pool



cache = CachePool()

if __name__ == '__main__':
    print(len(cache))
