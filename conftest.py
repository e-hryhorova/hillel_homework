import subprocess

from selenium import webdriver

import pytest


# @pytest.fixture(scope='module')
# def docker():
#     subprocess.run("docker run -d --name schr -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug", shell=True,
#                    check=True)
#     yield
#     subprocess.run("docker rm -f schr", shell=True, check=True)


@pytest.fixture(scope='function')
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
    yield driver
    driver.quit()



