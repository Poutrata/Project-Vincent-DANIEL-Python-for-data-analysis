# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:14:51 2021

@author: 20cen
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'pagevalue':140})
