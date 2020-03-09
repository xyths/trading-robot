#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''backtest
start: 2018-02-19 00:00:00
end: 2018-03-22 12:00:00
period: 15m
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD","balance":10000,"stocks":3}]
'''

import sys
import getopt
import configparser
from fmz import *

task = VCtx(__doc__)  # initialize backtest engine from __doc__
print(exchange.GetAccount())  # 调用一些接口，打印其返回值。
print(exchange.GetTicker())


def main(argv):
    configfile = ''
    try:
        opts, args = getopt.getopt(argv, "hc:", ["configfile="])
    except getopt.GetoptError:
        print('ma_across.py -c <configfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ma_across.py -c <configfile>')
            sys.exit()
        elif opt == "-c":
            configfile = arg
    print('Config file is ', configfile)
    config = configparser.ConfigParser()
    config.read(configfile)
    print("config sections:", config.sections())
    key = config["gate"]["key"]
    secret = config["gate"]["secret"]
    print("key: {}, secret: {}".format(key, secret))

    while True:
        Log(exchange.GetAccount().Balance)
        Sleep(2000)


if __name__ == "__main__":
    main(sys.argv[1:])
