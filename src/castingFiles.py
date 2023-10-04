import sys, os

fileName = sys.argv[1]

if fileName == "qrc":
    os.system(r"pyside6-rcc Include\src\autoFiles\qrc.qrc -o Include\src\autoFiles\qrc_rc.py")
else:
    os.system(r"pyside6-uic Include\src\uiFiles\{fileName}.ui -o Include\src\autoFiles\{fileName}_ui.py".format(fileName=fileName))