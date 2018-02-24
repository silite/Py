
from selenium import webdriver
import time,re,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = ''
pwd = ''
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
wait_short = WebDriverWait(driver, 1)
comp = ['0156','0158','0167','0169','0178','0189',
'0257','0259','0279',
'0356','0358','0367','0369','0378','0389',
'0457','0459','0479',
'1256','1258','1267','1269','1278','1289',
'1368','1456','1458','1467','1469','1478','1489',
'2356','2358','2367','2369','2378','2389',
'2457','2459','2479',
'3456','3458','3467','3469','3478','3489']
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
def JudgeRe(list_,method): #method分前中后
    num_1 = list_[0].split(',') #中奖号码
    num_2 = list_[1].split(',')
    num_3 = list_[2].split(',')
    #num_4 = list_[3].split(',')
    if method == 'hou' :
        method_zh = '后三'
        num_1 = num_1[2:]
        num_2 = num_2[2:]
        num_3 = num_3[2:]
        #num_4 = num_4[2:]
    elif method == 'zhong' :
        method_zh = '中三'
        num_1 = num_1[1:4]
        num_2 = num_2[1:4]
        num_3 = num_3[1:4]
        #num_4 = num_4[1:4]
    elif method == 'qian' :
        method_zh = '前三'
        num_1 = num_1[:3]
        num_2 = num_2[:3]
        num_3 = num_3[:3]
        #num_4 = num_4[:3]
    temp = list(set(num_1 + num_2 + num_3))
    rejudge = []
    for i in range(0,10):
        i = str(i)
        if i not in temp:
            rejudge.append(i)
    if len(rejudge) == 0:
        print("--- 无剩余数字 ---")
    else:
        print("--- 剩余可选数字: ---")
        print(rejudge)
        if len(rejudge) < 4:
            return ''
        else:
            for i in comp:
                count = 0
                for j in i:
                    if j in ''.join(rejudge):
                        count += 1
                        if(count == 4):
                            print("--- 符合给定: " + method_zh + ' ' + i + " 正在打印 ---")
                            return i
            return ''
def OpStr(result):
    if len(result) == 0:
        return ''
    else:
        temp = []
        str_ = ''
        result = list(result)
        for j in range(0,500):
            j = "%03d" % j
            j = str(j)
            if result[0] in j or result[1] in j or result[2] in j or result[3] in j:
                str_ += j + ','
        str_ = str_[0:-1]
        temp.append(str_)
        str_ = ''
        for j in range(500,1000):
            j = "%03d" % j
            j = str(j)
            if result[0] in j or result[1] in j or result[2] in j or result[3] in j:
                str_ += j + ','
        str_ = str_[0:-1]
        temp.append(str_)
    return temp
def submit():
    time.sleep(3)
    wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[3]'))
    )
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a')
def click(x):
    time.sleep(0.5)
    driver.find_element_by_xpath(x).click()
def AlertRate():
    time.sleep(0.5)
    try:
        sure = wait_short.until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="layermbox1"]/div[2]/div/div/div[2]/span'))
        )
        sure.click()
    except:
        return 0
def send_all_me(xpath,result):
    method = wait.until(
        EC.presence_of_element_located((By.XPATH,xpath))
    )
    method.click()
    danshi = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[2]/li[1]/div/a[2]'))
    )
    danshi.click()
    fen = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p/select/option[3]'))
    )
    fen.click()
    send_result = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[3]/textarea'))
    )
    send_result.send_keys(result[0])
    submit()
    send_result.send_keys(result[1])
    submit()
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[3]/p/label[2]')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/ul/li[3]')
    AlertRate()
    sure_2 = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="layermbox0"]/div[2]/div/div/div[2]/span'))
    )
    sure_2.click()
    week_num = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[3]/td/input'))
    )
    week_num.send_keys(Keys.CONTROL + 'a')
    week_num.send_keys('3')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys('4')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
def wait_to_be_num():
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[2]/td[2]/i')) #加载第二个
    )
def PreAddNum(method):
    WinningNum = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    print("--- 此四期号码 ---:\n--- " + WinningNum[0] + " ---\n--- " + WinningNum[1] + " ---\n--- " + WinningNum[2] + " ---\n--- ")
    return OpStr(JudgeRe(WinningNum,method))
def FirstIn():
    try:
        sure_fir = wait_short.until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="layermbox1"]/div[2]/div/div/div[2]/span'))
        )
        sure_fir.click()
    except:
        return 0
try:
    LogIn()
    driver.get('http://www.yfcp885.com/lottery/SSC/1000')
    FirstIn()
    while True:
        flag = input("--- 是否开始判断后三 --- :  ")
        if flag == "y" or flag == "Y":
            wait_to_be_num()
            result_hou = PreAddNum('hou')
            if len(result_hou) == 2:
                housan = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[6]'
                send_all_me(housan,result_hou)
            else:
                print("--- 后三此次无符合 ---.\n")
        flag = ''
        flag = input("--- 是否开始判断中三 ---:  ")
        if flag == "y" or flag == "Y":
            driver.refresh()
            FirstIn()
            wait_to_be_num()
            result_zhong = PreAddNum('zhong')
            if len(result_zhong) == 2:
                zhongsan = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[5]'
                send_all_me(zhongsan,result_zhong)
            else:
                print("--- 中三此次无符合 ---.\n")
        flag = ''
        flag = input("--- 是否开始判断前三 ---:  ")
        if flag == "y" or flag == "Y":
            driver.refresh()
            FirstIn()
            wait_to_be_num()
            result_qian = PreAddNum('qian')
            if len(result_qian) == 2:
                qiansan = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[4]'
                send_all_me(qiansan,result_qian)
            else:
                print("--- 前三此次无符合 ---.\n")
        flag = ''
        flag = input("--- 是否刷新重新执行 ---:  ")
        if flag == 'y':
            driver.refresh()
            os.system('cls')
            continue
        else:
            break
except Exception as e:
    print(e)