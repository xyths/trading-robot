#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

'''backtest
start: 2018-02-19 00:00:00
end: 2018-03-22 12:00:00
period: 15m
exchanges: [{"eid":"OKEX","currency":"LTC_BTC","balance":3,"stocks":0}]
'''

from fmz import *
from hs import *

task = VCtx(__doc__)  # initialize backtest engine from __doc__

log("策略版本: v0.3.1")
log("系统版本:", Version())
log("机器人进程ID:", GetPid())
log("是否是模拟回测:", IsVirtual())

print(exchange.GetAccount())
print(exchange.GetTicker())
print(task.Join(True))  # print backtest result
