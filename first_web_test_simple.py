from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('E:\selenium\chromedriver.exe')
url = 'https://www.work.ua/'
driver.get(url)
search_vacation = 'Project manager'
search_field = driver.find_element(By.XPATH, '//*[@id="search"]')
search_field.send_keys(search_vacation)
button = driver.find_element(By.ID, 'sm-but')
button.click()
reference_element = driver.find_element(By.XPATH, '//*[@id="pjax-job-list"]/div[1]/div[2]/div[1]/h1')
assert search_vacation in reference_element.text, 'such vacation is not found'
driver.close()
