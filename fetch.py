import gevent
import time

from db import connect


def profile(func):
    grn = hex(id(gevent.getcurrent()))

    def wrapped(*args, **kwargs):
        start = time.time()
        func_name = func.__name__
        print("{} / {} start".format(grn, func_name))
        func(*args, **kwargs)
        elapsed = time.time() - start
        print("{} / {} finish ({:0.6f}ms elapsed)"
              .format(grn, func_name, 1000 * elapsed))

    return wrapped


@profile
def _fetch(wait=1.0, connection=None):
    if not connection:
        connection = connect()

    with connection.cursor() as cursor:
        cursor.execute("SELECT SLEEP(%s)", [wait])
        cursor.fetchall()

    connection.close()


@profile
def fetch_sync(num, waits):
    for i, _ in enumerate(range(num)):
        _fetch(waits[i])


@profile
def fetch_async(num, waits):
    tasks = [
        gevent.spawn(_fetch, waits[i])
        for i, _ in enumerate(range(num))
    ]
    gevent.joinall(tasks, raise_error=True)
