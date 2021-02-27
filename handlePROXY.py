from selenium import webdriver
import time
PROXY="23.23.23.23:3128"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome("C:\\Users\\AAA\\gekodriver browsers drivers\\chromedriver.exe",options=chrome_options)
chrome.get('https://www.instagram.com/')
time.sleep(3)
chrome.close()