#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_input():
    string = input("Введите строку ")
    return string


def test_input(x):
    if x.isdigit():
        return True
    else:
        return False


def  str_to_int(x):
    y = int(x)
    return y


def  print_int(x):
    print(x)
