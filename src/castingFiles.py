import sys, os

fileName = sys.argv[1]

if fileName == "qrc":
    os.system(r"pyside6-rcc app3\src\autoFiles\qrc.qrc -o app3\src\autoFiles\qrc_rc.py")
else:
    os.system(r"pyside6-uic app3\src\uiFiles\{fileName}.ui -o app3\src\autoFiles\{fileName}_ui.py".format(fileName=fileName))