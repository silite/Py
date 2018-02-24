from selenium import webdriver
import re,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = ''
pwd = ''
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 100)
white = '                  '
cut_line = white + '——————————————————————————————————'

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
def GetWinningNum(type):
    if type == '1':
        type = '1000'
    elif type == '2':
        type = '1001'
    elif type == '3':
        type = '1008'
    url = 'http://www.yfcp885.com/trendChart/' + type
    driver.get(url)
    click_200 = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="periods-data"]/a[3]'))    
    )
    click_200.click()
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="J-chart-content"]/tr[105]/td[5]/span'))
    )
    WinningNum = re.compile('class="lottery-numbers">(.*?)</span>').findall(driver.page_source)
    return WinningNum[:-4]
def Add(a ,b):
    result = ''
    for i in range(0,9,2):
        result += str((int(a[i]) + int(b[i])) % 10) + ','
    return result[:-1]
def print_me(WinningNum):
    print(white ,'|  开奖数据 |' ,'  01组   |' ,'  02组   |' ,'  03组   |' ,'  04组   |' ,'  05组   |\n' ,cut_line)
    for i in range(100):
        print(white ,'|' ,WinningNum[i] ,'|' ,end = '')
        print(Add(WinningNum[0] ,WinningNum[i + 1]) ,'|' ,end = '')
        print(Add(WinningNum[1] ,WinningNum[i + 2]) ,'|' ,end = '')
        print(Add(WinningNum[2] ,WinningNum[i + 3]) ,'|' ,end = '')
        print(Add(WinningNum[3] ,WinningNum[i + 4]) ,'|' ,end = '')
        print(Add(WinningNum[4] ,WinningNum[i + 5]) ,'|')
LogIn()
os.system('cls')
while True:
    i = input('请输入:   1为重庆  2为新疆  3为大发:\n')
    if i == '1' or i == '2' or i == '3':
        WinningNum = GetWinningNum(i)
        print_me(WinningNum)
    while True:
        p = input('是否重新选择? 按y确定:\n')
        if p == 'y':
            os.system('cls')
            break
