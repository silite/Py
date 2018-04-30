from selenium import webdriver
import re, time, sys, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'zy0108'
pwd = 'zy731027'
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=profile, firefox_options=fireFoxOptions)

driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
TheAddList_1 = [5, 7, 9, 11, 13, 15, 17]
TheAddList_2 = [6, 8, 10, 12, 14, 16, 18]
TheAddList_3 = [5, 8, 9, 12, 13, 16, 17]
TheAddList_4 = [6, 7, 10, 11, 14, 15, 18]
TheAddList_5 = [9, 10, 11, 12, 13, 14]
TheAddList_6 = [5, 6, 7, 8, 15, 16, 17, 18]
TheAddList_7 = [5, 7, 8, 11, 13, 14, 17]
TheAddList_8 = [10, 12, 14, 16, 18, 20, 22] 
TheAddList_9 = [6, 9, 10, 12, 15, 16, 18]
TheAddList_10 = [5, 9, 11, 14, 16, 18, 20, 22]
TheAddList_11 = [5, 6, 7, 8, 9, 10, 11, 12]
TheAddList_12 = [15, 16, 17, 18, 19, 20, 21, 22]
TheAddList_13 = [11, 12, 15, 16, 19, 20, 23, 24]
TheAddList_14 = [9, 10, 11, 12, 19, 20, 21, 22]
TheAddList_15 = [5, 6, 7, 9, 10, 12, 14, 16]
TheAddList_16 = [6, 8, 9, 10, 11, 13, 15]
TheAddList_17 = [3, 4, 7, 8, 11, 12, 15, 16]
TheAddList_18 = [4, 5, 6, 9, 10, 13, 14, 17]
TheAddList_19 = [10, 13, 14, 17, 18, 21, 22, 23]
start_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
qian = 1
zhong = 2
hou = 3
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
def wait_to_be_num():
    driver.get("http://www.yfcp885.com/trendChart/1000")
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="J-chart-content"]/tr[30]/td[5]/span')) #加载第一个
    )
def click(x):
    time.sleep(0.3)
    driver.find_element_by_xpath(x).click()
def PrintLog(content):
    with open('D:\log\Cq总_' + start_time + '.txt' ,'a') as f:
        f.write(content)
def GetTime():
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,'/html/body/div/div[2]/div[1]/div[2]/em'))
    )
    time.sleep(1)
    os.system('cls')
    Time = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/em').text
    if len(Time) != 8:
        sys.exit()
    sys.stdout.write('重庆和值总  :' + Time + '\n')
    sys.stdout.flush()
    if Time == '00:00:01':
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/span').click()
    return int(Time[-5] + Time[-4]) * 60 + int(Time[-2] + Time[-1])
def waitTime(nowTime ,l ,h = 130):
    while True:
        if nowTime > l and nowTime < h:
            return nowTime
        else:
            if nowTime == 130:
                driver.refresh()
            nowTime = GetTime()
def EitherBuyList(method):
    EitherList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    wait_to_be_num()
    WinningNum = re.compile('class="lottery-numbers">(.*?)</span>').findall(driver.page_source)
    driver.get("http://www.yfcp885.com/lottery/SSC/1000")
    for i in range(1, 20):
        BuyFlag = True
        if i == 1:
            TheAddList = TheAddList_1
        elif i == 2:
            TheAddList = TheAddList_2
        elif i == 3:
            TheAddList = TheAddList_3
        elif i == 4:
            TheAddList = TheAddList_4
        elif i == 5:
            TheAddList = TheAddList_5
        elif i == 6:
            TheAddList = TheAddList_6
        elif i == 7:
            TheAddList = TheAddList_7
        elif i == 8:
            TheAddList = TheAddList_8
        elif i == 9:
            TheAddList = TheAddList_9
        elif i == 10:
            TheAddList = TheAddList_10
        elif i == 11:
            TheAddList = TheAddList_11
        elif i == 12:
            TheAddList = TheAddList_12
        elif i == 13:
            TheAddList = TheAddList_13
        elif i == 14:
            TheAddList = TheAddList_14
        elif i == 15:
            TheAddList = TheAddList_15
        elif i == 16:
            TheAddList = TheAddList_16
        elif i == 17:
            TheAddList = TheAddList_17
        elif i == 18:
            TheAddList = TheAddList_18
        elif i == 19:
            TheAddList = TheAddList_19
        for j in range(16, 30):
            if AddNum(WinningNum[j], method) in TheAddList:
                BuyFlag = False
                break
        if BuyFlag:
            EitherList[i - 1] = 1
    return EitherList
