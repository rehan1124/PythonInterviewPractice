from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.irctc.co.in/nget/train-search"

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options)

try:
    # Driver navigations
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)

    # Clicking on `Register` button
    driver.find_element(By.XPATH, "//*[contains(text(), 'REGISTER')]").click()

    # Entering details
    driver.find_element(By.ID, "userName").send_keys("Rehan")
    driver.find_element(By.ID, "usrPwd").send_keys("Password")
    driver.find_element(By.ID, "cnfUsrPwd").send_keys("cnfUsrPwd")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Preferred Language')]").click()
    driver.find_element(By.XPATH, "//ul[@role='listbox']//li//*[text()='English']").click()

    driver.find_element(By.XPATH, "//span[text()='Security Question']").click()
    driver.find_element(By.XPATH, "//ul//li//*[text()='What is your pet name?']").click()
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Security Answer']").send_keys("Pigeon")

    # Clicking on `Continue` button
    driver.find_element(By.CSS_SELECTOR, "button[label='Continue']").click()

    print("--- Test ended ---")

except Exception as e:
    print(e)
finally:
    driver.quit()
