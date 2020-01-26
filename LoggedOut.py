from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.XPATH, "//span[contains(text(),'& Orders')]")

# click orders
driver.find_element(By.XPATH, "//span[contains(text(),'& Orders')]").click()

# verify
assert 'Sign-In' in driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text


sleep(2)
driver.quit()