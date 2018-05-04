import os

def GetScreenShot():
    os.system('adb shell screencap -p /sdcard/happyball.png')
    os.system('adb pull /sdcard/happyball.png .')