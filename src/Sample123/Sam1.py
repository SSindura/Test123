'''
Created on Jul 12, 2017

@author: Sindura
'''
from selenium import webdriver
'''
NOT NEEDED ANYMORE
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

ff_binary=FirefoxBinary('/usr/bin/firefox')
#C:\\Users\\Sindura\\Downloads\\geckodriver-v0.17.0-win64\\geckodriver.exe
'''


'''driver = webdriver.Ie("C:\\Python27\\Drivers\\IEDriverServer.exe")
driver=webdriver.Chrome("C:\\Python27\\Drivers\\chromedriver.exe")
'''
#driver=webdriver.Firefox("C:\\Python27\\Drivers\\geckodriver.exe")
driver=webdriver.Firefox()
driver.maximize_window()

driver.get("http://www.python.org")
assert "Python" in driver.title
ele=driver.find_element_by_id('id-search-field')
ele.clear()
ele.send_keys('python')
driver.find_element_by_id('submit').click()
ele1=driver.find_element_by_link_text('Python Events Calendar')
ele1.click()
assert "Problem loading page" in driver.title
driver.close()



