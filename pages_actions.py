from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging


BASE_URL = 'https://www.aqa.science/admin'

# create logger
logger = logging.getLogger('Test_ui_crude')
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug
file_handler = logging.FileHandler("logging_ui.log")
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handler
file_handler.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(file_handler)


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
            logger.info('seems login is ok')
        except():
            logger.error('something went wrong')

    @staticmethod
    def move_to_add_user_window_after_login(driver: webdriver):
        try:
            users_table = driver.find_element(By.XPATH, '//*[text()="Users"]').click()
            add_user = driver.find_element(By.XPATH, "//*[@id='content-main']/ul/li/a").click()
            header_add_user_window = driver.find_element(By.XPATH, '//*[text()="Add user"]')
            assert header_add_user_window.text == 'Add user'
        except():
            logger.error('add user window is not opened')
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
            logger.info('new data sent successfully')
        except():
            logger.error('new data is not set')
            return False

    @staticmethod
    def validate_user_not_in_users_table(driver: webdriver, user_name):
        try:
            table = driver.find_element(By.XPATH, '//*[@id="result_list"]')
            table_values = table.text
            assert user_name not in table_values
        except():
            logger.error('user exists')
            return False
