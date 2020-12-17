#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

from fmz import *


def hslog(*objects):
    if os.getenv('LOCALFMZ') == "1":
        print(*objects)
    else:
        Log(*objects)
