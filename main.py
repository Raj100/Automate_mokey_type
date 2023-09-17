import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from bs4 import BeautifulSoup
import requests




os.environ['PATH'] += r"/Users/raj/Documents/Python/chromedriver_mac64"
driver = webdriver.Chrome()
driver.get("https://monkeytype.com")
driver.maximize_window()

driver.implicitly_wait(10)
time.sleep(2)
words = driver.find_element(By.ID, "typingTest")
l = []
l = words.text
l = l.replace("english", "", 1)
l = l.split()
nl=len(l)-1
def convert(l):
    return ' '.join(l)


t_end=time.time()+30
while t_end >= time.time():
    w=convert(l)
    print(w)
    pyautogui.typewrite(w)
    pyautogui.typewrite(" ")
    words = driver.find_element(By.ID, "typingTest")
    a = words.text
    a = a.split()
    # print(l)
    n = len(a)-1
    j = 0
    while a[n - j] != l[nl] and a[n - j - 1] != l[nl - 1] and n-j>=0 and n-j-1>=0 :
        j+= 1
    l = a[n - j + 1:]
    nl = len(l) - 1

# print(l)
# print(n)

#i = 0

# pyautogui.typewrite('\n')
time.sleep(10)

driver.quit()
