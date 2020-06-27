from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser= webdriver.Firefox()
browser.get('https://play2048.co/')

htmlElem=browser.find_element_by_tag_name('html')
n=0
while (n==0):
    htmlElem.send_keys(Keys.UP) 
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)