from PySide6.QtCore import QRunnable, Slot

class Worker(QRunnable):
    '''
    Worker thread
    '''
    def __init__(self, slot, *args, **kwargs) -> None:
        super().__init__()        
        self.slot = slot
        self.args = args
        self.kwargs = kwargs

    @Slot()  # QtCore.Slot
    def run(self):
        if self.kwargs != {} and self.args != ():
            self.slot(*self.args, **self.kwargs)
            return
        
        if self.args != ():
            self.slot(*self.args)
        
        elif self.kwargs != {}:
            self.slot(**self.kwargs)
        
        else:
            self.slot()