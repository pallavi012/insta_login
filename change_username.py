from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome("C:\\Users\\AAA\\gekodriver browsers drivers\\chromedriver.exe")
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

#---------------------Login page--------------------------
login_link = browser.find_element_by_id("react-root")
login_link.click()
sleep(2)
list_of_username=['update_pass1','update_pass2']
password='SOFT_GOWAY123'
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
for i in list_of_username:
    username_input.send_keys(i)
    password_input.send_keys(password)
    break
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

#---------------------Feed page--------------------------
profile = browser.find_element_by_class_name("_6q-tv")
sleep(2)
profile.click()
x = browser.find_element_by_class_name("-qQT3")
sleep(2)
x.click()

#---------------------profile page-------------------------
edit_profile = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/a")
sleep(2)
edit_profile.click()
user =browser.find_element_by_id("pepUsername").clear()
sleep(2)
user=browser.find_element_by_id("pepUsername").send_keys("update_pass1")
sleep(2)
sub=browser.find_element_by_class_name("L3NKy")
sub.click()




sleep(30)
browser.close()