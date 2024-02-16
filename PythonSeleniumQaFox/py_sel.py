"""
https://www.youtube.com/playlist?list=PLsjUcU8CQXGEe8D7ZVJnANklJEHeqjBul
https://omayo.blogspot.com/
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://omayo.blogspot.com/"
IMPLICIT_WAIT = 30
SLEEP_FOR = 0


def sleep(sleep_time):
    time.sleep(sleep_time)


try:
    print("--- Test started ---")
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)
    time.sleep(SLEEP_FOR)

    text_content = driver.find_element(By.ID, "pah")
    print(f"Text content is:", text_content.text)

    page_title = driver.title
    print("Title of the page is:", page_title)

    page_url = driver.current_url
    print("Page URL is:", page_url)

    driver.find_element(By.LINK_TEXT, "Open a popup window").click()
    print("A new pop-up window opened.")
    print("Page title after pop-up window open:", driver.title)
    sleep(3)

except Exception as e:
    print("Error occurred while running tests:", e)
finally:
    driver.quit()
    # driver.close()
    print("--- Test finished ---")
