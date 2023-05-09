# This Python file uses the following encoding: utf-8
import sys
import save_decode
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide6.QtCore import QDir, Qt, QPoint
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.global_filename = ''

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def min_button_clicked(self):

        self.showMinimized()

    def exit_button_clicked(self):
        sys.exit(0)


    def path_button_clicked(self):
        home = QDir.homePath()
        filename = QFileDialog.getOpenFileName(
            parent=None,
            caption="Select Save File",
            dir=home + "/AppData/LocalLow/Kinetic Games/Phasmophobia/SaveFile.txt"
            )[0]
        if filename == None or filename == '':
            return
        self.global_filename = filename

        self.ui.label_filename.setText(filename.split('/')[-1])


        self.ui.bt_path.setDisabled(True)

        self.ui.box_level.setEnabled(True)
        self.ui.box_money.setEnabled(True)
        self.ui.bt_save.setEnabled(True)

        (money, level) = save_decode.get_info(filename)
#        print(money, level)
        self.ui.box_money.setValue(int(money))
        self.ui.box_level.setValue(int(level))

    def save_button_clicked(self):
        filename = self.global_filename
        money = self.ui.box_money.value()
        level = self.ui.box_level.value()
        save_decode.change_info(filename, money, level)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
