from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from AssistantRelay import Ui_AssistantRelay
import requests
import keyboard
import os
from subprocess import call


# pyuic5 -x AssistantRelay.ui -o AssistantRelay.py
# pyinstaller --noconsole --icon=icon.ico AssistantRelayProg.py -n "Assistant Relay"

class AssistantRelay(QtWidgets.QMainWindow, Ui_AssistantRelay):
    def __init__(self, parent=None):
        super(AssistantRelay, self).__init__(parent)
        self.setupUi(self)

        # Initialize launch actions
        self.setWindowIcon(QIcon('icon.ico'))
        self.initialize_program()

        # REGION: LIGHTS
        self.lightsOffButton.clicked.connect(self.lights_off)
        self.lightsOnButton.clicked.connect(self.lights_on)

    def showWindow(self):
        self.show()

    def keyPressEvent(self, event):
        import PyQt5.QtCore as core
        if event.key() == core.Qt.Key_F1:
            self.light_control('off', 'potato and ninja')
        elif event.key() == core.Qt.Key_F2:
            self.light_control('on', 'potato and ninja')

    def initialize_program(self):
        print("Initializing Program")
        self.allLightCheckBox.setChecked(True)
        print("Program Initialized")

    def light_control(self, setting, light):
        url = "http://192.168.0.101:3000/assistant"
        full_command = light + " " + setting
        payload = "{\r\n    \"user\": \"js-teoh\",\r\n    \"command\": \"turn " + full_command + "\",\r\n    \"converse\": false,\r\n    \"broadcast\": false\r\n}"
        headers = {
            'AssistantRelay': '',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text.encode('utf8'))

    def lights_off(self):
        if self.allLightCheckBox.isChecked():
            print("Turning all lights off.")
            self.light_control('off', 'potato and ninja')
        elif self.potatoLightCheckBox.isChecked():
            print("Turning Potato light off.")
            self.light_control('off', 'potato')
        elif self.ninjaLightCheckBox.isChecked():
            print("Turning Ninja light off.")
            self.light_control('off', 'ninja')

    def lights_on(self):
        if self.allLightCheckBox.isChecked():
            print("Turning all lights on.")
            self.light_control('on', 'potato and ninja')
        elif self.potatoLightCheckBox.isChecked():
            print("Turning Potato light on.")
            self.light_control('on', 'potato')
        elif self.ninjaLightCheckBox.isChecked():
            print("Turning Ninja light on.")
            self.light_control('on', 'ninja')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    assistant_relay = AssistantRelay()

    # app.setQuitOnLastWindowClosed(False)

    # Adding an icon
    icon = QIcon("icon.jpg")

    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Creating the options
    menu = QMenu()
    option1 = QAction("Assistant Relay")
    option1.triggered.connect(lambda: assistant_relay.showWindow())
    menu.addAction(option1)

    lightson = QAction("Lights On")
    lightson.triggered.connect(lambda: assistant_relay.light_control('on', 'potato and ninja'))
    menu.addAction(lightson)

    lightsoff = QAction("Lights Off")
    lightsoff.triggered.connect(lambda: assistant_relay.light_control('off', 'potato and ninja'))
    menu.addAction(lightsoff)

    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    assistant_relay.show()
    sys.exit(app.exec_())
