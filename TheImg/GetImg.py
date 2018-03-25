import urllib.request
grade = '17'
error = 0
for profinal in range(1, 21):
    for academic in range(1, 8):
        for class_ in range(1, 8):
            if error > 40:
                error = 0
                break
            for one in range(1, 37):
                ImgName = grade + str('%02d'%profinal) + str('%02d'%academic) + str('%02d'%class_) + str('%02d'%one)
                print(ImgName)
                try:
                    response = urllib.request.urlopen("http://kdjw.hnust.cn/kdjw/uploadfile/studentphoto/pic/" + ImgName + ".JPG")
                    img = response.read()
                    with open("17/" + ImgName + ".jpg", 'wb') as f:
                        f.write(img)
                except Exception as e:
                    try:
                        print("小写")
                        response = urllib.request.urlopen("http://kdjw.hnust.cn/kdjw/uploadfile/studentphoto/pic/" + ImgName + ".jpg")
                        img = response.read()
                        with open("17/" + ImgName + ".jpg", 'wb') as f:
                            f.write(img)
                    except Exception as f:
                        error += 1
