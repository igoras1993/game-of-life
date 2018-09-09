from __future__ import division
import numpy as np
import sys
from scipy.signal import convolve as conv
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GUI_res import Ui_Main_Widget
import cv2

class Board():

    def __init__(self, vert_sz=7, horz_sz=7):
        self.__size = (vert_sz, horz_sz)
        self.curr_board_array = np.zeros(self.__size, dtype=np.uint8)
        self.__next_board_array = np.zeros(self.__size, dtype=np.uint8)
        self.__kernel = np.ones((3,3), dtype=np.uint8)
        self.__kernel[1, 1] = 0
    def conway_unit_step(self):

        self.curr_board_array = self.__next_board_array.copy()

        # alive pixels counts
        convoluted1 = conv(self.curr_board_array, self.__kernel, mode='same')
        mask1 = np.logical_and(np.logical_and(convoluted1>=2, convoluted1<=3), self.curr_board_array==1)

        # alive pixels do not count
        convoluted2 = conv(self.curr_board_array, self.__kernel, mode='same')
        mask2 = convoluted2==3

        self.__next_board_array = (np.logical_or(mask1, mask2)*1).astype(np.uint8)

    def update_next(self):

        # alive pixels counts
        convoluted1 = conv(self.curr_board_array, self.__kernel, mode='same')
        mask1 = np.logical_and(np.logical_and(convoluted1>=2, convoluted1<=3), self.curr_board_array==1)

        # alive pixels do not count
        convoluted2 = conv(self.curr_board_array, self.__kernel, mode='same')
        mask2 = convoluted2==3

        self.__next_board_array = (np.logical_or(mask1, mask2)*1).astype(np.uint8)

    def set_board_random(self):
        self.__next_board_array = ((np.random.rand(self.__size[0], self.__size[1])>0.5)*1).astype(np.uint8)
        self.conway_unit_step()

    def as_uint8_image(self, array):
        return ((array>0)*255).astype(np.uint8)


class GUI(QWidget, Ui_Main_Widget):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon("Icon.png"))

        self.last_x = int(self.sb_x.text())
        self.last_y = int(self.sb_y.text())

        self.game = Board(vert_sz=self.last_y, horz_sz=self.last_x)
        self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)

        self.label.clear()
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))
        self.label.show()
        self.timer = QTimer(self)
        self.timer.setInterval(self.hs_interv.value())
        self.timer.timeout.connect(self.refresh)

        self.label.mouseMoveEvent = self.moveMouseOverLabel
        self.label.mousePressEvent = self.pressMouse
        self.resizeEvent = self.resize_ev

        self.__rigcz_cnt = 0

        #SiGNALS
        self.connect(self.pb_Start, SIGNAL('clicked()'), self.pb_start_clk)
        self.connect(self.pb_Stop, SIGNAL('clicked()'), self.pb_stop_clk)
        self.connect(self.pb_Random, SIGNAL('clicked()'), self.pb_random_clk)
        self.connect(self.hs_interv, SIGNAL('valueChanged(int)'), self.hs_interv_change)
        self.connect(self.pb_Next, SIGNAL('clicked()'), self.pb_next_clk)

    def pb_start_clk(self):
        if (self.game._Board__size[1] != int(self.sb_x.text())) or (self.game._Board__size[0] != int(self.sb_y.text())):
            self.game = Board(vert_sz=int(self.sb_y.text()), horz_sz=int(self.sb_x.text()))
        self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))
        self.timer.start()

    def pb_stop_clk(self):
        self.timer.stop()

    def pb_random_clk(self):
        self.game = Board(vert_sz=int(self.sb_y.text()), horz_sz=int(self.sb_x.text()))
        self.game.set_board_random()
        self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))

    def pb_next_clk(self):
        self.game.conway_unit_step()
        self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))

    def hs_interv_change(self, value):
        self.timer.setInterval(value)


    def qPxMapFromNpGrayArray(self, image_gray, negation = False):

        if negation:
            bytesBuffer = (255 - cv2.cvtColor((image_gray/3).astype(np.uint8), cv2.COLOR_GRAY2RGB)).tobytes()
        else:
            bytesBuffer = cv2.applyColorMap((255 - cv2.cvtColor((image_gray/3).astype(np.uint8), cv2.COLOR_GRAY2RGB)),cv2.COLORMAP_JET).tobytes()

        return QPixmap().fromImage(QImage(bytesBuffer,
                                    image_gray.shape[1],
                                    image_gray.shape[0],
                                    3 * image_gray.shape[1],
                                    QImage.Format_RGB888))

    def refresh(self):
        self.game.conway_unit_step()
        self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))

    def pressMouse(self, event):

        x = event.pos().x()
        y = event.pos().y()
        x_idx = int((x/self.label.width())*self.game._Board__size[1])
        y_idx = int((y/self.label.height())*self.game._Board__size[0])

        # use buttons() instead of button() when dealing with move instead of press
        if event.button() == Qt.RightButton:
            self.game.curr_board_array[y_idx, x_idx] = 0
        elif event.button() == Qt.LeftButton:
            self.game.curr_board_array[y_idx, x_idx] = 1


        self.game.update_next()
        self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))


    def moveMouseOverLabel(self, event):
        self.__rigcz_cnt += 1

        x = event.pos().x()
        y = event.pos().y()
        x_idx = int((x/self.label.width())*self.game._Board__size[1])
        y_idx = int((y/self.label.height())*self.game._Board__size[0])

        try:
            # use buttons() instead of button() when dealing with move instead of press
            if event.buttons() == Qt.RightButton:
                self.game.curr_board_array[y_idx, x_idx] = 0
            elif event.buttons() == Qt.LeftButton:
                self.game.curr_board_array[y_idx, x_idx] = 1

            if self.__rigcz_cnt % 10 == 0:
                self.game.update_next()
                self.curr_image = self.game.as_uint8_image(self.game.curr_board_array)
                self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                        self.label.height(),
                                                                                        Qt.IgnoreAspectRatio))
        except:
            pass


    def resize_ev(self, event):
        self.label.setPixmap(self.qPxMapFromNpGrayArray(self.curr_image).scaled(self.label.width(),
                                                                                self.label.height(),
                                                                                Qt.IgnoreAspectRatio))


app = QApplication(sys.argv)
form = GUI()
form.show()
app.exec_()
