import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.salesforce.com/in/")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "hgf-button").click()
time.sleep(3)
driver.close()
