# !/usr/local/bin/python3
# -*- coding: UTF-8 -*-

class Grid:
    base_price = 0
    distance = 0.1
    amount = 100

    def __init__(self, p, d, a):
        self.base_price = p
        self.distance = d
        self.amount = a

    def estimate(self, price):
        if price >= self.base_price / (1 - self.distance):
            return 1, self.base_price / (1 - self.distance)
        elif price <= self.base_price * (1 - self.distance):
            return -1, self.base_price * (1 - self.distance)
        else:
            return 0, price

    def update_base(self, new_base):
        self.base_price = new_base
