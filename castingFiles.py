import sys, os

fileName = sys.argv[1]

if fileName == "qrc":
    os.system(r"pyside6-rcc resources\autoFiles\qrc.qrc -o resources\autoFiles\qrc_rc.py")
else:
    os.system(r"pyside6-uic resources\uiFiles\{fileName}.ui -o resources\autoFiles\{fileName}_ui.py".format(fileName=fileName))