from selenium import webdriver

import Config

driver=webdriver.Chrome(executable_path="D:\Tools\Python\Driver\Chrome\chromedriver.exe")
driver.get("https://tejira.tataelxsi.co.in/login.jsp")
driver.implicitly_wait(15)

#Login

username=driver.find_element_by_name("os_username")
username.send_keys(Config.loginidStr)
password=driver.find_element_by_name("os_password")
password.send_keys(Config.passwordStr)
driver.find_element_by_name("login").click()

PageTitle=driver.title
print(PageTitle)
