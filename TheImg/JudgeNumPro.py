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
list_0_1 = [8, 9, 0, 1, 2]
list_0_2 = [3, 4, 5, 6, 7]
list_1_1 = [9, 0, 1, 2, 3]
list_1_2 = [4, 5, 6, 7, 8]
list_2_1 = [0, 1, 2, 3, 4]
list_2_2 = [5, 6, 7, 8, 9]
list_3_1 = [1, 2, 3, 4, 5]
list_3_2 = [6, 7, 8, 9, 0]
list_4_1 = [2, 3, 4, 5, 6]
list_4_2 = [7, 8, 9, 0, 1]
list_5_1 = [3, 4, 5, 6, 7]
list_5_2 = [8, 9, 0, 1, 2]
list_6_1 = [4, 5, 6, 7, 8]
list_6_2 = [9, 0, 1, 2, 3]
list_7_1 = [5, 6, 7, 8, 9]
list_7_2 = [0, 1, 2, 3, 4]
list_8_1 = [6, 7, 8, 9, 0]
list_8_2 = [1, 2, 3, 4, 5]
list_9_1 = [7, 8, 9, 0, 1]
list_9_2 = [2, 3, 4, 5, 6]
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
def judgeWin(WinningNumList, order, WantBuy, position):
    EitherWin = False
    for i in range(1, 12):
        if int(WinningNumList[order + i][position]) in WantBuy:
            EitherWin = True
    if not EitherWin:
        print("----未中在", end = '')
        max = 12
        while True:
            if int(WinningNumList[order + max][position]) in WantBuy:
                print(max, end = '')
                print("期----")
                break
            max += 1
    return EitherWin
def judge():
    for i in range(1, 3):
        if i == 1:
            type_ = '重庆'
        else:
            type_ = '新疆'
        WinningNumList = GetWinningNum(i)
        for j in range(0, 9, 2):
            win_1 = 0
            win_2 = 0
            count = 0
            if j == 0:
                position = '万'
            elif j == 2:
                position = '千'
            elif j == 4:
                position = '百'
            elif j == 6:
                position = '十'
            elif j == 8:
                position = '个'
            for k in range(180):
                count += 1
                num = WinningNumList[k][j]
                if num == '0':
                    WantBuy_1 = list_0_1
                    WangBuy_2 = list_0_2
                elif num == '1':
                    WantBuy_1 = list_1_1
                    WangBuy_2 = list_1_2
                elif num == '2':
                    WantBuy_1 = list_2_1
                    WangBuy_2 = list_2_2
                elif num == '3':
                    WantBuy_1 = list_3_1
                    WangBuy_2 = list_3_2
                elif num == '4':
                    WantBuy_1 = list_4_1
                    WangBuy_2 = list_4_2
                elif num == '5':
                    WantBuy_1 = list_5_1
                    WangBuy_2 = list_5_2
                elif num == '6':
                    WantBuy_1 = list_6_1
                    WangBuy_2 = list_6_2
                elif num == '7':
                    WantBuy_1 = list_7_1
                    WangBuy_2 = list_7_2
                elif num == '8':
                    WantBuy_1 = list_8_1
                    WangBuy_2 = list_8_2
                elif num == '9':
                    WantBuy_1 = list_9_1
                    WangBuy_2 = list_9_2
                if judgeWin(WinningNumList, k, WantBuy_1, j):
                    win_1 += 1
                if judgeWin(WinningNumList, k, WangBuy_2, j):
                    win_2 += 1
            print(type_ + position + '位第一组共' + str(count) + ' 中' + str(win_1))
            print(type_ + position + '位第二组共' + str(count) + ' 中' + str(win_2))
def main():
    LogIn()
    judge()
if __name__ == '__main__':
    main()