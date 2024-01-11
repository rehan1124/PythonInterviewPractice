from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demo.automationtesting.in/Windows.html"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(URL)

driver.find_element(By.CSS_SELECTOR, "[id='Tabbed'] button[class='btn btn-info']").click()

handles = driver.window_handles
print("Windows opened:", handles)
for items in handles:
    driver.switch_to.window(items)
    print(driver.title)
