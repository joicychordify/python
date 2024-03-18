from selenium import webdriver
driver =webdriver.Chrome()

driver.get('https://reditum.ec/users/sign_in')
driver.maximize_window()
print(driver.title)
driver.close()
