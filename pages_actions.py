from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging


BASE_URL = 'https://www.aqa.science/admin'


class PagesActions:

    logging.basicConfig(filename='testing.log', level=logging.DEBUG)
    LOGGER = logging.getLogger()

    @staticmethod
    def login_to_app(driver: webdriver, user: str, password: str):
        try:
            driver.get(BASE_URL)
            username_field = driver.find_element(By.XPATH, '//*[@id="id_username"]')
            username_field.send_keys(user)
            password_field = driver.find_element(By.XPATH, "//*[@id='id_password']")
            password_field.send_keys(password)
            submit_login_button = driver.find_element(By.XPATH, "//input[@type='submit'][@value='Log in']")
            submit_login_button.click()
            logging.info('seems login is ok')
        except():
            logging.error('something went wrong')

    @staticmethod
    def move_to_add_user_window_after_login(driver: webdriver):
        try:
            users_table = driver.find_element(By.XPATH, '//*[text()="Users"]').click()
            add_user = driver.find_element(By.XPATH, "//*[@id='content-main']/ul/li/a").click()
            header_add_user_window = driver.find_element(By.XPATH, '//*[text()="Add user"]')
            assert header_add_user_window.text == 'Add user'
        except():
            logging.error('add user window is not opened')
            return False

    @staticmethod
    def update_user_info(driver: webdriver, update_user_name: str, first_name: str, last_name: str, email: str):
        try:
            driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
            driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys(update_user_name)
            driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys(first_name)
            driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys(last_name)
            driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys(email)
            driver.find_element(By.XPATH, '//*[@id="id_is_staff"]').click()
            driver.find_element(By.XPATH, '//*[@id="user_form"]/div/div/input[1]').click()
            logging.info('new data sent successfully')
        except():
            logging.error('new data is not set')
            return False

    @staticmethod
    def validate_user_not_in_users_table(driver: webdriver, user_name):
        try:
            table = driver.find_element(By.XPATH, '//*[@id="result_list"]')
            table_values = table.text
            assert user_name not in table_values
        except():
            logging.error('user exists')
            return False
