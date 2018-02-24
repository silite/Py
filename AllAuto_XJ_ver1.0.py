import time,re,os,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = ''
pwd = ''
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(firefox_options=fireFoxOptions)

#driver = webdriver.Firefox()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
start_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
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
def JudgeRe(list_,method):
    num_1 = list_[0].split(',')
    num_2 = list_[1].split(',')
    num_3 = list_[2].split(',')
    num_4 = list_[3].split(',')
    #num_5 = list_[4].split(',')
    if method == 'hou' :
        method_zh = '后三'
        method_en = 'Back'
        num_1 = num_1[2:]
        num_2 = num_2[2:]
        num_3 = num_3[2:]
        num_4 = num_4[2:]
        #num_5 = num_5[2:]
    elif method == 'zhong' :
        method_zh = '中三'
        method_en = 'Mid'
        num_1 = num_1[1:4]
        num_2 = num_2[1:4]
        num_3 = num_3[1:4]
        num_4 = num_4[1:4]
        #num_5 = num_5[1:4]
    elif method == 'qian' :
        method_zh = '前三'
        method_en = 'Front'
        num_1 = num_1[:3]
        num_2 = num_2[:3]
        num_3 = num_3[:3]
        num_4 = num_4[:3]
        #num_5 = num_5[:3]
    temp = list(set(num_1 + num_2 + num_3 + num_4))
    rejudge = []
    for i in range(0,10):
        i = str(i)
        if i not in temp:
            rejudge.append(i)
    if len(rejudge) >= 4:
        i = rejudge[0] + rejudge[1] + rejudge[2] + rejudge[3] 
        PrintLog('' + method_en + ':' + i + '\n')
        print("符合给定: " + method_zh + ' ' + i + " 正在打印 ")
        return i
    else:
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
    wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[3]'))
    )
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a')
def click(x):
    time.sleep(0.3)
    driver.find_element_by_xpath(x).click()
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
    week_num.send_keys('3')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys('4')
    #times = wait.until(
    #    EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[4]/td/input'))
    #)
    #times.send_keys(Keys.CONTROL + 'a')
    #times.send_keys('2')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
def wait_to_be_num():
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[2]/td[2]/i')) #加载第二个
    )
def PrintLog(content):
    with open('D:\log\d_' + start_time + '.txt' ,'a') as f:
        f.write(content)
def PreAddNum(method):
    WinningNum = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    PrintLog("X_ " + WinningNum[0] + " | " + WinningNum[1] + " | " + WinningNum[2] + " | " + WinningNum[3] + "   ")
    return OpStr(JudgeRe(WinningNum,method))
def Buy():
    money_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/p/em[2]'
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,money_xpath))    
    )
    money = driver.find_element_by_xpath(money_xpath).text
    if money == '674.24':
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
    Time = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/em').text
    if Time == '00:00:01':
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/span').click()
    return int(Time[-5] + Time[-4]) * 60 + int(Time[-2] + Time[-1])
def waitTime(nowTime ,l ,h = 210):
    while True:
        if nowTime > l and nowTime < h:
            return nowTime
        else:
            if nowTime == 210:
                driver.refresh()
            nowTime = GetTime()
def main():
    LogIn()
    while True:
        try:
            url = 'http://www.yfcp885.com/lottery/SSC/1001'
            driver.get(url)
            nowTime = waitTime(GetTime() ,170)
            if nowTime > 170:
                wait_to_be_num()
                result_hou = PreAddNum('hou')
                if len(result_hou) == 2:
                    housan = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[6]'
                    send_all_me(housan,result_hou)
                    Buy()
                else:
                    PrintLog('BackNone\n')
                    print('新疆后三暂无符合')
            nowTime = waitTime(GetTime() ,130)
            if nowTime > 130:
                nowTime = GetTime()
                wait_to_be_num()
                result_zhong = PreAddNum('zhong')
                if len(result_zhong) == 2:
                    zhongsan = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[5]'
                    send_all_me(zhongsan,result_zhong)
                    Buy()
                else:
                    PrintLog('MidNone\n')
                    print('新疆中三暂无符合')
            nowTime = waitTime(GetTime() ,90)
            if nowTime > 90:
                nowTime = GetTime()
                wait_to_be_num()
                result_qian = PreAddNum('qian')
                if len(result_qian) == 2:
                    qiansan = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[4]'
                    send_all_me(qiansan,result_qian)
                    Buy()
                else:
                    PrintLog('FrontNone\n')
                    print('新疆前三暂无符合')
                time.sleep(20)
                os.system('cls')
        except Exception as e:
            #error = time.strftime("%H:%M:%S", time.localtime()) + '-' + 'ERROR:' + str(e) + '\n'
            #PrintLog(error)
            pass
if __name__ == '__main__':
    main()