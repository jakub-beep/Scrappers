import os

import time
import data_generator
import requests
import websockets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r'C:\Users\User\Desktop\my_way_to_code\21_scrapper'
driver = webdriver.Chrome()

driver.get('https://www.plemiona.pl/')
print(driver.title)

registration = driver.find_element(By.XPATH, "//*[contains(text(), 'Bezpłatna rejestracja!')]")
registration.click()
waiting = time.sleep(3)

login = data_generator.password_generator(10)
password = data_generator.password_generator(11)
email = data_generator.password_generator(6) + '@gmail.com'

login_textfield = driver.find_element(By.ID, value='register_username')
login_textfield.send_keys(login)

password_textfield = driver.find_element(By.ID, value='register_password')
password_textfield.send_keys(password)

email_textfield = driver.find_element(By.ID, value='register_email')
email_textfield.send_keys(email)

checkbox_regulations = driver.find_element(By.ID, value='terms')
checkbox_regulations.click()

create_account_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Stwórz konto')]")
create_account_button.click()
# driver.quit()
