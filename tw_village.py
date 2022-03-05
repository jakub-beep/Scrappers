import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import data_generator
import time
import tw_register

os.environ['PATH'] += r'C:\Users\User\Desktop\my_way_to_code\21_scrapper'
driver = webdriver.Chrome()

# logging
driver.get('https://www.plemiona.pl/')
print(driver.title)
user_name = driver.find_element(By.ID, value='user')
user_name.send_keys(tw_register.login)
password = driver.find_element(By.ID, value='password')
password.send_keys(tw_register.password)
signing = driver.find_element(By.CLASS_NAME, value='btn-login')
signing.click()
time.sleep(20)

# village building
building_src = "main_buildlink_"
# townhall accessing
townhall = driver.find_element(By.TAG_NAME, value='area').click()

# townhall
townhall_build_2 = driver.find_element(By.ID, value=building_src + "main_2").click()
time.sleep(5)
townhall_build_3 = driver.find_element(By.ID, value=building_src + "main_3").click()
time.sleep(5)
townhall_build_4 = driver.find_element(By.ID, value=building_src + "main_4").click()
time.sleep(300)
townhall_build_5 = driver.find_element(By.ID, value=building_src + "main_5").click()
time.sleep(450)

# sawmill
sawmill_build_1 = driver.find_element(By.ID, value=building_src + "_wood_1").click()
sawmill_build_2 = driver.find_element(By.ID, value=building_src + "_wood_2").click()
time.sleep(300)

# brickyard
brickyard_build_1 = driver.find_element(By.ID, value=building_src + "_stone_1").click()
brickyard_build_2 = driver.find_element(By.ID, value=building_src + "_stone_2").click()
time.sleep(300)

# ironworks
brickyard_build_1 = driver.find_element(By.ID, value=building_src + "_stone_1").click()
brickyard_build_2 = driver.find_element(By.ID, value=building_src + "_stone_2").click()
time.sleep(300)

#
# townhall_icon = driver.find_element(By.CLASS_NAME, value='visual-building visual-building-main1 quest-arrow-target')
# world_button.click()
