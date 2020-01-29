#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd
import numpy as np
from datetime import datetime

def monitor():
    r = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=')
    tx = r.text
    tx = tx.replace('\\n','')
    tx = tx.replace('\\','')
    tx = tx.replace(' ','')


    tx = tx.split('[')[1]
    tx = tx.split(']')[0]
    df = pd.read_json('['+tx+']')

    cn = df[df.country == '中国']


    now = datetime.now()
    current_time = now.strftime("%Y%m%d_%H%M")
    df.to_excel('virus/'+current_time+'.xlsx')

monitor()