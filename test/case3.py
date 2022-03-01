# Login With Facebook

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# set up driver
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://selcenkaya.github.io/netflux/index.html")
driver.maximize_window()
time.sleep(3)

window_before = driver.window_handles[0]

# locate facebook button
button = driver.find_element(By.ID, "fb-btn")
button.click()
time.sleep(5)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

email = "kolsonpmjimyobrogp@nvhrw.com"
password = "şifre123"

email2 = driver.find_element(By.ID, "email")
password2 = driver.find_element(By.ID, "pass")
button2 = driver.find_element(By.ID, "loginbutton")

email2.send_keys(email)
password2.send_keys(password)
button2.click()

time.sleep(5)
driver.close()

driver.switch_to.window(window_before)

expectedURL = "https://selcenkaya.github.io/netflux/home.html"
actualURL = driver.current_url
assert expectedURL == actualURL

displayedText = driver.find_element(By.ID, "user").text
assert email == displayedText

driver.close()
print( "THE END" )