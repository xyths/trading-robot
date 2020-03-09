#!/usr/bin/env python3

'''backtest
start: 2018-02-19 00:00:00
end: 2018-03-22 12:00:00
period: 15m
exchanges: [{"eid":"OKEX","currency":"LTC_BTC","balance":3,"stocks":0}]
'''

from fmz import *

task = VCtx(__doc__)  # initialize backtest engine from __doc__
print(exchange.GetAccount())
print(exchange.GetTicker())
print(task.Join(True))  # print backtest result
