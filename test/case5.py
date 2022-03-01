# Other Functionalities such as Remember Me, Sign In Button Disable and Logout after logging in

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def logout( textField, passwordField, expectedURL ):
    # set up driver
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.get("https://selcenkaya.github.io/netflux/index.html")
    driver.maximize_window()
    time.sleep(3)

    # locate input fields
    text = driver.find_element(By.ID, "id-email-phone")
    password = driver.find_element(By.ID, "id-password")
    button = driver.find_element(By.ID, "signin-button")

    text.send_keys(textField)
    password.send_keys(passwordField)
    button.click()
    time.sleep(3)

    # click logout button
    button2 = driver.find_element_by_xpath('//a[@href="index.html"]')
    button2.click()
    
    time.sleep(3)
    actualURL = driver.current_url
    assert expectedURL == actualURL

    driver.close()


# empty email+phone / full password
text1 = "test1@test.test"
password1 = "test1"
expectedURL1 = "https://selcenkaya.github.io/netflux/index.html"
logout( text1, password1, expectedURL1 )

print( "THE END" )