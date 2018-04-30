from selenium import webdriver
import re, time, sys, os
from prettytable import PrettyTable
# from colorama import Fore, init
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'silite'
pwd = 'silite'
# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
# driver = webdriver.Firefox(firefox_options=fireFoxOptions)
driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
Type = ['江苏', '安徽', '广西', '湖北', '北京', '河北', '甘肃', '上海', '贵州', '吉林']
# init(autoreset = False)
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
def click(x):
    time.sleep(0.3)
    driver.find_element_by_xpath(x).click()
    time.sleep(0.3)
def FastClick(x):
    driver.find_element_by_xpath(x).click()
def GetText(xpath):
    return driver.find_element_by_xpath(xpath).text
def main():
    LogIn()
    while True:
        x = input("按n\n")
        if x == 'n':
            driver.get('http://www.yfcp885.com/lottery/K3/1401')
            table = PrettyTable()
            EitherDf = True
            Unlike_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, " "]
            Unlike_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, " "]
            Unlike_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, " "]
            for i in range(1, 12):
                if i == 6:
                    EitherDf = False
                    for j in range(5):
                        FastClick('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/a[2]')
                    continue
                xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/ul/li[ ' + str(i) + ' ]'
                click(xpath)
                result = []
                for j in range(1, 11):
                    xpath_1 = '//*[@id="fn_getoPenGame"]/tbody[2]/tr[' + str(j) + ']/td[4]/em[1]'
                    xpath_2 = '//*[@id="fn_getoPenGame"]/tbody[2]/tr[' + str(j) + ']/td[4]/em[2]'
                    temp = GetText(xpath_1) + " " + GetText(xpath_2)
                    result.append(temp)
                if i < 10:
                    for k in range(9):
                        if result[k][0] != result[k + 1][0]:
                            Unlike_1[k] += 1
                        if result[k][2] != result[k + 1][2]:
                            Unlike_1[k] += 1
                else:
                    for k in range(9):
                        if result[k][0] != result[k + 1][0]:
                            Unlike_2[k] += 1
                        if result[k][2] != result[k + 1][2]:
                            Unlike_2[k] += 1
                if EitherDf:
                    table.add_column(Type[i - 1], result)
                else:
                    table.add_column(Type[i - 2], result)
                if i == 9:
                    table.add_column("异值1", Unlike_1)
                elif i == 11:
                    table.add_column("异值2", Unlike_2)
                    for s in range(9):
                        Unlike_3[s] = Unlike_1[s] + Unlike_2[s]
                    table.add_column("异值和", Unlike_3)
            print(table)
if __name__ == '__main__':
    main()