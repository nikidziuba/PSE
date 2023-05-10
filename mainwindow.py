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
import subprocess
import demjson3


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
        self.tmp_file = home + '/TEMP/pse_temp.txt'

        filename = QFileDialog.getOpenFileName(
            parent=None,
            caption="Select Save File",
            dir=home + "/AppData/LocalLow/Kinetic Games/Phasmophobia/SaveFile.txt"
            )[0]
        if filename == None or filename == '':
            return
        self.global_filename = filename




        self.ui.bt_path.setDisabled(True)

        self.ui.box_level.setEnabled(True)
        self.ui.box_money.setEnabled(True)
        self.ui.bt_save_main.setEnabled(True)
        self.ui.bt_save.setEnabled(True)

        self.ui.bt_editor.setEnabled(True)
        self.ui.bt_value_save.setEnabled(True)
        self.ui.combo_key.setEnabled(True)
        self.ui.te_value.setEnabled(True)

        save_data = save_decode.decrypt(filename)

        self.save_data = save_data

        self.ui.combo_key.addItems(save_data.keys())

        money = self.save_data['PlayersMoney']['value']
        level = self.save_data['Level']['value']

        self.ui.box_money.setValue(int(money))
        self.ui.box_level.setValue(int(level))

    def save_main_button_clicked(self):

        money = self.ui.box_money.value()
        level = self.ui.box_level.value()

        self.save_data['PlayersMoney']['value'] = money
        self.save_data['Level']['value'] = level


    def key_combo_changed(self):
        key = self.ui.combo_key.currentText()
        value = str(self.save_data[key]['value'])

        self.ui.te_value.setPlainText(value)

    def save_button_clicked(self):

        filename = self.global_filename
        save_decode.encrypt(filename, self.save_data)

    def save_value_button_clicked(self):
        key = self.ui.combo_key.currentText()

        value = self.ui.te_value.toPlainText()

        value_type = self.save_data[key]['__type']

        if value_type == 'int':
            self.save_data[key]['value'] = int(value)
        elif value_type == 'float':
            self.save_data[key]['value'] = float(value)
        else:
            self.save_data[key]['value'] = value

        money = self.save_data['PlayersMoney']['value']
        level = self.save_data['Level']['value']

        self.ui.box_money.setValue(int(money))
        self.ui.box_level.setValue(int(level))


    def edit_button_clicked(self):
        save_decode.dump(self.tmp_file, self.save_data)
        subprocess.run('notepad.exe ' + self.tmp_file)
        self.ui.bt_load.setEnabled(True)

    def load_editor_button_clicked(self):
        with open(self.tmp_file, 'r') as f:
            self.save_data = demjson3.decode(f.read())
        money = self.save_data['PlayersMoney']['value']
        level = self.save_data['Level']['value']

        self.ui.box_money.setValue(int(money))
        self.ui.box_level.setValue(int(level))

        self.ui.bt_load.setEnabled(False)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
