"""
缓存类
"""
import typing as t
from collections import UserDict


class CachePool(UserDict):
    """全局变量池"""
    
    def get(self, key: t.Text, default=None) -> t.Any:
        return self.data.get(key, default)

    def set(self, key: t.Text, value: t.Any=None) -> None:
        self.data.setdefault(key, value)

    def has(self, key: t.Text) -> bool:
        return key in self.data

    def __len__(self) -> int:
        return len(self.data)

    def __bool__(self) -> bool:
        return bool(self.data)



cache = CachePool()

if __name__ == '__main__':
    print(len(cache))
