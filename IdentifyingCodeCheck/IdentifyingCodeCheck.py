from PIL import Image
from selenium import webdriver
import time, sys, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.bilibili.com")
move_action = ActionChains(driver)
move_btn_xpath = '//*[@id="gc-box"]/div/div[3]/div[2]'
cropped_im_size = (650, 235)

def LogIn():
    login_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/ul/li[1]/div/a'))
    )
    login_btn.click()
    move_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, move_btn_xpath))
    )
def MoveElement(distance):
    move_action.click_and_hold(driver.find_element_by_xpath(move_btn_xpath))
    move_action.move_by_offset(260, 0)
    move_action.release().perform()
def ImageCrop():
    move_action.click_and_hold(driver.find_element_by_xpath(move_btn_xpath))
    move_action.move_by_offset(100, 0)
    move_action.release().perform()
    time.sleep(1)
    driver.save_screenshot('screenshot.png')
    im = Image.open('./screenshot.png')
    im_crop = im.crop((1388, 560, 2038, 795))
    im_crop.save('./cropped.png')
    return im.getdata()
def GetDistance(RGBList):
    return 0
def main():
    LogIn()
    RGBList = ImageCrop()
    distance = GetDistance(RGBList)
    print(distance)
    MoveElement(distance)
if __name__ == "__main__":
    main()