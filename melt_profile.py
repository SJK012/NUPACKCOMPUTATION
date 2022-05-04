from asyncore import write

import os
from tkinter.filedialog import SaveAs
from tokenize import Double
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

numbers =[]
n=int(input("Enter the Number of Sequences: "))

print("Enter The Sequences")
for k in range (0,n):
   ele = input()

   numbers.append(ele)

initial = input("min_melt_temperature: ")

increment = input("melt_temperature_increment: ")

final = input("job_max_melt_temperature: ")

initial = int (initial)
increment =int(increment)
final = int(final)
innerloops = (final - initial + 1) /  25
innerloops = float(innerloops)

print(innerloops)

if int(innerloops) < innerloops :
                                   innerloops = int(innerloops) +1

print(innerloops)
print(int(innerloops))
for i in range(n):

                
                                       
                    for k in range(int(innerloops)):
                                                driver.get( 'http://www.nupack.org/partition/new')

                                                link1 = driver.find_element_by_id("partition_job_is_melt").click()


                                                link2 = driver.find_element_by_id("partition_job_min_melt_temperature").send_keys(initial+25*k)
                                                tempinitial= initial+25*k  

                                                link3 = driver.find_element_by_id("partition_job_melt_temperature_increment").send_keys(increment)
                                                
                                                if k==(int(innerloops)-1):
                                                                     link4 = driver.find_element_by_id("partition_job_max_melt_temperature").send_keys(final)
                                                                     print("this is if stement ",final)
                                                                     tempfinal = final

                                                elif k!=(int(innerloops)-1):                  
                                                                     link4 = driver.find_element_by_id("partition_job_max_melt_temperature").send_keys((k+1)*final/innerloops)
                                                                     print("this is elif stement ",(k+1)*final/innerloops)
                                                                     tempfinal = (k+1)*final/innerloops
                                                
                                                link5 = driver.find_element_by_id("partition_sequence_0_contents").send_keys(numbers[i])


                                                element1 = driver.find_element_by_name("commit")
                                                element1.click()

                                                try:
                                                    r1= WebDriverWait(driver, 120 ).until(EC.presence_of_element_located((By.ID,"melt_curve" )))

                                                    r1.click()


                                                except: 
                                                       driver.refresh()


                                                try:
                                                    r2= WebDriverWait(driver, 120 ).until(EC.presence_of_element_located((By.LINK_TEXT,"Download data" )))

                                                    r2.click()


                                                except:
                                                       driver.refresh()
 

                                                html = driver.page_source
                                                fileToWrite = open(str(i+1)+"_"+str(tempinitial)+"_"+str(tempfinal)+".txt", "w")
                                                fileToWrite.write(html)
                                                fileToWrite.close()

                                                print(i+1,":",tempinitial,"_",tempfinal," ","DONE")
                                                time.sleep(5)
                                                             



driver.close()
