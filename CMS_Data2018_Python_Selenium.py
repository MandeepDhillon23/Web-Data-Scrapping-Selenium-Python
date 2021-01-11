#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This code is for scrapping web data from "https://data.cms.gov/mapping-medicare-disparities".
# The data is from all states, for county level data by different selections as elements and varaiables.


# In[ ]:


#Run only once. Delete or comment it out after installation is complete
get_ipython().system('pip install selenium')


# In[ ]:


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


# In[ ]:


# get the working directory information
import os
cwd = os.getcwd()
print(cwd)


# In[ ]:


#all downloads will be in this folder. But sometimes this code doesnt work then get all files in the downloads
# And then manually paste in a folder

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:/Users/MD/Downloads/CMS2018_CountyUSA"}
chromeOptions.add_experimental_option("prefs",prefs)


# In[ ]:


# Here the code is splitted as per requiremnts.No fix formula.Make a varaible list and then make loops to downlad
# here follow the excel data selection sheet 1 color codes to make the loops for measure,domain and condition.
# year, adjust, analysis, sex code is single selection for the all the variables.
# gepgraphy has two parts-state and county level, meaure,condition,age group, dual,race code has many selections
# here in this cell - data with domain d1
# download the chromedrivers. Change the path based on where you have the driver installed.
# install chrome driver compatible with chrome and python version.

driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://data.cms.gov/mapping-medicare-disparities")
try:
    driver.find_element_by_xpath("/html/body/div[1]/button/span[1]").click()
except:
    pass
for y in [8]:
    element_year=driver.find_element_by_id("year")
    drp_year=Select(element_year)
    drp_year.select_by_value(str(8))
    time.sleep(2)
    element_adjust=driver.find_element_by_id("adjust")
    drp_adjust=Select(element_adjust)
    drp_adjust.select_by_value(str('1'))
    time.sleep(2)
    element_analysis=driver.find_element_by_id("analysis")
    drp_analysis=Select(element_analysis)
    drp_analysis.select_by_value(str('base'))
    time.sleep(2)
    element_gender=driver.find_element_by_id("sex_code")
    drp_gender=Select(element_gender)
    drp_gender.select_by_value(str('null'))
    time.sleep(2)
    element_county=driver.find_element_by_id("geography")
    drp_geo=Select(element_county)
    drp_geo.select_by_value('s')
    time.sleep(2)
    a=0
    for d in ["d1"]:
        element_domain=driver.find_element_by_id("domain")
        drp_domain=Select(element_domain)
        drp_domain.select_by_value(str('d1'))
        for m in ["p","e","h","m","v"]:
            element_measure=driver.find_element_by_id("measure")
            drp_measure=Select(element_measure)
            drp_measure.select_by_value(str(m))
            time.sleep(2)
            for c in [1,2,14,15,16,17,20,24,78]:
                element_condition=driver.find_element_by_id("condition")
                drp_condition=Select(element_condition)
                drp_condition.select_by_value(str(c))
                for a in ["null",0,1,2,3]:
                    element_age=driver.find_element_by_id("age_group")
                    drp_age=Select(element_age)
                    drp_age.select_by_value(str(a))
                    time.sleep(2)
                    for u in ["null",0,1]:
                        element_dual=driver.find_element_by_id("dual")
                        drp_dual=Select(element_dual)
                        drp_dual.select_by_value(str(u))
                        time.sleep(2)
                        for r in ["null",1,2,3,4,5,6]:
                            element_race=driver.find_element_by_id("race_code")
                            drp_race=Select(element_race)
                            drp_race.select_by_value(str(r))
                            time.sleep(2)
                            driver.find_element_by_xpath("//*[@id='data_download']").click()
                  
    driver.close() 


# In[ ]:


# when more than one conditions have similar code number like here
# for measure=e (emergency)  domain=d1(pri chronic)  condition=10 (all emergency visits)
#Change the path based on where you have the driver installed.
driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://data.cms.gov/mapping-medicare-disparities")
try:
    driver.find_element_by_xpath("/html/body/div[1]/button/span[1]").click()
except:
    pass
