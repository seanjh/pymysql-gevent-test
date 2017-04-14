#!/usr/bin/env python3

from gevent import monkey
monkey.patch_all()

import random
import sys

from db import connect
from fetch import fetch_sync, fetch_async
from uuid import uuid4


MAX_WAIT_SECS = 5


def main():
    try:
        num = int(sys.argv[1])
    except:
        sys.exit("Nope")

    print("Running {:d} queries".format(num))

    waits = [
        random.random() * MAX_WAIT_SECS
        for _ in range(num)
    ]

    fetch_sync(num, waits)
    fetch_async(num, waits)


if __name__ == "__main__":
    main()
