#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:05:39 2024

@author: jonathancruz
"""


import time 
import pandas as pd 
import requests
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
import math
import re

def get_state_id(district, school_numbe):
    if len(district) == 1:
        district = "0" + district
    state_id_url = "https://opengovny.com/school/{}"
    parse = "32{}00011{}".format(district, school_numbe)
    return state_id_url.format(parse)

    
schools = pd.read_csv("bronx_high_test.csv")

schools = schools.drop_duplicates(subset=['code'])
urls = list()
for index, row in schools.iterrows():
    url = get_state_id(str(row["district"]), str(row["code"]))
    urls.append(url)
    
district = schools["district"].tolist()
code = schools["code"].tolist()
name = schools["name"].tolist()



df = pd.DataFrame({"district": district, "code": code, "name": name, "urls": urls})

## does not accept request s muct insert manually 

inst = [800000046252, \
    	800000057979, \
        800000058074, \
        800000059126, \
        800000057984, \
        800000058081, \
        800000058085, \
        800000058089, \
        800000059092, \
        800000058099, \
        800000059087, \
        800000057980, \
        800000059076, \
        800000059091, \
        800000057981, \
        800000077812, \
        800000059106, \
        800000059128, \
        800000077822, \
        800000057982, \
        800000057983, \
        800000059085, \
        800000057986, \
        800000059071, \
        800000058011, \
        800000058028, \
        800000058110, \
        800000057985, \
        800000058009, \
        800000057978, \
        800000058068, \
        800000058048, \
        800000057977, \
        800000058047, \
        800000058105, \
        800000077814, \
        800000059609, \
        800000059616, \
        800000059630, \
        800000059631, \
        800000077815, \
        800000077816, \
        800000077820, \
        800000077823, \
        800000077824, \
        800000060383, \
        800000060370, \
        800000046209, \
        800000060390, \
        800000060369, \
        800000060399, \
        800000060401, \
        800000062370, \
        800000062376, \
        800000062377, \
        800000045617, \
        800000056059, \
        800000045618, \
        800000056068, \
        800000056069, \
        800000056060, \
        800000056061, \
        800000069143, \
        800000056062, \
        800000056071, \
        800000056072, \
        800000056073, \
        800000056074, \
        800000045624, \
        800000057135, \
        800000045625, \
        800000069146, \
        800000056063, \
        800000045627, \
        800000056064, \
        800000056065, \
        800000065477, \
        800000065478, \
        800000045659, \
        800000045661, \
        800000045662, \
        800000045609, \
        800000045609, \
        800000070871, \
        800000070872, \
        800000070875, \
        800000059094, \
        800000059101, \
        800000058016, \
        800000070893, \
        800000070866, \
        800000070868, \
        800000045630, \
        800000056066, \
        800000045631, \
        800000070867, \
        800000057138, \
        800000057139, \
        800000057140, \
        800000057141, \
        800000057143, \
        800000057145, \
        800000057148, \
        800000045664, \
        800000057149, \
        800000075020, \
        800000075021, \
        800000075023, \
        800000075026, \
        800000075028, \
        800000075027]
df["inst"] = inst

df.to_csv("instid.csv",  encoding='utf-8', index=False)
