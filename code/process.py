# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:51:02 2021

@author: Neha
"""

import requests,json
import pandas as pd
import os
import configparser
from pandas.io import sql
import pymysql
from sqlalchemy import create_engine
import datetime
import logging


def get_data(input_path,input_file,user,password,hostname,database):
    complete_data =[]
    states_df = pd.read_csv(input_path+input_file)
    try:
        for city,state in zip(states_df["city"],states_df["state"]):
            #print(city,state)
            #print(api_url+"q="+city+"&appid="+api_key)
            response = requests.get(api_url+"q="+city+"&appid="+api_key)    
            response = response.json()
            data ={}
            data["city"] = city
            data["state"] = state
            data["temperature"] = response['main']['temp']
            data["pressure"] = response['main']['pressure']
            data["humidity"] = response["main"]["humidity"]
            data["weather"] = response["weather"][0]["description"]
            complete_data.append(data)
            logger.info("process completed for {}".format(city))
    except:
        logger.error("process failed for {}".format(city))

    complete_df = pd.DataFrame(complete_data)  
    try:   
        engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(user,password,hostname,database))
        complete_df.to_sql(table, con = engine,if_exists="append",index=False)
        logger.info("data inserted in database")
    except:
        logger.info("ërror in inserting data in database")
            
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(r'C:\Users\dell\python_projects\code\config\config.ini')
    input_path = config.get("INPUT","input_path")
    input_file = config.get("INPUT","input_file")
    api_url = config.get("API","api_url")
    api_key = config.get("API","api_key")
    hostname =  config.get("DATABASE","hostname")
    user =  config.get("DATABASE","user")
    password =  config.get("DATABASE","password")
    database =  config.get("DATABASE","dbname")
    table =  config.get("DATABASE","table")
    var_datetime = datetime.datetime.now().strftime('weather_%Y%m%d_%H%M%S.log')
    log_path = config.get("OUTPUT","log_path")
    var_pylogflnm = log_path  +"\\"+ var_datetime
    logging.basicConfig(filename=var_pylogflnm, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt = "%Y-%M-%d %H:%M:%S",filemode ='w')
    logger = logging.getLogger()
    logger.setLevel("INFO")
    get_data(input_path,input_file,user,password,hostname,database)        
        
        
        
        
        







