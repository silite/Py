from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'silite'
pwd = 'silite'
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(firefox_options=fireFoxOptions)
#driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 100)
Buy_1 = ['03489','01459','01256','12367','23478','12567','23678','34789','04589','01569']
Buy_2 = ['01256','12367','23468','03489','01459','04589','01569','12568','23678','34789']
gewei = 8
shiwei = 6
baiwei = 4
qianwei = 2
wanwei = 0
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
    click_50 = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="periods-data"]/a[2]'))    
    )
    click_50.click()
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="J-chart-content"]/tr[48]/td[2]'))
    )
    WinningNum = re.compile('class="lottery-numbers">(.*?)</span>').findall(driver.page_source)
    return WinningNum[:-4]
def GetWeekNum():
    WeekNum = []
    for i in range(1, 51):
        xpath = '//*[@id="J-chart-content"]/tr[' + str(i) + ']/td[2]'
        WeekNum.append(driver.find_element_by_xpath(xpath).text)
    return WeekNum
    #WinningWeek = re.compile('class="issue-numbers">(.*?)</td>').findall(driver.page_source)
def Judge(WinningNum):
    position = gewei
    week = 8
    win = 0
    for i in range(190):
        father_num = int(WinningNum[i][position])
        for j in range(1, week + 1):
            if WinningNum[i + j][position] in Buy_1[father_num] or WinningNum[i + j][position] in Buy_2[father_num]:
                win += 1
                break
    print(win)
def AddTenWeekNum(WinningWeek, WinningNum, x):
    if x == 1:
        position = wanwei
    elif x == 2:
        position = qianwei
    elif x == 3:
        position = baiwei
    elif x == 4:
        position = shiwei
    elif x == 5:
        position = gewei
    else:
        print('重新输入')
        return 0
    for i in range(41):
        result = 0
        for j in range(10):
            result += int(WinningNum[i + j][position])
        print(WinningWeek[i] + '-' + WinningWeek[i + 9] + ' :' + str(result))
def main():
    LogIn()
    while True:
        x = input('请输入种类 1.重庆 2.新疆\n')
        WinningNum = GetWinningNum(int(x))
        WinningWeek = GetWeekNum()
        while True:
            x = input('请输入位置 1.万位 2.千位 3.百位 4.十位 5.个位 6.重新选择彩种\n')
            if x == '6':
                break
            AddTenWeekNum(WinningWeek, WinningNum, int(x))
        #Judge(WinningNum)
if __name__ == '__main__':
    main()