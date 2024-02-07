#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from File import Pac

if __name__ == '__main__':
    stri = Pac.get_input()
    if Pac.test_input(stri):
        num = Pac.str_to_int(stri)
        Pac.print_int(num)
    else:
        print("Строка не числовая")
        