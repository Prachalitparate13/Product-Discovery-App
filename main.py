from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# AMAZON SEARCH

driver = webdriver.Chrome()
driver.get('https://www.amazon.in')
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('coconut cooking oil ')
button = driver.find_element(By.ID, 'nav-search-submit-button')
button.click()
for element in driver.find_elements(By.TAG_NAME, 'h2'):
    elements = element.find_elements(By.TAG_NAME, 'a')
    for e in elements:
        print(e.get_attribute('href'))


# BIG BASKET SEARCH

driver = webdriver.Chrome()
driver.get('https://www.bigbasket.com/')
search = driver.find_element(By.ID, 'input')
search.send_keys(product_name)
button = driver.find_element(By.CLASS_NAME, 'input-group-btn')
button.click()
for element in driver.find_elements(By.CLASS_NAME, 'prod-name'):
    elements = element.find_elements(By.TAG_NAME, 'a')
    for e in elements:
        print(e.get_attribute('href'))

# FLIPKART SEARCH
driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/')
# closing the login page
button = driver.find_element(By.CLASS_NAME, '_2doB4z')
button.click()
search = driver.find_element(By.CLASS_NAME, '_3704LK')
search.send_keys(product_name)
button = driver.find_element(By.CLASS_NAME, 'L0Z3Pu')
button.click()
for element in driver.find_elements(By.CLASS_NAME, '_4ddWXP'):
    elements = element.find_elements(By.TAG_NAME, 'a')
    for e in elements:
        print(e.get_attribute('href'))

#AMAZON SEARCH FUCTION(RUNS WELL)
def Amazon_Search(product_name):
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.in')
    search=driver.find_element(By.ID,'twotabsearchtextbox')
    search.send_keys(product_name)
    button=driver.find_element(By.ID,'nav-search-submit-button')
    button.click()  
    for element in driver.find_elements(By.TAG_NAME,'h2'):
        elements = element.find_elements(By.TAG_NAME, 'a')
        for e in elements:
            print(e.get_attribute('href'))

#BIG BASKET SEARCH FUCTION (GETTING PROBLEM)
def Big_Basket_Search(product_name):
    driver = webdriver.Chrome()
    driver.get('https://www.bigbasket.com/')
    search=driver.find_element(By.ID,'input')
    search.send_keys(product_name)
    button=driver.find_element(By.CLASS_NAME,'input-group-btn')
    button.click()
    for element in driver.find_elements(By.CLASS_NAME,'prod-name'):
        elements = element.find_elements(By.TAG_NAME, 'a')
        for e in elements:
            print(e.get_attribute('href'))

#FLIPKART SEARCH FUNCTION(SAME PROBLEM AS BIGBASKET)
def Flipkart_Search(product_name):
    driver = webdriver.Chrome()
    driver.get('https://www.flipkart.com/')
    #closing the login page
    button=driver.find_element(By.CLASS_NAME,'_2doB4z')
    button.click()
    search=driver.find_element(By.CLASS_NAME,'_3704LK')
    search.send_keys(product_name)
    button=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
    button.click()
    for element in driver.find_elements(By.CLASS_NAME,'_4ddWXP'):
        elements = element.find_elements(By.TAG_NAME, 'a')
        for e in elements:
            print(e.get_attribute('href'))