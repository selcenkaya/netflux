# Valid & Invalid Inputs to email/phone and password and their various combinations

from cmath import exp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def checkInputs( textField, passwordField, expectedURL, sameTextID, sameTextValue, errors ):
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

    time.sleep(3)
    if( expectedURL != "" ):
        actualURL = driver.current_url
        assert expectedURL == actualURL

    if( sameTextID != "" ):
        displayedText = driver.find_element(By.ID, sameTextID).text
        assert textField == displayedText
    
    if( sameTextValue != "" ):
        displayedValue = driver.find_element(By.ID, sameTextValue).get_attribute('value')
        assert textField == displayedValue

    for id in errors:
        err = driver.find_element(By.ID, id).text
        assert err != ""

    time.sleep(3)
    driver.close()


# valid email / valid password
text1 = "test1@test.test"
password1 = "test1"
expectedURL1 = "https://selcenkaya.github.io/netflux/home.html"
sameTextID1 = "user"
sameTextValue1 = ""
errors1 = []
checkInputs( text1, password1, expectedURL1, sameTextID1, sameTextValue1, errors1 )

# valid phone / valid password
text2 = "123456789"
password2 = "kralcık"
expectedURL2 = "https://selcenkaya.github.io/netflux/home.html"
sameTextID2 = "user"
sameTextValue2 = ""
errors2 = []
checkInputs( text2, password2, expectedURL2, sameTextID2, sameTextValue2, errors2 )

# valid email / invalid password
text3 = "panda@pan.da"
password3 = "panda"
expectedURL3 = "https://selcenkaya.github.io/netflux/index.html"
sameTextID3 = ""
sameTextValue3 = "id-email-phone"
errors3 = ["db-error"]
checkInputs( text3, password3, expectedURL3, sameTextID3, sameTextValue3, errors3 )

# valid phone / invalid password
text4 = "123456789"
password4 = "minik"
expectedURL4 = "https://selcenkaya.github.io/netflux/index.html"
sameTextID4 = ""
sameTextValue4 = "id-email-phone"
errors4 = ["db-error"]
checkInputs( text4, password4, expectedURL4, sameTextID4, sameTextValue4, errors4 )

# invalid email / valid password - not really logical but...
text5 = "aa" 
password5 = "PANDA"
expectedURL5 = "https://selcenkaya.github.io/netflux/index.html"
sameTextID5 = ""
sameTextValue5 = "id-email-phone"
errors5 = ["text-error"]
checkInputs( text5, password5, expectedURL5, sameTextID5, sameTextValue5, errors5 )

# invalid phone / valid password - not really logical but...
text6 = "123456789101112131415161718192021222324252627282930" 
password6 = "kralcık"
expectedURL6 = "https://selcenkaya.github.io/netflux/index.html"
sameTextID6 = ""
sameTextValue6 = "id-email-phone"
errors6 = ["text-error"]
checkInputs( text6, password6, expectedURL6, sameTextID6, sameTextValue6, errors6 )

# invalid email / invalid password
text7 = "abcdefg" 
password7 = "r"
expectedURL7 = "https://selcenkaya.github.io/netflux/index.html"
sameTextID7 = ""
sameTextValue7 = "id-email-phone"
errors7 = ["text-error", "pass-error"]
checkInputs( text7, password7, expectedURL7, sameTextID7, sameTextValue7, errors7 )

# invalid phone / invalid password
text8 = "00" 
password8 = "IWLEYBGIRWNFILwyebfınwefılubwlıfhuowenflUVYFIEQJALKCJKVYFWEIOJDPQŞLAXSKLDJSVI"
expectedURL8 = "https://selcenkaya.github.io/netflux/index.html"
sameTextID8 = ""
sameTextValue8 = "id-email-phone"
errors8 = ["text-error", "pass-error"]
checkInputs( text8, password8, expectedURL8, sameTextID8, sameTextValue8, errors8 )

print( "THE END" )