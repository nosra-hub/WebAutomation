from lib2to3.pgen2 import driver
from re import X
from socket import timeout
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from locale import currency
from operator import index
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from unicodedata import name
import pandas as pd
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
web = webdriver.Chrome("/home/nosra/chromedriver")
#class selenium :webdriver.support.wait.WebDriverWait(web, timeout, poll_frequency=0.5, ignored_exceptions=None)


df=pd.read_excel('info1.xlsx')
url=["https://docs.google.com/forms/d/e/1FAIpQLScGMoYVsxtsQ0Je4RTYEZndWrKkdt5jJwXBcMAcOia2WuIRtA/viewform?usp=sf_link"]
for link in url:  
    for i in df.index :
     web.get(link)
     entry=df.loc[i]     
     name=web.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input")
     time.sleep(1)
     name.send_keys(entry['name'])
     time.sleep(1)
     lastName=web.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
     time.sleep(2)
     lastName.send_keys(entry['lastName '])
     #sect=web.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
     #time.sleep(3)


#wait = WebDriverWait(driver, 10)
#wait.until(
 #   EC.element_to_be_clickable(
  #      (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[3]/span")))  
     #currency.send_keys(entry['money'])
  #select_country = web.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div")
 #    x= WebDriverWait(web, 5).until(
#EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[5]")))

     

wait = WebDriverWait(web, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Tunisia")))
#select_C=Select(web.find_elements(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[3]/span"))
#select_C.select_by_index(1)
       
