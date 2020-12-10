from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get("https://selenium-python.readthedocs.io/locating-elements.html")

login_link = browser.find_element_by_xpath('''/html/body/div[1]/div[2]/div/ul/li[5]''')
login_link.click()

sleep(20)

browser.close()