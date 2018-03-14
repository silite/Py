import sys
from PyQt5 import QtWidgets,QtCore,QtGui

class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

        self.reset()

    def initUI(self):
        self.setWindowTitle('简易计算器')
        grid = QtWidgets.QGridLayout()

        self.display = QtWidgets.QLineEdit('0')
        self.display.setFont(QtGui.QFont("Times", 20))
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)
        grid.addWidget(self.display,0,0,1,4)

        names = ['Clear', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3 ),
               (4, 0), (4, 1), (4, 2), (4, 3)]
        c = 0
        for name in names:
            button = QtWidgets.QPushButton(name)
            button.setFixedSize(QtCore.QSize(60,30))
            button.clicked.connect(self.buttonClicked) # 给每个按钮设置信号/槽
            if c == 2:
                pass
                #grid.addWidget(QtWidgets.QLabel(''), 0, 2) #替换 第三个按钮 为 文本标签！
            else:
                grid.addWidget(button, pos[c][0]+1, pos[c][1])
            c = c + 1

        self.setLayout(grid)

    def buttonClicked(self):
        #sender = self.sender();  # 确定信号发送者
        #self.display.setText(sender.text())
        text = self.sender().text()
        if text in '+-*/':
            self.history.append(self.number) # 数字入栈
            self.history.append(text) # 运算符入栈
            self.operator = text # 设置当前运算符
            self.number = "" # 数字清空
            self.numberType = "int"
            return
        elif text == "=":
            self.calculate() # 计算
        elif text == "Back":
            pass
        elif text == "Clear":
            self.reset()
        elif text == "Close":
            self.close()
        elif text == ".":
            if self.numberType == "int":
                self.number += text
                self.numberType = "float"
        else:
            self.number = self.number + text if self.number != "0" else text

        self.display.setText(self.number)

    def calculate(self):
        pass

    def reset(self):
        self.number = "0"
        self.result = 0
        self.history = []
        self.operator = '' # +,-,*,/
        self.numberType = 'int' # int与float两种，如果输入了小数点则为实数

app = QtWidgets.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())