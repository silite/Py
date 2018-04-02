from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'silite'
pwd = 'silite'
# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
# driver = webdriver.Firefox(firefox_options=fireFoxOptions)
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
TheAddList_1 = [5, 7, 9, 11, 13, 15, 17]
TheAddList_2 = [6, 8, 10, 12, 14, 16, 18]
TheAddList_3 = [5, 8, 9, 12, 13, 16, 17]
TheAddList_4 = [6, 7, 10, 11, 14, 15, 18]
TheAddList_5 = [2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20]
TheAddList_6 = [9, 10, 11, 12, 13, 14]

def LogIn():
    element_user = wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/ul/li[1]/input'))
    )
    element_user.send_keys(user)
    element_pwd = wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/ul/li[2]/input'))
    )
    element_pwd.send_keys(pwd)
    element_click = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/ul/li[3]/a[1]'))
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
        EC.element_to_be_clickable((By.XPATH,'//*[@id="periods-data"]/a[3]'))
    )
    click_200.click()
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="J-chart-content"]/tr[30]/td[5]/span'))
    )
    WinningNum = re.compile('class="lottery-numbers">(.*?)</span>').findall(driver.page_source)
    return WinningNum[:-4]
def AddNum(x):
    TheAdd = 0
    for i in range(0, 5, 2):
#   for i in range(2, 7, 2):
#   for i in range(4, 9, 2):
        TheAdd += int(x[i])
    return TheAdd
def judge(WinningNum):
    TheMax = 0
    for i in range(190):
        print(".", end='')
        Week = 0
        while True:
            if AddNum(WinningNum[i + Week]) in TheAddList_1:
                if Week > TheMax:
                    TheMax = Week
                break
            else:
                Week += 1
    return TheMax
def main():
    LogIn()
    while True:
        x = input('请输入种类 1.重庆 2.新疆\n')
        WinningNum = GetWinningNum(int(x))
        print(judge(WinningNum))
if __name__ == '__main__':
    main()