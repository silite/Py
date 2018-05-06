from PIL import Image
import os, screenshot, time, sys

WIDTH = 1080
BLOCK_RGB = (59, 59, 59, 255)  #块平台RGBA
CENTER_SCREEN_WIDTH = 540
CENTER_FIRST_BLOCK = 731  #第一层块中心高
FIRST_BLOCK_LEFT = 300    #预设纵向扫描左间距
FIRST_BLOCK_RIGHT = 780
START_LEFT = 112          #开始扫描初始化
START_RIGHT = 960
LEFT_BLOCK_BORDER = 0     #预设扫到的左边下落点
RIGHT_BLOCK_BORDER = 0
ORANGE_BLOCK_RGB = (255, 117, 70, 255)
OVER_BACK_RGB = (79, 79, 80, 255)

def Get_LEFT_BLOCK_BORDER():
    """
        获得左侧下落点
    """
    """
        寻找左边界 START_LEFT
    """
    # while True:
    #     if RGBList[CENTER_FIRST_BLOCK * WIDTH + START_LEFT] == BLOCK_RGB:
    #         break
    #     else:
    #         START_LEFT += 1
    """
        左面
        第一层START_LEFT扫到球落点溅射左
    """

    for iter_width in range(START_LEFT, CENTER_SCREEN_WIDTH):
        NOW_RGB = RGBList[CENTER_FIRST_BLOCK * WIDTH + iter_width]
        LEFT_BLOCK_BORDER = iter_width
        if NOW_RGB == (57, 57, 57, 255) and LEFT_BLOCK_BORDER < 490: #RGBA为块阴影 后者规避落点球颜色重合
            if LEFT_BLOCK_BORDER < 150:  #遇到刚开始向右扫描时就扫到上述阴影
                return 400 #需修改
            break
        if NOW_RGB[0] > 150 and NOW_RGB != ORANGE_BLOCK_RGB:
            return CENTER_SCREEN_WIDTH - LEFT_BLOCK_BORDER + 100
    """
        当出现上述角度过大时  纵向扫描
    """
    if LEFT_BLOCK_BORDER < 200 or LEFT_BLOCK_BORDER > 530: #原小于315
        for iter_height in range(250):
            NOW_RGB = RGBList[FIRST_BLOCK_LEFT + (CENTER_FIRST_BLOCK - iter_height) * WIDTH]
            if NOW_RGB != BLOCK_RGB:
                LEFT_BLOCK_BORDER += iter_height #应计算旋转角度后的长度  暂定需修改
                break
    """
        左侧无 超出阈值
    """
    if LEFT_BLOCK_BORDER == 766:
        LEFT_BLOCK_BORDER = 0

    return LEFT_BLOCK_BORDER

def Get_RIGHT_BLOCK_BORDER():
    """
        获得右侧下落点
    """

    """
        右面
        第一层START_LEFT扫到球落点溅射右
    """

    for iter_width in range(START_RIGHT, CENTER_SCREEN_WIDTH, -1):
        NOW_RGB = RGBList[CENTER_FIRST_BLOCK * WIDTH + iter_width]
        RIGHT_BLOCK_BORDER = iter_width
        if NOW_RGB[0] == NOW_RGB[1] == NOW_RGB[2] and NOW_RGB[0] < 59: #需修改
            if RIGHT_BLOCK_BORDER > 800:
                return 400
            break
        if NOW_RGB[0] > 150 and NOW_RGB != ORANGE_BLOCK_RGB:
            return RIGHT_BLOCK_BORDER - CENTER_SCREEN_WIDTH + 100
    print(RIGHT_BLOCK_BORDER)
    """
        当出现上述角度过大时  纵向扫描
    """
    RIGHT_BLOCK_BORDER = WIDTH - RIGHT_BLOCK_BORDER
    if RIGHT_BLOCK_BORDER < 200 or RIGHT_BLOCK_BORDER > 530:
        print("角度过大")
        for iter_height in range(250):
            NOW_RGB = RGBList[FIRST_BLOCK_RIGHT + (CENTER_FIRST_BLOCK - iter_height) * WIDTH]
            if NOW_RGB != BLOCK_RGB:
                RIGHT_BLOCK_BORDER += iter_height
                break

    return RIGHT_BLOCK_BORDER


def GetSwipeDistance(border):
    if border > 650:
        distance = border // 1.8
    elif 650 >= border > 400:
        distance = border // 2.6
    elif 400 >= border:
        distance = border // 2.2
    else:
        distance = 0
    return str(distance)

def SwipeScreen(method, distance):
    if method == 'left':
        os.system('adb shell input swipe 0 0 ' + distance + ' ' + distance)
    else:
        os.system('adb shell input swipe ' + distance + ' ' + distance + ' 0 0')

def main():
    while True:
        screenshot.GetScreenShot()
        im = Image.open("./happyball.png")
        global RGBList
        RGBList = im.getdata()
        if RGBList[WIDTH * 20 + CENTER_SCREEN_WIDTH] != OVER_BACK_RGB:
            LEFT_BLOCK_BORDER = Get_LEFT_BLOCK_BORDER()
            if LEFT_BLOCK_BORDER != 0:
                method = 'left'
                distance = GetSwipeDistance(LEFT_BLOCK_BORDER)
                SwipeScreen(method, distance)
            else:
                RIGHT_BLOCK_BORDER = Get_RIGHT_BLOCK_BORDER()
                method = 'right'
                distance = GetSwipeDistance(RIGHT_BLOCK_BORDER)
                SwipeScreen(method, distance)
            time.sleep(2)
        else:
            print('游戏结束')
            input()
            sys.exit()

if __name__ == '__main__':
    main()