#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import os
import sqlite3
import settings

sqlite_path = os.path.join(settings.BASE_DIR, 'database', 'sqlite3.sqlite')


class SQLite:
    def __init__(self):
        self.con = sqlite3.connect(sqlite_path)
        self.cur = self.con.cursor()

    def __enter__(self):
        """
        with as 打开数据库
        :return:
        """
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    with SQLite() as f:
        f.execute('select * from TEACHER;')
        print(f.fetchall())
