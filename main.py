import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui
os.environ['PATH'] += r"/Users/raj/Documents/Python/chromedriver_mac64"
driver = webdriver.Chrome()
driver.get("https://monkeytype.com")
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(2)
reject = driver.find_element(By.CLASS_NAME, "rejectAll")
reject.click()
words = driver.find_element(By.ID, "typingTest")
l = []
l = words.text
l = l.replace("english", "", 1)
l = l.split()
nl = len(l) - 1
def convert(l):
    return ' '.join(l)
t_end = time.time() + 30
while t_end >= time.time():
    w = convert(l)
    pyautogui.typewrite(w)
    pyautogui.typewrite(" ")
    words = driver.find_element(By.ID, "typingTest")
    a = words.text
    a = a.split()
    n = len(a) - 1
    j = 0
    while n - j >= 0 and n - j - 1 >= 0 and n - j - 2 >= 0 and nl - 2 >= 0:
        if a[n - j] == l[nl] and a[n - j - 1] == l[nl - 1] and a[n - j - 2] == l[nl - 2]:
            break
        j += 1
    l = a[n - j + 1:]
    nl = len(l) - 1
time.sleep(10)
driver.quit()
