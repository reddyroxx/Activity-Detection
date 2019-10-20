#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:05:00 2019

@author: rakesh
"""

import pandas as pd
import numpy as np
import random

df = pd.read_csv('1.csv')
ts = list(df['timestamp'])
sl = list(df['sl_no'])
k=len(sl)


for i in range(0,k):
    a=random.randint(100000,900000)
    ts[i]=a
    
df['timestamp'] = ts    
df.to_csv('1_1.csv',sep=',')