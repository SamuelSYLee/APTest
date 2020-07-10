'----------------------------------------------------'
'Automation for AP AnimalKenTei Website              '
'Copyright @ Samuel Lee                              '
'----------------------------------------------------'

import time, os
from selenium import webdriver
import pyautogui as pag


def loginAPKT():
    #Login APKT
    driver.find_element_by_xpath("//nav[@class='header-nav']/ul/li[5]").click()

    AccountName = driver.find_element_by_xpath("//div[1]/input[@class='input-field w50']")
    AccountName.clear()
    AccountName.send_keys("Please type in your ACCOUNT")

    AccountPW = driver.find_element_by_xpath("//div[2]/input[@class='input-field w50']")
    AccountPW.clear()
    AccountPW.send_keys("Please type in your PASSWORD")

    driver.find_element_by_xpath("//button[@class='btn_signin btn_blue btn_radius']").click()

def logoutAPKT():
    time.sleep(2)
    driver.find_element_by_xpath("//nav[@class='header-nav']/ul/li[5]").click()

def answerQ():
    for i in range(5):
        print('Answer question', i + 1)
        time.sleep(1)
        filename = os.path.dirname(__file__) + '/akt' + str(i + 1) + '.png'
        driver.get_screenshot_as_file(filename)
        driver.find_element_by_xpath("//div[@class='item'][1]").click()
        pag.scroll(-100)
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn_nextchallenge btn_blue btn_radius gaBtn']").click()
        time.sleep(1)
        pag.scroll(-100)

        if i == 4:
            driver.find_element_by_xpath("//div[@class='lb-close-btn']").click()
        else:
            try:
                driver.find_element_by_xpath("//button[@class='btn_nextchallenge btn_darkblue btn_radius']").click()
            except:
                MouseMoveTo(580, 710)
                print(pag.position())
                pag.click()

        time.sleep(2)

def MouseMoveTo(xPos, yPos):
    pag.moveTo(xPos, yPos, duration = 0.5)


if __name__ == "__main__":
    #Connect AKT Website
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    AKT_url = "https://www.discoverychannel.com.tw/animalkentei/index.php"
    driver.get(AKT_url)
    #Adjust Window Size
    driver.maximize_window()
    try: 
        driver.find_element_by_xpath("//div[@class='lb-close-btn']").click()
    except:
        time.sleep(1)

    #-------Login & Start------
    loginAPKT()
    time.sleep(1)
    MouseMoveTo(450, 350)
    pag.scroll(-10)
    time.sleep(1)
    filename = os.path.dirname(__file__) + '/ACCOUNT.png'
    driver.get_screenshot_as_file(filename)
    driver.find_element_by_xpath("//button[@class='btn_goplay btn_darkblue btn_radius gaBtn']").click()
    driver.find_element_by_xpath("//a[@class='btn btn_play']").click()

    try:
        print("Alert:", driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
    except:
        answerQ()

    logoutAPKT()
    time.sleep(3)
    print('Test Result: PASS')
    driver.quit()
