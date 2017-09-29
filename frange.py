# -*- coding: utf-8 -*-
"""
Author: Luc Frachon

"""

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump