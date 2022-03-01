# Redirecting Functionalities

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def checkInputs( ref ):
    # set up driver
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.get("https://selcenkaya.github.io/netflux/index.html")
    driver.maximize_window()
    time.sleep(3)

    learnMore = driver.find_element(By.ID, "disappear")
    learnMore.click()
    link = driver.find_element_by_xpath('//a[@href="' + ref + '"]')
    link.click()

    driver.switch_to.window(driver.window_handles[1])

    actualURL = driver.current_url
    assert ref == actualURL

    time.sleep(3)
    driver.close()


# help
ref1 = "http://help.netflix.com/en/"
checkInputs( ref1 )

# sign up
ref2 = "https://www.netflix.com/tr-en/"
checkInputs( ref2 )

# google privacy
ref3 = "https://policies.google.com/privacy?hl=en"
checkInputs( ref3 )

# google terms
ref4 = "https://policies.google.com/terms?hl=en"
checkInputs( ref4 )

# faq
ref5 = "https://help.netflix.com/en/node/412"
checkInputs( ref5 )

# help center
ref6 = "https://help.netflix.com/en"
checkInputs( ref6 )

# terms of use
ref7 = "https://help.netflix.com/en/legal/termsofuse"
checkInputs( ref7 )
# privacy
ref8 = "https://help.netflix.com/en/legal/privacy"
checkInputs( ref8 )
# cookie preferences
ref9 = "https://tasty.co/compilation/31-cookie-recipes"
checkInputs( ref9 )

# corporate
ref10 = "https://help.netflix.com/en/legal/corpinfo"
checkInputs( ref10 )

print( "THE END" )