#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

'''backtest
start: 2018-02-19 00:00:00
end: 2018-03-22 12:00:00
period: 15m
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD","balance":10000,"stocks":3}]
'''

from fmz import *
import math
import talib

task = VCtx(__doc__) # initialize backtest engine from __doc__

# ------------------------------ 策略部分开始 --------------------------

print(exchange.GetAccount())     # 调用一些接口，打印其返回值。
print(exchange.GetTicker())

def adjustFloat(v):             # 策略中自定义的函数
    v = math.floor(v * 1000)
    return v / 1000

def onTick():
    Log("onTick")
    # 具体的策略代码


def main():
    InitAccount = GetAccount()
    while True:
        onTick()
        Sleep(1000)

# ------------------------------ 策略部分结束 --------------------------

try:
    main()                     # 回测结束时会 raise EOFError() 抛出异常，来停止回测的循环。所以要对这个异常处理，在检测到抛出的异常后调用 task.Join() 打印回测结果。
except:
    print(task.Join())