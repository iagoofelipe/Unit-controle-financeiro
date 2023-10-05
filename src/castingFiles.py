import sys, os

fileName = sys.argv[1]

if fileName == "qrc":
    os.system(r"pyside6-rcc temp\src\autoFiles\qrc.qrc -o temp\src\autoFiles\qrc_rc.py")
else:
    os.system(r"pyside6-uic temp\src\uiFiles\{fileName}.ui -o temp\src\autoFiles\{fileName}_ui.py".format(fileName=fileName))