from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('Cancel order')
sleep(1)

# click search
driver.find_element(By.XPATH, "//span[@id='helpSearchSubmit']").click()

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]").text
sleep(2)
driver.quit()

