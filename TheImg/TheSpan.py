from selenium import webdriver
import re, time, sys, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'silite'
pwd = 'silite'
# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
# profile = webdriver.FirefoxProfile()
# profile.set_preference('permissions.default.stylesheet', 2)
# profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# profile.set_preference('permissions.default.image', 2)
# driver = webdriver.Firefox(firefox_profile=profile, firefox_options=fireFoxOptions)
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
BuyList_1 = [0, 2, 4, 6, 8]
BuyList_2 = [1, 3, 5, 7, 9]
BuyList_3 = [1, 2, 6, 7, 9]
BuyList_4 = [0, 3, 4, 5, 8]
BuyList_5 = [1, 3, 4, 8, 9]
BuyList_6 = [0, 2, 5, 6, 7]
TheReflashTime = 130
TheMinTime = 100
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
def GetBuyNumList(method):
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    WinningNumList = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    for i in range(1, 7):
        if i == 1:
            BuyList = BuyList_1
        elif i == 2:
            BuyList = BuyList_2
        elif i == 3:
            BuyList = BuyList_3
        elif i == 4:
            BuyList = BuyList_4
        elif i == 5:
            BuyList = BuyList_5
        elif i == 6:
            BuyList = BuyList_6
        for j in range(7):
            EitherBuy = True
            if method == 0:
                TheSubNum = int(WinningNumList[j][0]) - int(WinningNumList[j][2])
            else:
                TheSubNum = int(WinningNumList[j][6]) - int(WinningNumList[j][8])
            if TheSubNum < 0:
                TheSubNum = 0 - TheSubNum
            if TheSubNum in BuyList:
                EitherBuy = False
                break
        if EitherBuy:
            Operation(method, BuyList)
def Operation(method, BuyList):
    method_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[' + str(method + 2) + ']'
    method = wait.until(
        EC.presence_of_element_located((By.XPATH, method_xpath))
    )
    method.click()
    method_child = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[2]/li[1]/div/a[4]'))
    )
    method_child.click()
    for i in BuyList:
        position_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div/div/a[' + str(i + 1) + ']'
        click(position_xpath)
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p/select/option[2]')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a')
    click('/html/body/div/div[2]/div[2]/div[1]/div[2]/div[3]/p/label[2]')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/ul/li[3]')
    time.sleep(1)
    try:
        click('/html/body/div[2]/div[2]/div/div/div[2]/span')
    except: pass
    week_num = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[3]/td/input'))
    )
    week_num.send_keys(Keys.CONTROL + 'a')
    week_num.send_keys('6')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys('12')
    #times = wait.until(
    #    EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[4]/td/input'))
    #)
    #times.send_keys(Keys.CONTROL + 'a')
    #times.send_keys('2')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
    Buy()
def click(x):
    time.sleep(0.3)
    driver.find_element_by_xpath(x).click()
def Buy():
    money_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/p/em[2]'
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,money_xpath))
    )
    money = driver.find_element_by_xpath(money_xpath).text
    if money == '1060.00':
        click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/a')
        click('/html/body/div[2]/div[2]/div/div/div[2]/span[2]')
        sure_last = wait.until(
            EC.element_to_be_clickable((By.XPATH ,'/html/body/div[2]/div[2]/div/div/div[2]/span'))
        )
        sure_last.click()
        time.sleep(1)
def GetTime():
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,'/html/body/div/div[2]/div[1]/div[2]/em'))
    )
    time.sleep(1)
    os.system('cls')
    Time = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/em').text
    if len(Time) != 8:
        sys.exit()
    sys.stdout.write('当前时间:' + Time + '\n')
    sys.stdout.flush()
    if Time == '00:00:01':
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/span').click()
    return int(Time[-5] + Time[-4]) * 60 + int(Time[-2] + Time[-1])
def waitTime(nowTime ,l ,h = TheReflashTime):
    while True:
        if nowTime > l and nowTime < h:
            return nowTime
        else:
            if nowTime == TheReflashTime:
                driver.refresh()
            nowTime = GetTime()
def main():
    LogIn()
    while True:
        try:
            url = 'http://www.yfcp885.com/lottery/SSC/1000'
            driver.get(url)
            nowTime = waitTime(GetTime(), TheMinTime)
            if nowTime > TheMinTime:
                for method in range(2):
                    GetBuyNumList(method)
            time.sleep(30)
        except Exception as e:
            time.sleep(40)
if __name__ == '__main__':
    main()