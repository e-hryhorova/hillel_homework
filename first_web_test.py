from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(' --ignore-ssl-errors-yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
url = 'https://www.work.ua/'
driver.get(url)
search_vacation = 'Manager'
search_field = driver.find_element(By.XPATH, '//*[@id="search"]')
search_field.send_keys(search_vacation)
button = driver.find_element(By.ID, 'sm-but')
button.click()
reference_element = driver.find_element(By.XPATH, '//*[@id="pjax-job-list"]/div[1]/div[2]/div[1]/h1')
assert search_vacation in reference_element.text
