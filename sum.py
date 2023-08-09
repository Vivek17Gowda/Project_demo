import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
# extracting texts from the categories block in demo webshop

driver.get("https://demowebshop.tricentis.com/")
categories = driver.find_elements("xpath", '(//ul[@class="list"])[1]//a')

print(categories)  # list of webelements

for category in categories:
    print(category)  # webelement
    print(category.text)