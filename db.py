import pymysql
pymysql.install_as_MySQLdb()

import sys

try:
    import MySQLdb as Database
except ImportError as err:
    sys.exit(err)


def connect():
    print("Creating connection")
    return Database.connect(host='localhost',
                            port=8806,
                            user='root',
                            password='password',
                            db='test',
                            charset='utf8mb4')
