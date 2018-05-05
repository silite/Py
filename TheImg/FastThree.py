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
Type = ['江苏', '安徽', '广西', '湖北', '北京', '河北', '甘肃', '上海']
THREE_1 = [1, 2, 3]
THREE_2 = [2, 3, 4]
THREE_3 = [3, 4, 5]
THREE_4 = [4, 5, 6]
THREE_5 = [5, 6, 7]
THREE_6 = [6, 7, 8]
FIVE_1 = [1, 2, 3, 4, 5]
FIVE_2 = [2, 3, 4, 5, 6]
FIVE_3 = [3, 4, 5, 6, 7]
FIVE_4 = [4, 5, 6, 7, 8]
SEVEN_1 = [1, 2, 3, 4, 5, 6, 7]
SEVEN_2 = [2, 3, 4, 5, 6, 7, 8]
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
        TheNewWeekResult_1 = []
        TheNewWeekResult_2 = []
        TheNewWeekResult_3 = []
        TheNewWeekResult_4 = []
        TheNewWeekResult_5 = []
        TheNewWeekResult_6 = []
        TheNewWeekResult_7 = []
        TheNewWeekResult_8 = []
        TheNewWeekResult_9 = []
        TheNewWeekResult_10 = []
        driver.get('http://www.yfcp885.com/lottery/K3/1401')
        table = PrettyTable()
        EitherDf = True
        for i in range(1, 10):
            if i == 4:
                Time = GetTime()
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
                temp_1 = GetText(xpath_1)
                temp_2 = GetText(xpath_2)
                if j == 1:
                    TheNewWeekResult_1.append([temp_1, temp_2])
                elif j == 2:
                    TheNewWeekResult_2.append([temp_1, temp_2])
                elif j == 3:
                    TheNewWeekResult_3.append([temp_1, temp_2])
                elif j == 4:
                    TheNewWeekResult_4.append([temp_1, temp_2])
                elif j == 5:
                    TheNewWeekResult_5.append([temp_1, temp_2])
                elif j == 6:
                    TheNewWeekResult_6.append([temp_1, temp_2])
                elif j == 7:
                    TheNewWeekResult_7.append([temp_1, temp_2])
                elif j == 8:
                    TheNewWeekResult_8.append([temp_1, temp_2])
                elif j == 9:
                    TheNewWeekResult_9.append([temp_1, temp_2])
                elif j == 10:
                    TheNewWeekResult_10.append([temp_1, temp_2])
                if temp_1 == '大':
                    temp_1 = color_red(temp_1)
                else:
                    temp_1 = Fore.LIGHTWHITE_EX + temp_1 + Fore.RESET
                if temp_2 == '单':
                    temp_2 = color_blue(temp_2)
                else:
                    temp_2 = Fore.LIGHTWHITE_EX + temp_2 + Fore.RESET
                temp = temp_1 + " " + temp_2
                result.append(temp)
            if EitherDf:
                table.add_column(Type[i - 1], result)
            else:
                table.add_column(Type[i - 2], result)
        Time = Time - 9
        for i in range(1, 7):
            big_1 = 0
            danshu_1 = 0
            big_2 = 0
            danshu_2 = 0
            big_3 = 0
            danshu_3 = 0
            big_4 = 0
            danshu_4 = 0
            big_5 = 0
            danshu_5 = 0
            big_6 = 0
            danshu_6 = 0
            big_7 = 0
            danshu_7 = 0
            big_8 = 0
            danshu_8 = 0
            big_9 = 0
            danshu_9 = 0
            big_10 = 0
            danshu_10 = 0

            if i == 1:
                THREE = THREE_1
                name = '1'
            elif i == 2:
                THREE = THREE_2
                name = '2'
            elif i == 3:
                THREE = THREE_3
                name = '3'
            elif i == 4:
                THREE = THREE_4
                name = '4'
            elif i == 5:
                THREE = THREE_5
                name = '5'
            elif i == 6:
                THREE = THREE_6
                name = '6'

            for j in range(3):
                if TheNewWeekResult_1[THREE[j] - 1][0] == '大':
                    big_1 += 1
                if TheNewWeekResult_1[THREE[j] - 1][1] == '单':
                    danshu_1 += 1
                if TheNewWeekResult_2[THREE[j] - 1][0] == '大':
                    big_2 += 1
                if TheNewWeekResult_2[THREE[j] - 1][1] == '单':
                    danshu_2 += 1
                if TheNewWeekResult_3[THREE[j] - 1][0] == '大':
                    big_3 += 1
                if TheNewWeekResult_3[THREE[j] - 1][1] == '单':
                    danshu_3 += 1
                if TheNewWeekResult_4[THREE[j] - 1][0] == '大':
                    big_4 += 1
                if TheNewWeekResult_4[THREE[j] - 1][1] == '单':
                    danshu_4 += 1
                if TheNewWeekResult_5[THREE[j] - 1][0] == '大':
                    big_5 += 1
                if TheNewWeekResult_5[THREE[j] - 1][1] == '单':
                    danshu_5 += 1
                if TheNewWeekResult_6[THREE[j] - 1][0] == '大':
                    big_6 += 1
                if TheNewWeekResult_6[THREE[j] - 1][1] == '单':
                    danshu_6 += 1
                if TheNewWeekResult_7[THREE[j] - 1][0] == '大':
                    big_7 += 1
                if TheNewWeekResult_7[THREE[j] - 1][1] == '单':
                    danshu_7 += 1
                if TheNewWeekResult_8[THREE[j] - 1][0] == '大':
                    big_8 += 1
                if TheNewWeekResult_8[THREE[j] - 1][1] == '单':
                    danshu_8 += 1
                if TheNewWeekResult_9[THREE[j] - 1][0] == '大':
                    big_9 += 1
                if TheNewWeekResult_9[THREE[j] - 1][1] == '单':
                    danshu_9 += 1
                if TheNewWeekResult_10[THREE[j] - 1][0] == '大':
                    big_10 += 1
                if TheNewWeekResult_10[THREE[j] - 1][1] == '单':
                    danshu_10 += 1
            if big_1 < 2:
                big_1 = color_blue(big_1)
            else:
                big_1 = color_red(big_1)
            table.add_column('三' + name, [color_red(str(big_1)) + ' | ' + color_blue(str(danshu_1)), color_red(str(big_2)) + ' | ' + color_blue(str(danshu_2)), color_red(str(big_3)) + ' | ' + color_blue(str(danshu_3)), color_red(str(big_4)) + ' | ' + color_blue(str(danshu_4)), color_red(str(big_5)) + ' | ' + color_blue(str(danshu_5)), color_red(str(big_6)) + ' | ' + color_blue(str(danshu_6)), color_red(str(big_7)) + ' | ' + color_blue(str(danshu_7)), color_red(str(big_8)) + ' | ' + color_blue(str(danshu_8)), color_red(str(big_9)) + ' | ' + color_blue(str(danshu_9)), color_red(str(big_10)) + ' | ' + color_blue(str(danshu_10))])
        for i in range(1, 5):
            big_1 = 0
            danshu_1 = 0
            big_2 = 0
            danshu_2 = 0
            big_3 = 0
            danshu_3 = 0
            big_4 = 0
            danshu_4 = 0
            big_5 = 0
            danshu_5 = 0
            big_6 = 0
            danshu_6 = 0
            big_7 = 0
            danshu_7 = 0
            big_8 = 0
            danshu_8 = 0
            big_9 = 0
            danshu_9 = 0
            big_10 = 0
            danshu_10 = 0
            if i == 1:
                FIVE = FIVE_1
                name = '1'
            elif i == 2:
                FIVE = FIVE_2
                name = '2'
            elif i == 3:
                FIVE = FIVE_3
                name = '3'
            elif i == 4:
                FIVE = FIVE_4
                name = '4'

            for j in range(5):
                if TheNewWeekResult_1[FIVE[j] - 1][0] == '大':
                    big_1 += 1
                if TheNewWeekResult_1[FIVE[j] - 1][1] == '单':
                    danshu_1 += 1
                if TheNewWeekResult_2[FIVE[j] - 1][0] == '大':
                    big_2 += 1
                if TheNewWeekResult_2[FIVE[j] - 1][1] == '单':
                    danshu_2 += 1
                if TheNewWeekResult_3[FIVE[j] - 1][0] == '大':
                    big_3 += 1
                if TheNewWeekResult_3[FIVE[j] - 1][1] == '单':
                    danshu_3 += 1
                if TheNewWeekResult_4[FIVE[j] - 1][0] == '大':
                    big_4 += 1
                if TheNewWeekResult_4[FIVE[j] - 1][1] == '单':
                    danshu_4 += 1
                if TheNewWeekResult_5[FIVE[j] - 1][0] == '大':
                    big_5 += 1
                if TheNewWeekResult_5[FIVE[j] - 1][1] == '单':
                    danshu_5 += 1
                if TheNewWeekResult_6[FIVE[j] - 1][0] == '大':
                    big_6 += 1
                if TheNewWeekResult_6[FIVE[j] - 1][1] == '单':
                    danshu_6 += 1
                if TheNewWeekResult_7[FIVE[j] - 1][0] == '大':
                    big_7 += 1
                if TheNewWeekResult_7[FIVE[j] - 1][1] == '单':
                    danshu_7 += 1
                if TheNewWeekResult_8[FIVE[j] - 1][0] == '大':
                    big_8 += 1
                if TheNewWeekResult_8[FIVE[j] - 1][1] == '单':
                    danshu_8 += 1
                if TheNewWeekResult_9[FIVE[j] - 1][0] == '大':
                    big_9 += 1
                if TheNewWeekResult_9[FIVE[j] - 1][1] == '单':
                    danshu_9 += 1
                if TheNewWeekResult_10[FIVE[j] - 1][0] == '大':
                    big_10 += 1
                if TheNewWeekResult_10[FIVE[j] - 1][1] == '单':
                    danshu_10 += 1
            table.add_column('五' + name, [color_red(str(big_1)) + ' | ' + color_blue(str(danshu_1)), color_red(str(big_2)) + ' | ' + color_blue(str(danshu_2)), color_red(str(big_3)) + ' | ' + color_blue(str(danshu_3)), color_red(str(big_4)) + ' | ' + color_blue(str(danshu_4)), color_red(str(big_5)) + ' | ' + color_blue(str(danshu_5)), color_red(str(big_6)) + ' | ' + color_blue(str(danshu_6)), color_red(str(big_7)) + ' | ' + color_blue(str(danshu_7)), color_red(str(big_8)) + ' | ' + color_blue(str(danshu_8)), color_red(str(big_9)) + ' | ' + color_blue(str(danshu_9)), color_red(str(big_10)) + ' | ' + color_blue(str(danshu_10))])
        for i in range(1, 3):
            big_1 = 0
            danshu_1 = 0
            big_2 = 0
            danshu_2 = 0
            big_3 = 0
            danshu_3 = 0
            big_4 = 0
            danshu_4 = 0
            big_5 = 0
            danshu_5 = 0
            big_6 = 0
            danshu_6 = 0
            big_7 = 0
            danshu_7 = 0
            big_8 = 0
            danshu_8 = 0
            big_9 = 0
            danshu_9 = 0
            big_10 = 0
            danshu_10 = 0
            if i == 1:
                SEVEN = SEVEN_1
                name = '1'
            elif i == 2:
                SEVEN = SEVEN_2
                name = '2'

            for j in range(7):
                if TheNewWeekResult_1[SEVEN[j] - 1][0] == '大':
                    big_1 += 1
                if TheNewWeekResult_1[SEVEN[j] - 1][1] == '单':
                    danshu_1 += 1
                if TheNewWeekResult_2[SEVEN[j] - 1][0] == '大':
                    big_2 += 1
                if TheNewWeekResult_2[SEVEN[j] - 1][1] == '单':
                    danshu_2 += 1
                if TheNewWeekResult_3[SEVEN[j] - 1][0] == '大':
                    big_3 += 1
                if TheNewWeekResult_3[SEVEN[j] - 1][1] == '单':
                    danshu_3 += 1
                if TheNewWeekResult_4[SEVEN[j] - 1][0] == '大':
                    big_4 += 1
                if TheNewWeekResult_4[SEVEN[j] - 1][1] == '单':
                    danshu_4 += 1
                if TheNewWeekResult_5[SEVEN[j] - 1][0] == '大':
                    big_5 += 1
                if TheNewWeekResult_5[SEVEN[j] - 1][1] == '单':
                    danshu_5 += 1
                if TheNewWeekResult_6[SEVEN[j] - 1][0] == '大':
                    big_6 += 1
                if TheNewWeekResult_6[SEVEN[j] - 1][1] == '单':
                    danshu_6 += 1
                if TheNewWeekResult_7[SEVEN[j] - 1][0] == '大':
                    big_7 += 1
                if TheNewWeekResult_7[SEVEN[j] - 1][1] == '单':
                    danshu_7 += 1
                if TheNewWeekResult_8[SEVEN[j] - 1][0] == '大':
                    big_8 += 1
                if TheNewWeekResult_8[SEVEN[j] - 1][1] == '单':
                    danshu_8 += 1
                if TheNewWeekResult_9[SEVEN[j] - 1][0] == '大':
                    big_9 += 1
                if TheNewWeekResult_9[SEVEN[j] - 1][1] == '单':
                    danshu_9 += 1
                if TheNewWeekResult_10[SEVEN[j] - 1][0] == '大':
                    big_10 += 1
                if TheNewWeekResult_10[SEVEN[j] - 1][1] == '单':
                    danshu_10 += 1
            table.add_column('七' + name, [color_red(str(big_1)) + ' | ' + color_blue(str(danshu_1)), color_red(str(big_2)) + ' | ' + color_blue(str(danshu_2)), color_red(str(big_3)) + ' | ' + color_blue(str(danshu_3)), color_red(str(big_4)) + ' | ' + color_blue(str(danshu_4)), color_red(str(big_5)) + ' | ' + color_blue(str(danshu_5)), color_red(str(big_6)) + ' | ' + color_blue(str(danshu_6)), color_red(str(big_7)) + ' | ' + color_blue(str(danshu_7)), color_red(str(big_8)) + ' | ' + color_blue(str(danshu_8)), color_red(str(big_9)) + ' | ' + color_blue(str(danshu_9)), color_red(str(big_10)) + ' | ' + color_blue(str(danshu_10))])
        while True:
            if Time == 0:
                Time = 599
            print(str(Time // 60) + ':' + str(Time - (Time // 60 * 60)))
            print(table)
            time.sleep(1)
            Time = Time - 1
            os.system('cls')
            if Time == 130:
                print("\a")
                break

if __name__ == '__main__':
    main()