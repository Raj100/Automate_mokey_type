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

# assign URL
url = "https://monkeytype.com/"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "html.parser")

text= soup.find('typingTest')
print(text)
os.environ['PATH'] += r"/Users/raj/Documents/Python/chromedriver_mac64"
driver = webdriver.Chrome()
driver.get("https://monkeytype.com")
driver.maximize_window()
"""
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
except:
    driver.quit()
"""
driver.implicitly_wait(10)
"""
reject = driver.find_element(By.__class__, 'button_rejectAll')
reject.click()
"""

words = driver.find_element(By.ID, "typingTest")
a=[]
l=words.text
a = a.replace("english", "", 1)
l=l.split()
print(l)
t_end = time.time() + 30
for word in l:
    pyautogui.typewrite(word, interval=0.1)
    pyautogui.typewrite(" ", interval=0.1)
    if t_end <= time.time():
        break
pyautogui.typewrite('\n')


time.sleep(5)
print(driver.title)

driver.quit()




