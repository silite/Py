from PIL import Image
from selenium import webdriver
import time, sys, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
DEBUG = True
if not DEBUG:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.bilibili.com")
    move_btn_xpath = '//*[@id="gc-box"]/div/div[3]/div[2]'
cropped_im_size = (500, 235)
either_threshold = 100
jump_threshold = 180

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
    hold = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gc-box"]/div/div[3]/div[1]'))
    )
    hold.click()
    time.sleep(1)
    driver.save_screenshot('screenshot.png')
    im = Image.open('./screenshot.png')
    im_crop = im.crop((1538, 560, 2038, 795))
    im_crop.save('./cropped1.png')
    driver.find_element_by_xpath(move_btn_xpath).click()
    time.sleep(0.5)
    driver.save_screenshot('screenshot.png')
    im = Image.open('./screenshot.png')
    im_crop = im.crop((1538, 560, 2038, 795))
    im_crop.save('./cropped2.png')
def GetDistance(RGBList_1, RGBList_2):
    conform = []
    for iter_height in range(cropped_im_size[1]):
        either = 0

        for iter_width in range(cropped_im_size[0] - 100):
            NOW_RGB_1 = RGBList_1[iter_height * cropped_im_size[0] + iter_width]
            NOW_RGB_2 = RGBList_2[iter_height * cropped_im_size[0] + iter_width]
            if NOW_RGB_1 != NOW_RGB_2:
                either += 1
                if either >= either_threshold:
                    either_two = True
                    if len(conform) != 0 and iter_width - conform[-1] < jump_threshold:
                        continue
                    point_width = iter_width - either_threshold
                    for iter_height_two in range(1, 40):
                        NOW_RGB_1 = RGBList_1[(iter_height + iter_height_two) * cropped_im_size[0] + point_width]
                        NOW_RGB_2 = RGBList_2[(iter_height + iter_height_two) * cropped_im_size[0] + point_width]
                        if NOW_RGB_1 == NOW_RGB_2:
                            either_two = False
                            break
                    if either_two:
                        conform.append(point_width)
                        either = 0
            else:
                either = 0
    print(conform)
    return conform[0] + 135

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
    if DEBUG:
        RGBList_1 = Image.open('./cropped1.png').getdata()
        RGBList_2 = Image.open('./cropped2.png').getdata()
        distance = GetDistance(RGBList_1, RGBList_2)
    else:
        LogIn()
        while True:
            ImageCrop()
            RGBList_1 = Image.open('./cropped1.png').getdata()
            RGBList_2 = Image.open('./cropped2.png').getdata()
            distance = GetDistance(RGBList_1, RGBList_2)
            distance = round(distance / 490 * 200)
            track = GetTrack(distance)
            MoveElement(track)
            time.sleep(2)
if __name__ == "__main__":
    main()