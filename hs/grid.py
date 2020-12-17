#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

from fmz import *

class Grid:
    base_price = 0
    distance = 0.1
    funds = 100
    price_precision = 5
    amount_precision = 3

    def __init__(self, base, distance, funds, price_precision, amount_precision):
        self.base_price = base
        self.distance = distance
        self.funds = funds
        self.price_precision = price_precision
        self.amount_precision = amount_precision

    def estimate(self, price):
        top = _N(self.base_price / (1 - self.distance), self.price_precision)
        bottom = _N(self.base_price * (1 - self.distance), self.price_precision)
        if price >= top:
            return 1, top
        elif price <= bottom:
            return -1, bottom
        else:
            return 0, price

    def update_base(self, new_base):
        self.base_price = new_base

    def top(self):
        top = _N(self.base_price / (1 - self.distance), self.price_precision)
        base_amount = _N(self.funds / self.base_price, self.amount_precision)
        return top, base_amount
    def bottom(self):
        bottom = _N(self.base_price * (1 - self.distance), self.price_precision)
        amount = _N(self.funds / bottom, self.amount_precision)
        return bottom, amount
