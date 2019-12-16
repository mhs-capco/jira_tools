#!/usr/bin/env python3

import sys

def time_split(tm_str):
    bits = tm_str.split()
    componts = {}
    for bit in bits:
        unit = bit[-1]
        val = int(bit[:-1])
        componts[unit] = val
    return componts

rates = {
    "w": 40.0,
    "d": 8.0,
    "h": 1.0,
    "m": 1.0/60,
}

def calc_hrs(tm, rts=rates):
    tot = 0.0
    for unit, val in tm.items():
        conv = rts[unit]
        tot += conv * val
    return tot

def build_str(args):
    time_strings = []
    for arg in args:
        if arg[0].isdigit():
            time_strings.append(arg)
    return ' '.join(time_strings)

if __name__ == '__main__':
    t_str = build_str(sys.argv)
    t_bits = time_split(t_str)
    #print t_bits
    hrs = calc_hrs(t_bits)
    print( "%s" % hrs)

