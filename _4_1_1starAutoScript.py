from selenium import webdriver
import re,os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = ''
pwd = ''
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 100)
gewei = 5
shiwei = 4
baiwei = 3
qianwei = 2
wanwei = 1
comp_1 = ['7890','8901','9012','0123','1234','2345','3456','4567','5678','6789']
comp_2 = ['0123','1234','2345','3456','4567','5678','6789','7890','8901','9012']
def LogIn():
    element_user = wait.until(
        EC.presence_of_element_located((By.XPATH ,'//*[@id="app"]/div[2]/ul/li[1]/input'))
    )
    element_user.send_keys(user)
    element_pwd = wait.until(
        EC.presence_of_element_located((By.XPATH ,'//*[@id="app"]/div[2]/ul/li[2]/input'))
    )
    element_pwd.send_keys(pwd)
    element_click = wait.until(
        EC.element_to_be_clickable((By.XPATH ,'//*[@id="app"]/div[2]/ul/li[3]/a[1]'))
    )
    element_click.click()
    fin_driver = wait.until(
        EC.url_to_be('http://www.yfcp885.com/index')
    )
    os.system('cls')
def GetNum_list(position ,type_):
    if type_ == '1':
        type_ = '1000'
    elif type_ == '2':
        type_ = '1001'
    url = 'http://www.yfcp885.com/lottery/SSC/' + type_
    driver.get(url)
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    WinningNum_list = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    return [comp_1[int(WinningNum_list[0][position])] ,comp_2[int(WinningNum_list[0][position])]]
def click(x):
    driver.find_element_by_xpath(x).click()
def AllOp(method ,type_):
    if method == 1:
        method_zh = '万位'
        position = 0
    elif method == 2:
        method_zh = '千位'
        position = 2
    elif method == 3:
        method_zh = '百位'
        position = 4
    elif method == 4:
        method_zh = '十位'
        position = 6
    elif method == 5:
        method_zh = '个位'
        position = 8
    for count in range(2):
        flag = input('是否开始' + method_zh + '第 ' + str(count + 1) + ' 组? 按y确定:\n')
        if flag == 'y':
            send_list = GetNum_list(position ,type_)
            jiao = wait.until(
                EC.element_to_be_clickable((By.XPATH ,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p/select/option[2]'))
            )
            jiao.click()
            Xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div[' + str(method) + ']'
            wait.until(
                EC.presence_of_all_elements_located((By.XPATH ,Xpath))    
            )
            for i in send_list[count]:
                Xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div[' + str(method) + ']/div[1]/a[' + str(int(i) + 1) + ']'
                click(Xpath)
            click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a')
            click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[3]/p/label[2]')
            click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/ul/li[3]')
            time.sleep(0.5)
            alert = wait.until(
                EC.element_to_be_clickable((By.XPATH ,'//*[@id="layermbox0"]/div[2]/div/div/div[2]/span'))    
            )
            alert.click()
            week_num = wait.until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[3]/td/input'))
            )
            week_num.send_keys(Keys.CONTROL + 'a')
            week_num.send_keys('6')
            rate = wait.until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
            )
            rate.send_keys(Keys.CONTROL + 'a')
            rate.send_keys('23')
            click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
            click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/a')
LogIn()
while True:
    type_ = input('请输入彩种 1重庆 2新疆:\n')
    if type_ == '1' or type_ == '2':
        for position in range(5,0,-1):
            AllOp(position ,type_)
        while True:
            i = input('是否刷新重新执行？按y确定:\n')
            if i == 'y':
                os.system('cls')
                break
    else:
        print('错误 请重新输入\n')
