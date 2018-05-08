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
def MoveElement(track):
    ActionChains(driver).click_and_hold(driver.find_element_by_xpath(move_btn_xpath)).perform()
    for x in track:
        ActionChains(driver).move_by_offset(x, 0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()
def ImageCrop():
    driver.find_element_by_xpath(move_btn_xpath).click()
    time.sleep(1)
    driver.save_screenshot('screenshot.png')
    im = Image.open('./screenshot.png')
    im_crop = im.crop((1388, 560, 2038, 795))
    im_crop.save('./cropped.png')
    return im_crop.getdata()
def GetDistance(RGBList):
    for iter_height in range(cropped_im_size[1]):
        for iter_width in range(cropped_im_size[0] - 110):
            NOW_RGB = RGBList[iter_height * cropped_im_size[0] + iter_width]
            NEXT_RGB = RGBList[iter_height * cropped_im_size[0] + iter_width + 1]
            if NOW_RGB[0] - NEXT_RGB[0] > 60:
                return iter_width
    return 0

def GetTrack(distance):
    v0 = 0
    t = 0.2
    mid_distance = distance / 2
    now_distance = 0
    track = []
    while now_distance <= distance:
        if now_distance < mid_distance:
            a = 2
        else:
            a = -2
        v = v0 + a * t
        v0 = v
        x = v * t + 1 / 2 * a * t * t
        if x < 0:
            x = 0 - x
        now_distance += x
        track.append(round(x))
    return track
def main():
    LogIn()
    RGBList = ImageCrop()
    distance = GetDistance(RGBList)
    track = GetTrack(distance)
    MoveElement(track)
    time.sleep(2)
    driver.quit()
if __name__ == "__main__":
    main()