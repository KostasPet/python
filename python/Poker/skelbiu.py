from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')

def login(user, pas) :
    global driver
    driver.get("https://www.skelbiu.lt/users/signin")
    username = driver.find_element_by_xpath('//*[@id="user"]/input')
    password = driver.find_element_by_xpath('//*[@id="login-area"]/div[2]/input')
    submit = driver.find_element_by_xpath('//*[@id="login-button"]')
    username.send_keys(user)
    password.send_keys(pas)
    submit.click()

def update():
    global driver
    update = driver.find_element_by_xpath('//*[@id="updateAds"]')
    update.click()
    confirm = driver.find_element_by_xpath('//*[@id="submit"]')
    confirm.click()
    
login("tabletx","pukiss123");
