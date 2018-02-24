
from selenium import webdriver
import time,re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = ''
pwd = ''
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 120)
comp = ['0156','1267','2358','3469','0457','1458','2369','0378','1489','0259']
def JudgeRe(list_):

    num_1 = list_[0].split(',') #中奖号码1
    num_2 = list_[1].split(',') #同
    temp = comp[int(num_2[3])]
    if num_1[2] in temp or num_1[3] in temp or num_1[4] in temp:
        return '0156'
    else:
        return temp
def OpStr(result):
    if len(result) == 0:
        return 0
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
    driver.find_element_by_xpath(x).click()
try:
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
    driver.get('http://www.yfcp885.com/lottery/SSC/1000')
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[2]/td[2]/i')) #加载第二个
    )
    result = OpStr(JudgeRe(re.compile('class="numbers">(.*?)<').findall(driver.page_source)))
    print(result)
    #sure = wait.until(
    #    EC.element_to_be_clickable((By.XPATH,'//*[@id="layermbox0"]/div[2]/div/div/div[2]/span'))
    #)
    #sure.click()
    housan = wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[6]'))
    )
    housan.click()
    print("dwadaw")
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
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/a')
except:pass