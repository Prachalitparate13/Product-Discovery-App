import requests
from bs4 import BeautifulSoup

#def Search(Product_Name,Location=""):
#    url="https://www.google.com/search?q="+Product_Name+",%20"+Location
#    source=requests.get(url)
#    soup=BeautifulSoup(source.text,'html')
#   links=soup.find_all('a') 
#    print(links)

#First way gives all href
url="https://www.google.com/search?q=Addidas-Superstar,%20Pune"
source=requests.get(url)
soup=BeautifulSoup(source.text,'html.parser')
#links=soup.find_all('div',class_="yuRUbf")
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    linkText =link.get('href')
    all_links.add(link)
    print(linkText)


#Second Way (problem not getting the text from that tag)
from selenium import webdriver
url="https://www.google.com/search?q=Addidas-Superstar,%20Pune"
driver=webdriver.Chrome('C:/Users/owner/OneDrive/Desktop/Python/project/KernalPI/chromedriver_win32/chromedriver')
driver.get(url)
from selenium.webdriver.common.by import By
results=driver.find_elements(by=By.CLASS_NAME,value='g tF2Cxc')
for links in results:
    name=links.find_element(By.CLASS_NAME,"iUh30 qLRx3b tjvcx")
    print(name)
    print("................")

#OR
from selenium.webdriver.common.by import By
results=driver.find_elements(by=By.CLASS_NAME,value='TbwUpd NJjxre')
print(results)


#Third way (problem not getting the text from that tag showing empty)
import requests
from bs4 import BeautifulSoup
url="https://www.google.com/search?q=Addidas-Superstar,%20Pune"
source=requests.get(url)
soup=BeautifulSoup(source.text,'html.parser')
temp = soup.find_all("div",class_="yuRUbf")
    
print( temp ) 