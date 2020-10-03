# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:42:46 2020

@author: akrit
"""

import glassdoor_scraper as gs
import pandas as pd

path = "D:/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df