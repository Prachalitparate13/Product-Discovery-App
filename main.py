#AMAZON SEARCH
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://www.amazon.in')
search=driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys('coconut cooking oil ')
button=driver.find_element(By.ID,'nav-search-submit-button')
button.click()
for element in driver.find_elements(By.TAG_NAME,'h2'):
    elements = element.find_elements(By.TAG_NAME, 'a')
    for e in elements:
        print(e.get_attribute('href'))
     


