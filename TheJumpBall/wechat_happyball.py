from PIL import Image
import os
import screenshot
screenshot.GetScreenShot()
im = Image.open("./happyball.png")
RGBList = im.getdata()

WIDTH = 1080
BLOCK_RGB = (59, 59, 59, 255)  #块平台RGBA
CENTER_SCREEN_WIDTH = 540 #屏幕中心宽
CENTER_FIRST_BLOCK = 731  #第一层块中心高
FIRST_BLOCK_LEFT = 300    #预设纵向扫描左间距
START_LEFT = 112          #开始扫描初始化
LEFT_BLOCK_BORDER = 0     #扫到的左边下落点

def Get_LEFT_BLOCK_BORDER():
    """
        获得左边下落点
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
        if NOW_RGB == (57, 57, 57, 255): #RGBA为块阴影
            print("左块阴影")
            break
        if NOW_RGB[0] > 150:
            print("白墙")
            return CENTER_SCREEN_WIDTH - LEFT_BLOCK_BORDER + 100
    print(LEFT_BLOCK_BORDER)
    """
        当出现上述角度过大时  纵向扫描
    """
    if LEFT_BLOCK_BORDER < 315 or LEFT_BLOCK_BORDER > 530:
        print("过角度")
        for iter_height in range(250):
            if RGBList[FIRST_BLOCK_LEFT + (CENTER_FIRST_BLOCK - iter_height) * WIDTH] != BLOCK_RGB:
                LEFT_BLOCK_BORDER += iter_height #应计算旋转角度后的长度  暂定需修改
                break
    """
        左侧无 超出阈值
    """
    if LEFT_BLOCK_BORDER == 766:
        LEFT_BLOCK_BORDER = 0

    return LEFT_BLOCK_BORDER

def main():
    LEFT_BLOCK_BORDER = Get_LEFT_BLOCK_BORDER()
    print(LEFT_BLOCK_BORDER)
    if LEFT_BLOCK_BORDER > 600:
        distance = LEFT_BLOCK_BORDER // 2.8
    elif 600 >= LEFT_BLOCK_BORDER > 400:
        distance = LEFT_BLOCK_BORDER // 2.6
    elif 400 >= LEFT_BLOCK_BORDER > 200:
        distance = LEFT_BLOCK_BORDER // 2.4
    else:
        distance = LEFT_BLOCK_BORDER // 2.2
    os.system('adb shell input swipe 0 0 ' + str(distance) + ' ' + str(distance))

if __name__ == '__main__':
    main()