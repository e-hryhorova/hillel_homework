import json
import logging
import pathlib
import requests


current_dir = pathlib.Path(__file__).parent
file_name = 'test_data.json'
file_name = current_dir.joinpath(file_name)
# create logger
logger = logging.getLogger('Name_of_Logger')
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug

file_handler = logging.FileHandler("logging_api.log")
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handler
file_handler.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(file_handler)


class TestSuit:
    with open(file_name, "r") as f:
        testing_data = json.load(f)

    save_url = []

    def test_user_can_create_valid_new_user(self):
        url = f"{self.testing_data['urls']['main']}{self.testing_data['urls']['users']}"
        user = 'admin'
        password = self.testing_data['users']['admin']
        data = {
            "username": "evgeniya",
            "email": "22@email.com",
            "groups": []
        }
        resp_create_user = requests.post(url, data, auth=(user, password))
        user_url = resp_create_user.json()['url']
        self.save_url.append(user_url)
        assert resp_create_user.status_code == 201, logger.error(
            f"create user response returns {resp_create_user.status_code}")
        created_user_data = requests.get(user_url, data, auth=(user, password))
        assert created_user_data.status_code == 200
        assert created_user_data.json()["username"] == data["username"]
        assert created_user_data.json()["email"] == data["email"]
        logger.info(f'New user {data["username"]} is created as expected')

    def test_user_can_update_user_info(self):
        user = 'admin'
        password = self.testing_data['users']['admin']
        update_data = {
            "username": "evg_hr",
            "email": "test@email.com",
            "groups": []
        }
        resp_update_user = requests.put(self.save_url[0], update_data, auth=(user, password))
        assert resp_update_user.status_code == 200
        created_user_data = requests.get(self.save_url[0], auth=(user, password))
        assert created_user_data.status_code == 200
        assert created_user_data.json()["username"] == update_data["username"]
        assert created_user_data.json()["email"] == update_data["email"]
        logger.info(f'User data is updated successfully')

    def test_user_can_delete_user(self):
        user = 'admin'
        password = self.testing_data['users']['admin']
        resp_delete_user = requests.delete(self.save_url[0], auth=(user, password))
        assert resp_delete_user.status_code == 204, logger.error(
            f"delete user response returns {resp_delete_user.status_code}")
        logger.info(f'User is deleted successfully')
