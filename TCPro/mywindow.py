from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__(None, Qt.FramelessWindowHint)# 设置为顶级窗口，无边框
        self.initUI()
        
    def initUI(self):
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    def drawShadow(self, painter):
        #绘制左上角、左下角、右上角、右下角、上、下、左、右边框
        self.SHADOW_WIDTH = 8
        self.pixmaps = []
        self.pixmaps.append(str("./img/shadow/left_top.png"))
        self.pixmaps.append(str("./img/shadow/left_bottom.png"))
        self.pixmaps.append(str("./img/shadow/right_top.png"))
        self.pixmaps.append(str("./img/shadow/right_bottom.png"))
        self.pixmaps.append(str("./img/shadow/top_mid.png"))
        self.pixmaps.append(str("./img/shadow/bottom_mid.png"))
        self.pixmaps.append(str("./img/shadow/left_mid.png"))
        self.pixmaps.append(str("./img/shadow/right_mid.png"))

        painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[0]))   #左上角
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[2]))   #右上角
        painter.drawPixmap(0,self.height()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[1]))   #左下角
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, self.height()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[3]))  #右下角
        painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH, QPixmap(self.pixmaps[6]).scaled(self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH)) #左
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH, QPixmap(self.pixmaps[7]).scaled(self.SHADOW_WIDTH, self.height()- 2*self.SHADOW_WIDTH)) #右
        painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[4]).scaled(self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH)) #上
        painter.drawPixmap(self.SHADOW_WIDTH, self.height()-self.SHADOW_WIDTH, self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[5]).scaled(self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH))   #下

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width()-2*self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH))