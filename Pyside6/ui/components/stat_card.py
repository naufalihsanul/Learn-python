
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout, QFrame


class StatCard(QFrame):
    def __init__(self,title:str,value:str):
        super().__init__()

        self.setObjectName("statCard")

        layout = QVBoxLayout(self)

        self.lbl_title = QLabel(value)
        self.lbl_title.setObjectName("statTitle")

        layout.addWidget(self.lbl_title)

        self.lbl_val = QLabel(value)
        self.lbl_val.setObjectName("statValue")

        layout.addWidget(self.lbl_val)
    
    def set_value(self,new_value:str):
        self.lbl_val.setText(new_value)
