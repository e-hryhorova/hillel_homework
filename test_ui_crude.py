import logging
import os
import pathlib

import yaml
from selenium.webdriver.common.by import By

from pages_actions import PagesActions

current_dir = pathlib.Path(__file__).parent
file_name = 'test_data.jaml'
file_name = current_dir.joinpath(file_name)

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

pa = PagesActions()

os.system("docker run -d --name schr -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug")


class TestSuite:
    testing_data = yaml.safe_load(open("test_data.yaml"))

    def test_user_not_exist(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        driver_init.find_element(By.XPATH, '//*[text()="Users"]').click()
        pa.validate_user_not_in_users_table(driver_init, self.testing_data['new_user_name']['correct_name'])
        logger.info(f"User with the name {self.testing_data['new_user_name']['correct_name']} doesn't exist")

    def test_user_can_create_valid_new_user(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        pa.move_to_add_user_window_after_login(driver_init)
        input_user = driver_init.find_element(By.XPATH, "//*[@id='id_username']")
        input_user.send_keys(self.testing_data['new_user_name']['correct_name'])
        input_password = driver_init.find_element(By.XPATH, "//*[@id='id_password1']")
        input_password.send_keys(self.testing_data['new_user_password']['correct_password'])
        input_conf_password = driver_init.find_element(By.XPATH, "//*[@id='id_password2']")
        input_conf_password.send_keys(self.testing_data['password_confirm']['cpassword_5'])
        save = driver_init.find_element(By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
        save.click()
        message = driver_init.find_element(By.XPATH, '//*[@id="main"]/div/ul/li')
        assert self.testing_data['new_user_name']['correct_name'] in message.text, logger.error(
            'something wrong, user is not displayed in message')
        logger.info('message about user creation is displayed')

    def test_error_message_with_empty_all_required_fields(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        pa.move_to_add_user_window_after_login(driver_init)
        save = driver_init.find_element(By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
        save.click()
        error_message = driver_init.find_element(By.XPATH, '//*[@id="user_form"]/div/p')
        assert 'Please correct the errors below' in error_message.text, logger.error('no error message appears')
        logger.info('error message appears')

    def test_get_error_with_mismatch_password_and_confirm_password(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        pa.move_to_add_user_window_after_login(driver_init)
        input_user = driver_init.find_element(By.XPATH, "//*[@id='id_username']")
        input_user.send_keys(self.testing_data['new_user_name']['correct_name'])
        input_password = driver_init.find_element(By.XPATH, "//*[@id='id_password1']")
        input_password.send_keys(self.testing_data['new_user_password']['correct_password'])
        input_conf_password = driver_init.find_element(By.XPATH, "//*[@id='id_password2']")
        input_conf_password.send_keys(self.testing_data['password_confirm']['cpassword_2'])
        save = driver_init.find_element(By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
        save.click()
        error_message_password_field = driver_init.find_element(By.XPATH,
                                                                '//*[@id="user_form"]/div/fieldset/div[3]/ul/li')
        assert 'The two password fields didn’t match' in error_message_password_field.text, logger.error(
            'no error message appears')
        logger.info('error message appears')

    def test_error_message_with_invalid_password(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        pa.move_to_add_user_window_after_login(driver_init)
        clear_password_input_box = driver_init.find_element(By.XPATH, "//*[@id='id_password1']")
        clear_password_input_box.clear()
        clear_password_confirm_input_box = driver_init.find_element(By.XPATH, "//*[@id='id_password2']")
        clear_password_confirm_input_box.clear()
        input_user = driver_init.find_element(By.XPATH, "//*[@id='id_username']")
        input_user.send_keys(self.testing_data['new_user_name']['correct_name'])
        input_password = driver_init.find_element(By.XPATH, "//*[@id='id_password1']")
        input_password.send_keys(self.testing_data['new_user_password']['password_2'])
        input_conf_password = driver_init.find_element(By.XPATH, "//*[@id='id_password2']")
        input_conf_password.send_keys(self.testing_data['password_confirm']['cpassword_2'])
        save = driver_init.find_element(By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
        save.click()
        error_message_password_field = driver_init.find_element(By.XPATH,
                                                                '//*[@id="user_form"]/div/fieldset/div[3]/ul/li')
        assert 'This password is too short. It must contain at least 8 characters' in error_message_password_field.text, \
            logger.error('no error message appears')
        logger.info('error message appears')

    def test_created_user_is_in_users_table(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        navigate_to_users_table = driver_init.find_element(By.XPATH, '//*[text()="Users"]').click()
        user_name = self.testing_data['new_user_name']['correct_name']
        user_row = driver_init.find_element(By.XPATH, f'//tbody/tr[th[a[text()="{user_name}"]]]')
        assert user_name in user_row.text, logger.error('created user is not found in the users table')
        logger.info('created user is displayed in users table')

    def test_user_can_update_user_info(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        navigate_to_users_table = driver_init.find_element(By.XPATH, '//*[text()="Users"]').click()
        user_name = self.testing_data['new_user_name']['correct_name']
        user_name_in_users_table = driver_init.find_element(By.XPATH, f'//*[text()="{user_name}"]').click()
        pa.update_user_info(driver_init, self.testing_data['update']['update_user'],
                            self.testing_data['update']['update_first_name'],
                            self.testing_data['update']['update_last_name'],
                            self.testing_data['update']['update_email'])
        logger.info('new name, last name and email of user were inputted in the text boxes')

    def test_user_info_is_updated(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        driver_init.find_element(By.XPATH, '//*[text()="Users"]').click()
        user_name = self.testing_data['update']['update_user']
        first_name = self.testing_data['update']['update_first_name']
        last_name = self.testing_data['update']['update_last_name']
        email = self.testing_data['update']['update_email']
        user_name_actual = driver_init.find_element(By.XPATH, f'//tbody/tr[th[a[text()="{user_name}"]]]/th')
        assert user_name == user_name_actual.text
        logger.info('user name is updated')
        first_name_actual = driver_init.find_element(By.XPATH, f'//tbody/tr[th[a[text()="{user_name}"]]]/td[3]')
        assert first_name == first_name_actual.text
        logger.info('first name is updated')
        last_name_actual = driver_init.find_element(By.XPATH, f'//tbody/tr[th[a[text()="{user_name}"]]]/td[4]')
        assert last_name == last_name_actual.text
        logger.info('last_name is updated')
        email_actual = driver_init.find_element(By.XPATH, f'//tbody/tr[th[a[text()="{user_name}"]]]/td[2]')
        assert email == email_actual.text, logger.error('email is not updated properly')
        logger.info('email is updated')

    def test_user_can_delete_user(self, driver_init):
        pa.login_to_app(driver_init, self.testing_data['user'], self.testing_data['password'])
        user_name = self.testing_data['update']['update_user']
        user_name_in_users_table = driver_init.find_element(By.XPATH, f'//*[text()="{user_name}"]').click()
        driver_init.find_element(By.XPATH, '//*[text()="Delete"]').click()
        driver_init.find_element(By.XPATH, '//*[@id="content"]/form/div/input[2]').click()
        pa.validate_user_not_in_users_table(driver_init, self.testing_data['update']['update_user'])
        logger.info('user is deleted')
