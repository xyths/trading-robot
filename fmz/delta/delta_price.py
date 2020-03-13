'''backtest
start: 2020-03-08 00:00:00
end: 2020-03-09 00:00:00
period: 1d
exchanges: [{"eid":"OKEX","currency":"BTC_USDT"},{"eid":"Huobi","currency":"BTC_USDT"}]
'''

from fmz import *
import datetime
import json


def init():  # 初始化函数
    Log("策略版本: v0.1.0")
    Log("系统版本:", Version());
    Log("机器人进程ID:", GetPid());
    Log("是否是模拟回测:", IsVirtual());

    for ex in exchanges:
        Log("交易所名称:", ex.GetName(), "标签:", ex.GetLabel());
        account = ex.GetAccount();
        Log("帐户初始状态:", account);
        # Log("账户信息，Balance:", account.Balance, "FrozenBalance:", account.FrozenBalance, "Stocks:",
        #    account.Stocks, "FrozenStocks:", account.FrozenStocks);
        Log("交易对:", ex.GetCurrency());
        Log("基础货币:", ex.GetQuoteCurrency());
    # global base_balance, base_stocks
    # base_balance = account.Balance + account.FrozenBalance
    # base_stocks = account.Stocks + account.FrozenStocks
    pass


def CancelPendingOrders():
    Sleep(1000)  # 等待1秒
    for ex in exchanges:
        orders = _C(ex.GetOrders)
        for order in orders:
            _C(ex.CancelOrder, order["Id"])


def onTick():
    for ex in exchanges:
        account = _C(ex.GetAccount)
        # ticker = _C(ex.GetTicker)
        depth = ex.GetDepth()
        Log(depth)


def main():
    # 过滤非重要信息
    # SetErrorFilter("GetRecords:|GetOrders:|GetDepth:|GetAccount|:Buy|Sell|timeout");
    while True:  # 轮询模式
        CancelPendingOrders()  # 取消未成交的挂单
        onTick()  # 执行 onTick 函数
        # Log(_C(exchange.GetAccount)) # 打印当前账户信息
        Sleep(Interval * 1000)  # 休眠
