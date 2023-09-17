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
l=[]
l=words.text
l = l.replace("english", "", 1)
l=l.split()
print(l)
t_end = time.time() + 30
word = l[0]
i = 0
n = len(l)-1
print(n)
while t_end >= time.time():
    pyautogui.typewrite(word, interval=0.000001)
    pyautogui.typewrite(" ", interval=0.000001)
    i += 1
    if i == n:
        print('enytr at=' + str(i))
        words = driver.find_element(By.ID, "typingTest")
        l=words.text
        l=l.split()
        print(l)
        n = len(l) - 1
        j=0
        while l[n-j] != word:
            j+= 1
        l= l[n - j+1:]
        n = len(l) - 1
        print(l)
        print(n)
        i=0
    word = l[i]

pyautogui.typewrite('\n')


time.sleep(5)

driver.quit()




