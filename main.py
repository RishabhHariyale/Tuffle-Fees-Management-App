
from PyQt5.QtWidgets import QMainWindow,QApplication
from subsystem.main_win import Main_UI
from subsystem.menu_ui import Menu_Frame
from subsystem.add_new_batch_ui import Add_New_Batch_Frame
import sys
class Menu_App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Main_UI()
        self.ui.setupUi(self)
        self.menuFrame=Menu_Frame(self.ui.centralwidget)
        self.ui.verticalLayout_3.addWidget(self.menuFrame.frame_menu)
        self.ui.resetLayout()
        self.currentFrame=None

        self.menuFrame.pushButton_addNewBatch.pressed.connect(lambda: self.showAddNewBatch())
        self.ui.pushButton_back.pressed.connect(lambda: self.backToMenu())
        self.show()

    def backToMenu(self):
        self.currentFrame.frame_addNewBatch.close()
        del self.currentFrame
        self.menuFrame.frame_menu.show()
        self.ui.resetLayout()
        
    def showAddNewBatch(self):
        self.menuFrame.frame_menu.hide()
        self.newBatchFrame=Add_New_Batch_Frame(self.ui.centralwidget)
        self.currentFrame=self.newBatchFrame
        self.ui.verticalLayout_3.addWidget(self.newBatchFrame.frame_addNewBatch)
        self.ui.resetLayout()

    


if __name__=="__main__":
    app=QApplication(sys.argv)
    menu_obj=Menu_App()
    sys.exit(app.exec_())