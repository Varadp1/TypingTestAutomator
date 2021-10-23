from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import string
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://10fastfingers.com/advanced-typing-test/english")

input("Please clear all the cookie mess.")
    
row = driver.find_element(By.ID, "row1")
wordsTemp = row.find_elements(By.TAG_NAME, 'span')

bar = driver.find_element(By.ID, "inputfield")

for i in range(len(wordsTemp)):
    word = row.find_elements(By.CLASS_NAME, 'highlight')
    bar.send_keys(word[0].text + Keys.SPACE)

for char in string.ascii_lowercase + string.ascii_uppercase:
    bar.send_keys(char)
    time.sleep(1)

input("Done?")

driver.quit()