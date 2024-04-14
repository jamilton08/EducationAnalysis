#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:08:18 2024

@author: jonathancruz
"""

import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
import re



def clean_name(name):
  return re.sub("-.+$", "", name)  

def clean_regents_name(name):
    name = re.sub("\(\d+-\d+\)", "", name)
    return name.replace("ANNUAL REGENTS EXAMINATION IN", "")



levels = list()
units = list()
url="https://data.nysed.gov/essa.php?instid={}&year=2023&createreport=1&regents=1"



options = webdriver.ChromeOptions() 


options.page_load_strategy = "none"


driver = Chrome(options=options) 

driver.implicitly_wait(5)



# read csv ]
schools = pd.read_csv("instid.csv")
for index, row in schools.iterrows():
    req = url.format(str(row["inst"]))
    driver.get(req) 
    time.sleep(20)
    
    school_name = clean_name(driver.find_element(By.CLASS_NAME, "uppercase").text)
    
    content =  driver.find_elements(By.CLASS_NAME, "nobreak")
    
    for c in content:
        try : 
            regents_name = clean_regents_name(c.find_element(By.TAG_NAME, "h4").text)
            table = c.find_element(By.TAG_NAME, "tbody")
            for row in table.find_elements(By.TAG_NAME, "tr"):
                th = row.find_element(By.TAG_NAME, "th").text
                if th == "American Indian or Alaska Native" or th == "Asian or Native Hawaiian/Other Pacific Islander" or\
                    th == "Black or African American" or th == "Hispanic or Latino" or th == "White":
                    cols = row.find_elements(By.TAG_NAME, "td")
                    if len(cols) >= 13:
                        total_tested = cols[0].text
                        l1n = cols[1].text
                        l1p = cols[2].text
                        l2n = cols[3].text
                        l2p = cols[4].text
                        l3n = cols[5].text
                        l3p = cols[6].text
                        l4n = cols[7].text
                        l4p = cols[8].text
                        l5n = cols[9].text
                        l5p = cols[10].text
                        proficient_students = cols[11].text
                        proficient_percents = cols[12].text
                        levels.append([school_name, regents_name,th, l1n, l1p])
                        levels.append([school_name, regents_name,th, l2n, l2p])
                        levels.append([school_name, regents_name,th, l3n, l3p])
                        levels.append([school_name, regents_name, th, l4n, l4p])
                        levels.append([school_name, regents_name,th,l5n,l5p])
                        units.append([school_name, regents_name, th, total_tested, proficient_students, proficient_percents] )
        except NoSuchElementException:
            print("something happended")
            
        print(levels)
        
            
            
            
print(levels)
print(units)

df = pd.DataFrame(levels, columns=["school_name", "regents","group", "level_n", "level_p"])
dfu = pd.DataFrame(units, columns=["school_name", "regents","group", "totals_tested", "proficient", "proficient_percent"])
df.to_csv("regents_scores"".csv",  encoding='utf-8', index=False)
dfu.to_csv("totals.csv",  encoding='utf-8', index=False)
pd.set_option('display.max_columns', None)
print(df.head(20))