for y in [8]:
    element_year=driver.find_element_by_id("year")
    drp_year=Select(element_year)
    drp_year.select_by_value(str('8'))
    time.sleep(2)
    element_adjust=driver.find_element_by_id("adjust")
    drp_adjust=Select(element_adjust)
    drp_adjust.select_by_value(str('1'))
    time.sleep(2)
    element_analysis=driver.find_element_by_id("analysis")
    drp_analysis=Select(element_analysis)
    drp_analysis.select_by_value(str('base'))
    time.sleep(2)
    element_gender=driver.find_element_by_id("sex_code")
    drp_gender=Select(element_gender)
    drp_gender.select_by_value(str('null'))
    time.sleep(2)
    element_county=driver.find_element_by_id("geography")
    drp_geo=Select(element_county)
    drp_geo.select_by_value('s')
    time.sleep(2)
    a=0
    for d in ["d1"]:
        element_domain=driver.find_element_by_id("domain")
        drp_domain=Select(element_domain)
        drp_domain.select_by_value(str('d1'))
        for m in ["e"]:
            element_measure=driver.find_element_by_id("measure")
            drp_measure=Select(element_measure)
            drp_measure.select_by_value(str(m))
            time.sleep(2)
            for c in [10]:
                element_condition=driver.find_element_by_id("condition")
                drp_condition=Select(element_condition)
                drp_condition.select_by_value(str(c))
                for a in ["null",0,1,2,3]:
                    element_age=driver.find_element_by_id("age_group")
                    drp_age=Select(element_age)
                    drp_age.select_by_value(str(a))
                    time.sleep(2)
                    for u in ["null",0,1]:
                        element_dual=driver.find_element_by_id("dual")
                        drp_dual=Select(element_dual)
                        drp_dual.select_by_value(str(u))
                        time.sleep(2)
                        for r in ["null",1,2,3,4,5,6]:
                            element_race=driver.find_element_by_id("race_code")
                            drp_race=Select(element_race)
                            drp_race.select_by_value(str(r))
                            time.sleep(2)
                            driver.find_element_by_xpath("//*[@id='data_download']").click()
                  
    driver.close()      


# In[ ]:


# data with domain d2 (chronic condition) measure = prevalence(v) and different conditions
driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://data.cms.gov/mapping-medicare-disparities")
try:
    driver.find_element_by_xpath("/html/body/div[1]/button/span[1]").click()
except:
    pass
for y in [8]:
    element_year=driver.find_element_by_id("year")
    drp_year=Select(element_year)
    drp_year.select_by_value(str('8'))
    time.sleep(2)
    element_adjust=driver.find_element_by_id("adjust")
    drp_adjust=Select(element_adjust)
    drp_adjust.select_by_value(str('1'))
    time.sleep(2)
    element_analysis=driver.find_element_by_id("analysis")
    drp_analysis=Select(element_analysis)
    drp_analysis.select_by_value(str('base'))
    time.sleep(2)
    element_gender=driver.find_element_by_id("sex_code")
    drp_gender=Select(element_gender)
    drp_gender.select_by_value(str('null'))
    time.sleep(2)
    element_county=driver.find_element_by_id("geography")
    drp_geo=Select(element_county)
    drp_geo.select_by_value('s')
    time.sleep(2)
    a=0
    for d in ["d2"]:
        element_domain=driver.find_element_by_id("domain")
        drp_domain=Select(element_domain)
        drp_domain.select_by_value(str('d2'))
        for m in ["v"]:
            element_measure=driver.find_element_by_id("measure")
            drp_measure=Select(element_measure)
            drp_measure.select_by_value(str(m))
            time.sleep(2)
            for c in [43,51,57,75,110,69]:
                element_condition=driver.find_element_by_id("condition")
                drp_condition=Select(element_condition)
                drp_condition.select_by_value(str(c))
                for a in ["null",0,1,2,3]:
                    element_age=driver.find_element_by_id("age_group")
                    drp_age=Select(element_age)
                    drp_age.select_by_value(str(a))
                    time.sleep(2)
                    for u in ["null",0,1]:
                        element_dual=driver.find_element_by_id("dual")
                        drp_dual=Select(element_dual)
                        drp_dual.select_by_value(str(u))
                        time.sleep(2)
                        for r in ["null",1,2,3,4,5,6]:
                            element_race=driver.find_element_by_id("race_code")
                            drp_race=Select(element_race)
                            drp_race.select_by_value(str(r))
                            time.sleep(2)
                            driver.find_element_by_xpath("//*[@id='data_download']").click()
            
            
    driver.close()   


# In[ ]:


pip install pandas


# In[ ]:


#to combine the data in a single set
# download data in a folder and use this code to combine the files in the folder
import os
import glob
import pandas as pd
import numpy as np
os.chdir(r'C:\Users\*\Downloads\CMS2018_State_Metadata')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


# In[ ]:


# combine data in csv
data=pd.read_csv("combined_csv.csv")


# In[ ]:


# show the 10 lines of new dataset
data.head(10)


# In[ ]:




