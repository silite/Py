from selenium import webdriver
import re, time, sys, os
from prettytable import PrettyTable
from colorama import Fore, init
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'silite'
pwd = 'silite'
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(firefox_options=fireFoxOptions)
# driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
Type = ['江', '安', '广', '湖', '北', '河', '甘', '上']
THREE_1 = [1, 2, 3]
THREE_2 = [2, 3, 4]
THREE_3 = [3, 4, 5]
THREE_4 = [4, 5, 6]
THREE_5 = [5, 6, 7]
THREE_6 = [6, 7, 8]
init(autoreset = False)
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
def GetTime():
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH , '/html/body/div/div[2]/div[1]/div[2]/em'))
    )
    time.sleep(1)
    Time = GetText('/html/body/div/div[2]/div[1]/div[2]/em')
    if len(Time) != 8:
        print("已停售")
        input()
        sys.exit()
    return int(Time[-5] + Time[-4]) * 60 + int(Time[-2] + Time[-1])
def color_red(x):
    return Fore.LIGHTRED_EX + str(x) + Fore.RESET
def color_blue(x):
    return Fore.LIGHTBLUE_EX + str(x) + Fore.RESET
def main():
    LogIn()
    while True:
        TheNewWeekResult = [[], [], [], [], [], [], [], [], [], []]
        noColor_TheNewWeekResult = [[], [], [], [], [], [], [], [], [], []]
        driver.get('http://www.yfcp885.com/lottery/K3/1401')
        table = PrettyTable()
        EitherDf = True
        for i in range(1, 10):
            if i == 1:
                Time = GetTime()
            if i == 6:
                EitherDf = False
                for j in range(5):
                    FastClick('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/a[2]')
                continue
            xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/ul/li[ ' + str(i) + ' ]'
            click(xpath)
            result_1 = []
            for j in range(1, 11):
                xpath_1 = '//*[@id="fn_getoPenGame"]/tbody[2]/tr[' + str(j) + ']/td[4]/em[1]'
                xpath_2 = '//*[@id="fn_getoPenGame"]/tbody[2]/tr[' + str(j) + ']/td[4]/em[2]'
                temp_1 = GetText(xpath_1)
                temp_2 = GetText(xpath_2)
                TheNewWeekResult[j - 1].append([temp_1, temp_2])
                noColor_TheNewWeekResult[j - 1].append([temp_1, temp_2])
                if temp_1 == '大':
                    temp_1 = color_red(temp_1)
                else:
                    temp_1 = Fore.LIGHTWHITE_EX + temp_1 + Fore.RESET
                result_1.append(temp_1)
            if EitherDf:
                table.add_column(Type[i - 1], result_1)
            else:
                table.add_column(Type[i - 2], result_1)
        EitherDf = True
        for k in range(8):
            result_2 = []
            for j in range(1, 11):
                temp_2 = TheNewWeekResult[j - 1][k][1]
                if temp_2 == '单':
                    temp_2 = color_blue(temp_2)
                else:
                    temp_2 = Fore.LIGHTWHITE_EX + temp_2 + Fore.RESET
                result_2.append(temp_2)
            if EitherDf:
                table.add_column(Type[k], result_2)
            else:
                table.add_column(Type[k], result_2)
        Time = Time - 12
        result_3 = [[], [], [], [], [], [], [], [], [], []]
        result_4 = [[], [], [], [], [], [], [], [], [], []]
        for i in range(1, 7):
            big = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            danshu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            if i == 1:
                THREE = THREE_1
            elif i == 2:
                THREE = THREE_2
            elif i == 3:
                THREE = THREE_3
            elif i == 4:
                THREE = THREE_4
            elif i == 5:
                THREE = THREE_5
            elif i == 6:
                THREE = THREE_6

            for j in range(3):
                for k in range(10):
                    if TheNewWeekResult[k][THREE[j] - 1][0] == '大':
                        big[k] += 1
                    if TheNewWeekResult[k][THREE[j] - 1][1] == '单':
                        danshu[k] += 1
            for x in range(10):
                if big[x] < 2:
                    big[x] = color_blue(big[x])
                else:
                    big[x] = color_red(big[x])
                if danshu[x] < 2:
                    danshu[x] = color_blue(danshu[x])
                else:
                    danshu[x] = color_red(danshu[x])
                result_3[i - 1].append(big[x])
                result_4[i - 1].append(danshu[x])
        for i in range(1, 7):
            table.add_column('大' + str(i), result_3[i - 1])
        for i in range(1, 7):
            table.add_column('单' + str(i), result_4[i - 1])
        table_2 = PrettyTable()
        big_either = []
        danshu_either = []
        for i in range(6):
            for j in range(2):
                either = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                for k in range(9):
                    for x in range(3):
                        if noColor_TheNewWeekResult[k][i + x][j] != noColor_TheNewWeekResult[k + 1][i + x][j]:
                            either[k] += 1
                    if either[k] < 2:
                        either[k] = color_blue(either[k])
                    else:
                        either[k] = color_red(either[k])
                if j == 0:
                    big_either.append(either)
                else:
                    danshu_either.append(either)
        for i in range(2):
            if i == 0:
                name = '大'
                list_ = big_either
            else:
                name = '单'
                list_ = danshu_either
            for j in range(6):
                table_2.add_column(name + str(j + 1), list_[j])
        while True:
            if Time == 0:
                Time = 599

            print(str(Time // 60) + ':' + str(Time - (Time // 60 * 60)))
            print(table)
            print(table_2)
            time.sleep(1)
            Time = Time - 1
            os.system('cls')
            if Time == 310:
                print("\a")
                break

if __name__ == '__main__':
    main()