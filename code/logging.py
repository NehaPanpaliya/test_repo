# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:07:24 2021

@author: dell
"""

import logging
import datetime

var_datetime = datetime.datetime.now().strftime('weather_%Y%m%d_%H%M%S.log')
log_path = "C:\\Users\\dell\\python_projects\\logs"
var_pylogflnm = log_path  +"\\"+ var_datetime
print(var_pylogflnm)
logging.basicConfig(level="ÏNFO",filename=var_pylogflnm, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt = "%Y-%M-%d %H:%M:%S",filemode ='w')
logger = logging.getLogger()
logger.setLevel("INFO")
logger.info('This will get logged')
