from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#<a data-odd-id="451" data-items-count="0" data-odd-name="Laimės ranka 6" data-odd-number="5" data-odd-value="0.00" data-odd-value-real="0" href="#" class="team list-group-item disabled" data-odd-status="won" data-is-enabled="0">

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
try:
    driver.set_page_load_timeout(1)
    driver.get("https://www.topsport.lt/zaidimai")
except Exception:
        pass
driver.switch_to.frame("betgames_iframe_1")
amountField = driver.find_element_by_class_name('bet-amount-input')
amountField.click()
amountField.send_keys(0)
placeBet = driver.find_element_by_class_name('place-bet-button')
placeBet.send_keys(Keys.ENTER)


