import pytest

import hour_parser

@pytest.fixture
def wks_dys_hrs_dic():
    return {'w': 13.0,
            'd': 3.0,
            'h': 7.0,
            }

@pytest.fixture
def wks_dys_hrs_str():
    return "13w 3d 7h"

def test_default_config():
    assert hour_parser.rates['w'] == 40.0
    assert hour_parser.rates['d'] == 8.0
    assert hour_parser.rates['h'] == 1.0
    assert hour_parser.rates['m'] == 1.0/60.0

def test_time_split(wks_dys_hrs_str, wks_dys_hrs_dic):
    t_bits = hour_parser.time_split(wks_dys_hrs_str)
    for key, val in wks_dys_hrs_dic.items():
        assert key in t_bits
        assert val == t_bits[key]
    assert len(t_bits) == len(wks_dys_hrs_dic)

def test_calc_hrs(wks_dys_hrs_dic):
    hrs = 0.0
    hrs += 13 * 40.0
    hrs += 3 * 8.0
    hrs += 7.0
    assert hour_parser.calc_hrs(wks_dys_hrs_dic) == hrs

def test_build_string(wks_dys_hrs_dic, wks_dys_hrs_str):
    args = ["%i%s" % (v,k) for k,v in wks_dys_hrs_dic.items()]
    assert hour_parser.build_str(args) == wks_dys_hrs_str
