from PySide6.QtCore import QTimer, QObject

class Timer:
    def __init__(self, parent: QObject | None):
        self._qtimer = QTimer(parent)
        self._slots = dict()

    def setTimer(self, msec: int) -> None:
        self._qtimer.setInterval(msec)

    def start(self, msec=None) -> None:
        if msec != None:
            self.setTimer(msec)
        
        for _, slot in self._slots.items():
            self._qtimer.timeout.connect(slot)
        self._qtimer.start()
    
    def stop(self) -> None:
        self._qtimer.stop()

    def addSlot(self, slot: object) -> None:
        self._slots[len(self._slots)] = slot

    def clearSlots(self) -> None:
        self._slots = dict()
        self.stop()