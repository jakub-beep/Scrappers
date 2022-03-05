import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import data_generator
import time



if __name__ == "__main__":

    login = data_generator.password_generator(10)
    password = data_generator.password_generator(11)
    email = data_generator.password_generator(6) + '@gmail.com'
    print(login, password, email)

    os.environ['PATH'] += r'C:\Users\User\Desktop\my_way_to_code\21_scrapper'
    driver = webdriver.Chrome()

    driver.get('https://www.plemiona.pl/')
    print(driver.title)

    registration = driver.find_element(By.XPATH, "//*[contains(text(), 'Bezpłatna rejestracja!')]").click()
    waiting = time.sleep(3)

    login_textfield = driver.find_element(By.ID, value='register_username')
    login_textfield.send_keys(login)

    password_textfield = driver.find_element(By.ID, value='register_password')
    password_textfield.send_keys(password)

    email_textfield = driver.find_element(By.ID, value='register_email')
    email_textfield.send_keys(email)

    checkbox_regulations = driver.find_element(By.ID, value='terms').click()
    create_account_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Stwórz konto')]").click()

    time.sleep(5)

else:
    login = 'otaaak'
    password = 'Y@GD6cZqqZ3!b9h'
    print(login, password)

# how to pass bot testing!


# world_button = driver.find_element(By.CLASS_NAME, value='world_button_active')
# world_button.click()
#
# time.sleep(5)

