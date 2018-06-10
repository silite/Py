from selenium import webdriver
import re, time, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# user = 'zy0108'
# pwd = 'zy731027'
user = 'silite'
pwd = 'silite'
ISOTIMEFORMAT = '%X'
DEBUG = True
if not DEBUG:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    profile = webdriver.FirefoxProfile()
    profile.set_preference('permissions.default.stylesheet', 2)
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    profile.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(firefox_profile=profile, firefox_options=fireFoxOptions)
else:
    driver = webdriver.Firefox()
driver.get('http://www.yfcp828.com/login')
wait = WebDriverWait(driver, 10)
either_buy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
not_buy = [[0, 5], [1, 9], [2, 8], [3, 7], [4, 6], [5, 0], [4, 6], [3, 7], [2, 8], [1, 9]]
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
        EC.url_to_be('http://www.yfcp828.com/index')
    )
def click(x):
    time.sleep(0.3)
    driver.find_element_by_xpath(x).click()
def Operation(position, buy_list):
    method = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[' + str(position + 2) + ']'))
    )
    method.click()
    method_child = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[2]/li[1]/div/a[4]'))
    )
    method_child.click()
    for i in buy_list:
        position_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div/div/a[' + str(i + 1) + ']'
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
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[3]/td/input'))
    )
    week_num.send_keys(Keys.CONTROL + 'a')
    week_num.send_keys('3')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys('6')
    time_ = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[4]/td/input'))
    )
    time_.send_keys(Keys.CONTROL + 'a')
    time_.send_keys('10')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
    Buy()
def Buy():
    money_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/p/em[2]'
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH, money_xpath))
    )
    money = driver.find_element_by_xpath(money_xpath).text
    if money == '891.20':
        click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/a')
        click('/html/body/div[2]/div[2]/div/div/div[2]/span[2]')
        sure_last = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/span'))
        )
        sure_last.click()
        time.sleep(1)
def GetTheLastNum():
    result = []
    driver.get("http://www.yfcp828.com/lottery/SSC/1000")
    try:
        click('//*[@id="layermbox0"]/div[2]/div/div/div[2]/span')
    except:
        pass
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    WinningNumWeekList = re.compile('class="o_qi">(.*?)<').findall(driver.page_source)
    result.append(int(WinningNumWeekList[0][-1]))
    WinningNumList = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    result.append(WinningNumList[0])
    result.append(WinningNumList[1])
    return result
def get_either(i):
    temp = []
    for j in either_buy:
        if j not in not_buy[i]:
            temp.append(j)
    return temp
def main():
    LogIn()
    #准备工作完毕
    EitherLastNum = -1
    print("重庆跨度")
    while True:
        nowTime = time.strftime(ISOTIMEFORMAT, time.localtime())
        min = int(nowTime[3] + nowTime[4])
        if nowTime[0] == '0' and nowTime[1] == '1' and min >= 40:
            print("已停止")
            sys.exit(0)
        info = GetTheLastNum()
        LastNum = info[0]
        if LastNum != EitherLastNum:
            EitherLastNum = LastNum
            #并执行投注
            for i in range(2):
                if i == 0:
                    sub_1 = (int(info[1][2]) * 2 + int(info[2][2])) % 10
                    sub_2 = (int(info[1][0]) * 2 + int(info[2][0])) % 10
                else:
                    sub_1 = (int(info[1][8]) * 2 + int(info[2][8])) % 10
                    sub_2 = (int(info[1][6]) * 2 + int(info[2][6])) % 10
                sub = abs(sub_1 - sub_2)
                buy_list = get_either(sub)
                Operation(i, buy_list)
            time.sleep(60)
        else:
            time.sleep(60)
if __name__ == '__main__':
    main()