def AddNum(x, method):
    TheAdd = 0
    if method == qian:
        for i in range(0, 5, 2):
            TheAdd += int(x[i])
        return TheAdd
    elif method == zhong:
        for i in range(2, 7, 2):
            TheAdd += int(x[i])
        return TheAdd
    elif method == hou:
        for i in range(4, 9, 2):
            TheAdd += int(x[i])
        return TheAdd
def Operation(method, order):
    print("\n" + "第" + str(order) + "组符合")
    print("\a")
    method_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[' + str(method + 3) + ']'
    method = wait.until(
        EC.presence_of_element_located((By.XPATH, method_xpath))
    )
    method.click()
    method_child = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[2]/li[2]/div/a[1]'))
    )
    method_child.click()
    if order == 1:
        TheAddList = TheAddList_1
        percent = '134'
    elif order == 2:
        TheAddList = TheAddList_2
        percent = '124'
    elif order == 3:
        TheAddList = TheAddList_3
        percent = '127'
    elif order == 4:
        TheAddList = TheAddList_4
        percent = '131'
    elif order == 5:
        TheAddList = TheAddList_5
        percent = '127'
    elif order == 6:
        TheAddList = TheAddList_6
        percent = '131'
    elif order == 7:
        TheAddList = TheAddList_7
        percent = '134'
    elif order == 8:
        TheAddList = TheAddList_8
        percent = '134'
    elif order == 9:
        TheAddList = TheAddList_9
        percent = '124'
    elif order == 10:
        TheAddList = TheAddList_10
        percent = '124'
    elif order == 11:
        TheAddList = TheAddList_11
        percent = '131'
    elif order == 12:
        TheAddList = TheAddList_12
        percent = '131'
    elif order == 13:
        TheAddList = TheAddList_13
        percent = '134'
    elif order == 14:
        TheAddList = TheAddList_14
        percent = '131'
    elif order == 15:
        TheAddList = TheAddList_15
        percent = '134'
    elif order == 16:
        TheAddList = TheAddList_16
        percent = '124'
    elif order == 17:
        TheAddList = TheAddList_17
        percent = '134'
    elif order == 18:
        TheAddList = TheAddList_18
        percent = '127'
    elif order == 19:
        TheAddList = TheAddList_19
        percent = '127'
    for i in TheAddList:
        position_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div/div/a[' + str(i) + ']'
        click(position_xpath)
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p/select/option[3]')
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
    week_num.send_keys('8')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys(percent)
    #times = wait.until(
    #    EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[4]/td/input'))
    #)
    #times.send_keys(Keys.CONTROL + 'a')
    #times.send_keys('2')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
def Buy(order):
    money_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/p/em[2]'
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,money_xpath))
    )
    money = driver.find_element_by_xpath(money_xpath).text
    if order == 1:
        x = '934.40'
    elif order == 2:
        x = '833.32'
    elif order == 3:
        x = '828.20'
    elif order == 4:
        x = '944.46'
    elif order == 5:
        x = '828.20'
    elif order == 6:
        x = '944.46'
    elif order == 7:
        x = '934.40'
    elif order == 8:
        x = '934.40'
    elif order == 9:
        x = '833.32'
    elif order == 10:
        x = '833.32'
    elif order == 11:
        x = '944.46'
    elif order == 12:
        x = '944.46'
    elif order == 13:
        x = '934.40'
    elif order == 14:
        x = '944.46'
    elif order == 15:
        x = '833.32'
    elif order == 16:
        x = '833.32'
    elif order == 17:
        x = '934.40'
    elif order == 18:
        x = '828.20'
    elif order == 19:
        x = '828.20'
    if money == x:
        click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/a')
        click('/html/body/div[2]/div[2]/div/div/div[2]/span[2]')
        sure_last = wait.until(
            EC.element_to_be_clickable((By.XPATH ,'/html/body/div[2]/div[2]/div/div/div[2]/span'))
        )
        sure_last.click()
        time.sleep(1)
def main():
    LogIn()
    while True:
        try:
            url = 'http://www.yfcp885.com/lottery/SSC/1000'
            driver.get(url)
            nowTime = waitTime(GetTime(), 100)
            if nowTime > 100:
                for i in range(1, 4):
                    if i == 1:
                        print("----前三----")
                    elif i == 2:
                        print("----中三----")
                    elif i == 3:
                        print("----后三----")
                    EitherList = EitherBuyList(i)
                    for j in range(1, 20):
                        if EitherList[j - 1]:
                            Operation(i, j)
                            Buy(j)
            PrintLog("\n")
            time.sleep(30)
        except Exception as e:
            print(e)
            PrintLog(e)
            time.sleep(40)
if __name__ == '__main__':
    main()