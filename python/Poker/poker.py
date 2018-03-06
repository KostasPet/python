from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import urllib2
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.get("https://betsafe.lt/betgamestv")
driver.switch_to.frame("betgames_iframe_1")

def betting(x,amount):
    betNumber = str(x)
    betAmount = str(amount)
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
    try:
        driver.set_page_load_timeout(15)
        driver.get("https://www.topsport.lt/prisijungti?destination=betgamestv")
    except Exception:
        pass
    username = driver.find_element_by_xpath('//*[@id="edit-name"]')
    username.click()
    username.send_keys('kostuxxas@gmail.com')
    password = driver.find_element_by_xpath('//*[@id="edit-pass"]')
    password.click()
    password.send_keys('Pukiss123')
    driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
    time.sleep(2)
    driver.switch_to.frame("betgames_iframe_1")
    progress = driver.find_elements_by_class_name('progress-bar')
    hands = driver.find_element_by_xpath('//*[@id="group_32"]/div')
    hands = hands.find_elements_by_tag_name('a')
    time.sleep(2)
    for hand in hands:
        if hand.get_attribute('data-odd-number') == betNumber:
            hand.click()
    amountField = driver.find_element_by_class_name('bet-amount-input')
    amountField.click()
    amountField.send_keys(betAmount)
    placeBet = driver.find_element_by_class_name('place-bet-button')
    placeBet.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.quit()
    
def check():
    print ""
    global driver
    progress = driver.find_elements_by_class_name('progress-bar')
    money = 26
    defaultAmount = 0.3
    amount = defaultAmount
    
    while True:
        if progress[3].get_attribute('style') == 'width: 100%;' :
            print ""
            best = 1000
            numb = -1;
            addInfo = time.strftime("%c")
            print time.strftime("%c")

            hands = driver.find_element_by_xpath('//*[@id="group_32"]/div')
            hands = hands.find_elements_by_tag_name('a')
            for i in hands:
                print i.get_attribute('data-odd-number')+"("+ i.get_attribute('data-odd-status')+") :" + i.get_attribute('data-odd-name')+" "+i.get_attribute('data-odd-value')
                a = float(i.get_attribute('data-odd-value'))
                if best > a and a != 0:
                    best = a
                    numb = int(i.get_attribute('data-odd-number'))
                
            if best == 2.21 or best == 1.66:
                bet = 1
                print "BETTING"
                #betting(numb,amount)
            else :
                bet = 0
                
            print "best : " + str(numb) + ":" + str(best)
            if numb != -1:
                stat = 0
                print("waiting for result")
                while stat == 0:
                    xpath = '//a[@data-odd-number="'+str(numb)+'"]'
                    bestHand = driver.find_element_by_xpath(xpath)
                    bestHandBadge = bestHand.find_element_by_class_name('badge')
                    
                    
                    if bestHandBadge.get_attribute('innerHTML') == "won":


                        if bet == 1:
                            money = money + amount*(best-1)
                            print "bet amount :"+str(amount)
                            amount = defaultAmount
                            print "money: "+ str(money)
                            print "BET WON"
                            addInfo = str(addInfo)+"/won/"+str(best)
                            
                        addInfo =  addInfo.replace(" ", "_")
                        urllib2.urlopen("http://trolled.lt/poker/get.php?data="+addInfo).read()
                        print(str(numb) + " won "+"(" + str(best)+")")
                        f = open('results.txt','a+')
                        f.write(str(best)+'|won||')
                        f.close()
                        time.sleep(120)
                        stat = 1
                        
                    if bestHandBadge.get_attribute('innerHTML') == "lost":

                        if bet == 1:
                            money = money - amount
                            print "money: "+ str(money)
                            print "BET LOST"
                            if best == 2.21:
                                amount *= 1.5
                            if best == 1.66:
                                amount *= 2.5
                            print "current bet amount :" + str(amount)
                            addInfo = str(addInfo)+"/lost/"+str(best)
                            
                        addInfo = addInfo.replace(" ", "_")
                        urllib2.urlopen("http://trolled.lt/poker/get.php?data="+addInfo).read()
                        print(str(numb) + " lost "+"(" + str(best)+")")
                        f = open('results.txt','a+')
                        f.write(str(best)+'|lost||')
                        f.close()
                        time.sleep(120)
                        stat = 1
                        
                    time.sleep(1)
            else :
                print "error"
                time.sleep(120)

        else :
            time.sleep(1)
check()
