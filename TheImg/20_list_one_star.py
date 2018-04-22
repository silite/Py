import time,re,os,sys
from selenium import webdriver
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
def GetWantBuyAndOperation():
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[2]/td[2]/i')) #加载第二个
    )
    WinningNumList = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    for i in range(0, 9, 2):
        if i == 0:
            position = '万'
        elif i == 2:
            position = '千'
        elif i == 4:
            position = '百'
        elif i == 6:
            position = '十'
        elif i == 8:
            position = '个'
        num = WinningNumList[0][i]
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
        if num == WinningNumList[1][i]:
            print("重庆" + position + "位 " + num + " 符合一组" + str(WantBuy_1))
            Operation(WantBuy_1, i)
        else:
            print("重庆" + position + "位 " + num + " 符合两组" + str(WantBuy_1) + '和' + str(WangBuy_2))
            Operation(WantBuy_1, i)
            Operation(WangBuy_2, i)
def click(x):
    time.sleep(0.5)
    driver.find_element_by_xpath(x).click()
def Operation(WantBuyNum, position):
    for i in WantBuyNum:
        position_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div[' + str((position // 2) + 1) + ']/div[1]/a[' + str(int(i) + 1) + ']'
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
    week_num.send_keys('11')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys('1')
    #times = wait.until(
    #    EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[4]/td/input'))
    #)
    #times.send_keys(Keys.CONTROL + 'a')
    #times.send_keys('2')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
    Buy()
def Buy():
    money_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/p/em[2]'
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,money_xpath))
    )
    money = driver.find_element_by_xpath(money_xpath).text
    if money == '257.40':
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
    sys.stdout.write('重庆时间' + Time + '\n')
    sys.stdout.flush()
    if Time == '00:00:01':
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/span').click()
    return int(Time[-5] + Time[-4]) * 60 + int(Time[-2] + Time[-1])
def waitTime(nowTime ,l ,h = 9120):
    while True:
        if nowTime > l and nowTime < h:
            return nowTime
        else:
            if nowTime == 9120:
                driver.refresh()
            nowTime = GetTime()
def main():
    LogIn()
    while True:
        try:
            url = 'http://www.yfcp885.com/lottery/SSC/1000'
            driver.get(url)
            nowTime = waitTime(GetTime() ,90)
            if nowTime > 90:
                GetWantBuyAndOperation()
            time.sleep(30)
        except Exception as e:
            time.sleep(40)
if __name__ == '__main__':
    main()