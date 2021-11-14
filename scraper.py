import selenium
from selenium import webdriver  # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import os
import pyperclip
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://fossbytes.com/tools/random-name-generator')

driver.implicitly_wait(2)

numberset = driver.find_element_by_xpath('//*[@id="totalNames"]')
numberset.click()
numberset.send_keys(1000)

genname = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/form/div[3]/div/button')
genname.click()

copyname = driver.find_element_by_xpath('//*[@id="copyButton"]')
copyname.click()
driver.close()
driver.quit()

s = pyperclip.paste() 
with open('scraped.txt','w') as g:
   g.write(s)

fte = open('scraped.txt','a')

with open('scraped.txt', 'r') as infile, \
     open('fnames.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace(",", "\n ")
    outfile.write(data)
