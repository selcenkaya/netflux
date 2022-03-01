# Empty Input Fields and their various combinations

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def checkInputs( textField, passwordField, errors ):
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
    driver.find_element(By.CLASS_NAME, "logo").click() # for errors to show

    for id in errors:
        err = driver.find_element(By.ID, id).text
        assert err != ""

    time.sleep(3)
    driver.close()


# empty email+phone / full password
text1 = ""
password1 = "teftiş"
errors1 = ["text-error"]
checkInputs( text1, password1, errors1 )

# full email+phone / empty password
text2 = "123456789"
password2 = ""
errors2 = ["pass-error"]
checkInputs( text2, password2, errors2 )

# empty email+phone / empty password
text3 = ""
password3 = ""
errors3 = ["text-error", "pass-error"]
checkInputs( text3, password3, errors3 )

print( "THE END" )