import time,re,os,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'silite'
pwd = 'silite'
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=profile, firefox_options=fireFoxOptions)
# driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
def LogIn():
    element_user = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/ul/li[1]/input'))
    )
    element_user.send_keys(user)
    element_pwd = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/ul/li[2]/input'))
    )
    element_pwd.send_keys(pwd)
    element_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/ul/li[3]/a[1]'))
    )
    element_click.click()
    fin_driver = wait.until(
        EC.url_to_be('http://www.yfcp885.com/index')
    )
def GetWinningNum(x):
    if x == 1:
        url = 'http://www.yfcp885.com/trendChart/1000'
    else:
        url = 'http://www.yfcp885.com/trendChart/1001'
    driver.get(url)
    click_200 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="periods-data"]/a[3]'))
    )
    click_200.click()
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="J-chart-content"]/tr[30]/td[5]/span'))
    )
    WinningNum = re.compile('class="lottery-numbers">(.*?)</span>').findall(driver.page_source)
    return WinningNum[:-4]
def judgewin(WinningNumList, wantbuy, order, position):
    for i in range(1):
        if WinningNumList[order + 30 + i][position] in wantbuy:
            return True
    return False
# def judge():
#     for i in range(1, 3):
#         WinningNumList = GetWinningNum(i)
#         for j in range(0, 9, 2):
#             have = 0
#             win = 0
#             for k in range(160):
#                 count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#                 wantbuy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#                 for x in range(30):
#                     num = WinningNumList[k + x][j]
#                     count[int(num)] += 1
#                 for x in range(10):
#                     max = 0
#                     max_position = 0
#                     for y in range(10):
#                         if count[y] >= max:
#                             max = count[y]
#                             max_position = y
#                     wantbuy[x] = max_position
#                     count[max_position] = -1
#                 wantbuy_str = "".join(map(str, wantbuy[5:]))
#                 have += 1
#                 if judgewin(WinningNumList, wantbuy_str, k, j):
#                     win += 1
#             print(str(have) + " " + str(win))
def sorts(count):
    wantbuy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_ = count[:]
    for x in range(10):
        max = 0
        max_position = 0
        for y in range(10):
            if list_[y] >= max:
                max = list_[y]
                max_position = y
        wantbuy[x] = max_position
        list_[max_position] = -1
    return wantbuy
def judge():
    for i in range(1, 3):
        WinningNumList = GetWinningNum(i)
        for j in range(0, 9, 2):
            have = 0
            win = 0
            for k in range(160):
                count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                x = 0
                try:
                    while True:
                        num = WinningNumList[k + x][j]
                        count[int(num)] += 1
                        x += 1
                        wantbuy = sorts(count)
                        if count[wantbuy[4]] - count[wantbuy[5]] > 3:
                            have += 1
                            break
                except:
                    continue
                wantbuy_str = "".join(map(str, wantbuy[5:]))
                if judgewin(WinningNumList, wantbuy_str, k, j):
                    win += 1
            print(str(have) + " " + str(win))
def main():

    LogIn()
    judge()
if __name__ == '__main__':
    main()