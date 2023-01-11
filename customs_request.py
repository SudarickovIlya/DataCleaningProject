import pandas as pd
import numpy as np
import selenium
import time
import requests
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime

driver = webdriver.Chrome()
time.sleep(2)

start = datetime.date(2021,12,31)
end = datetime.date(2022,1,1)

k = 366
dates_start = []
dates_end = []
for day in range(k):
    date_start = (start + datetime.timedelta(days = day)).strftime("%d.%m.%Y")
    dates_start.append(date_start)
    
    date_end = (end + datetime.timedelta(days = day)).strftime("%d.%m.%Y")
    dates_end.append(date_end)


with open('voloshino.txt', 'w') as f:
    for (i, j) in zip(dates_start, dates_end):
        
        driver.get(f'https://customs.gov.ru/checkpoints?rtu=&customs=&app=34&date_from={i}+13%3A28&date_to={j}+15%3A43&cars=2')
        #time.sleep(1)
        chose = driver.find_elements_by_css_selector('div.pin')
        if chose[0].text == 'Найдено 0':
            a = 'no data'
        else:
            a = chose[2].text.split('\n')[0], 'на въезд оформлено', chose[3].text.split('\n')[4], 'на выезд оформлено', chose[4].text.split('\n')[4]
        print(str(a))
        f.write(str(a))
        f.write('\n')
        print(' ')