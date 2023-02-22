import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.find_element(By.LINK_TEXT, "LOGIN").click()
time.sleep(3)

captcha = (driver.find_element('xpath', "//span[@class='ng-star-inserted']//img[@class='captcha-img']")).copy()
input_cap = driver.find_element('xpath', "//input[@id='captcha']")
input_cap.send_keys(captcha)
time.sleep(3)


# //span[@class='ng-star-inserted']//img[@class='captcha-img']