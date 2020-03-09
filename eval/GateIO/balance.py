#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import getopt
import configparser
from gateAPI import GateIO
import datetime
import pandas as pd
import json
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


API_QUERY_URL = 'data.gateio.life'
API_TRADE_URL = 'api.gateio.life'


def get_api_key(configfile):
    print('Config file is ', configfile)
    config = configparser.ConfigParser()
    config.read(configfile)
    print("config sections:", config.sections())
    key = config["gate"]["key"]
    secret = config["gate"]["secret"]
    print("key: {}, secret: {}".format(key, secret))
    return key, secret


def get_history(api_key, secret_key):
    # gate_query = GateIO(API_QUERY_URL, api_key, secret_key)
    # print(gate_query.pairs())
    # res = gate_query.tradeHistory('sero_usdt')

    gate_trade = GateIO(API_TRADE_URL, api_key, secret_key)
    # print(gate_trade.pairs())
    # print(gate_trade.balances())
    res = gate_trade.mytradeHistory('sero_usdt', "")
    # print(res)
    trades = json.loads(res)["trades"]
    return json_to_df(trades)


'''
  {
    "tradeID": 232974139,
    "orderNumber": 9501827268,
    "pair": "sero_usdt",
    "type": "buy",
    "rate": "0.10968",
    "amount": "10.052",
    "total": 1.10250336,
    "date": "2020-03-06 14:11:44",
    "time_unix": 1583475104,
    "role": "taker",
    "fee": "0",
    "fee_coin": "sero",
    "gt_fee": "0",
    "point_fee": "0.001984506048"
  }
'''


def json_to_df(data):
    # trade_id = []
    date = []
    order_number = []
    order_type = []
    price = []
    amount = []
    total = []
    for j in data:
        # print(j)
        # trade_id.append(j["tradeID"])
        # date.append(datetime.datetime.fromtimestamp(int(j["timestamp"])))
        date.append(datetime.datetime.strptime(j["date"], "%Y-%m-%d %H:%M:%S"))
        order_number.append(j["orderNumber"])
        order_type.append(j["type"])
        price.append(float(j["rate"]))
        amount.append(float(j["amount"]))
        total.append(float(j["total"]))
    df = pd.DataFrame(
        {
            # "tradeId": trade_id,
            "orderNumber": order_number,
            "type": order_type,
            "amount": amount,
            "price": price,
            "total": total
        },
        index=date)
    return df


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
    api_key, secret_key = get_api_key(configfile)
    history = get_history(api_key, secret_key)
    # print(history)
    sell_history = history[history['type'] == 'sell']
    # print(sell_history)
    # print("sell len:", sell_history.nrows)
    buy_history = history[history['type'] == 'buy']
    # print(buy_history)
    # print("buy len:", buy_history.nrows)
    sell_price_list = sell_history.price
    buy_price_list = buy_history.price
    print(sell_price_list)
    print(buy_price_list)
    fig, ax = plt.subplots()
    ax.plot(sell_price_list.index, sell_price_list, 'ro--', label='Sell')  #
    ax.plot(buy_price_list.index, buy_price_list, 'g*--', label='Buy')  #
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
