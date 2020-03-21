# !/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import hs.grid as grid


def test_grid():
    base_price = 1
    distance = 0.1
    g = grid.Grid(base_price, distance, 100)
    print("base_price: {}, distance: {}, amount: {}".format(g.base_price, g.distance, g.amount))
    price = 1.3
    expect = 1 / (1 - distance)
    assert g.estimate(price) == (1, expect)
    g.update_base(expect)
    print("base_price: {}, distance: {}, amount: {}".format(g.base_price, g.distance, g.amount))
    expect /= (1 - distance)
    assert g.estimate(price) == (1, expect)
    g.update_base(expect)
    print("base_price: {}, distance: {}, amount: {}".format(g.base_price, g.distance, g.amount))
    assert g.estimate(price) == (0, price)
    price = 0.9
    expect = 1 / (1 - distance)
    assert g.estimate(price) == (-1, expect)
