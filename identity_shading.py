
from ast import increment_lineno
import urllib 
from asyncore import write
from msilib.schema import File
import os
from tkinter.filedialog import SaveAs
from webbrowser import Chrome
import warnings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import codecs

 
warnings.filterwarnings("ignore")
PATH='C:\Program Files (x86)\chromedriver '
driver= webdriver.Chrome(PATH)

# Enter the Sequence here
numbers =[]
n=int(input("Enter the Number of Sequences: "))

print("Enter The Sequences")
for k in range (0,n):
   ele = input()

   numbers.append(ele)



initial = input("Enter the initial temperature: ")

increment = input("Enter the increment temperature: ")

final = input("Enter the final temperature: ")

initial = int (initial)
tempinitial = initial
increment =int(increment)
final = int(final)

loops2 = (final - initial + 1) /  increment

loops2 = int (loops2)

for i in range(n):
                print('   ')
                initial = tempinitial
                for j in range(loops2):

                                  
                                  driver.get( 'http://www.nupack.org/partition/new')
                              
                                  print(numbers[i],j+1, end = '')
                                  link1 = driver.find_element_by_id("partition_job_temperature").clear()
                                  link1 = driver.find_element_by_id("partition_job_temperature").send_keys(initial)

                                  print('.',end ='')


                
                                  link5 = driver.find_element_by_id("partition_sequence_0_contents").send_keys(numbers[i])
                                  print('.',end ='')


                                  element1 = driver.find_element_by_name("commit")
                                  element1.click()
                                  print('.',end ='')

                                  time.sleep(2)

                                  try:
                                         r1= WebDriverWait(driver, 120 ).until(EC.presence_of_element_located((By.ID,"partition_image_toggle_1" )))

                                         r1.click()
                                         print('.',end ='')

                                  except: 
                                        driver.refresh()


                                  time.sleep(2)

                                  try:
                                        r2= WebDriverWait(driver, 120 ).until(EC.presence_of_element_located((By.ID,"fullsize")))

                                        r2.click()
                                        print('.',end ='')

                                  except:
                                           driver.refresh()

                                  print('.',end ='')
                                  time.sleep(2)

                                  img = driver.find_element_by_xpath('//div[@id="fullsize"]/img')
                                  src = img.get_attribute('src')

                                  print('.',end ='')
                                  driver.get( src)
                                  
                                  
                                  driver.save_screenshot(str(i+1)+"..."+ str(initial)+' Centigrade.b'+'.png')
                                  print('/',end='')
                                  
                                  initial = initial + increment
                                  
                                  time.sleep(5)
                                  print('Done')
                 


                         
time.sleep(5)   
print("ALL CASES DONE AND SAVED")
driver.close()
                    