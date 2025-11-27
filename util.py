from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton
)

import load
import shared

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("UploadTestRepo")

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.lbl_test = QLabel("This is a test label")
        self.lbl_test.setStyleSheet("font-size: 10pt;")
        self.lbl_test.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.lbl_test,1)

        btn_test = QPushButton("CHANGE SIZE")
        btn_test.clicked.connect(self.btn_test)
        main_layout.addWidget(btn_test,1)

        main_layout.addStretch(1)

    def btn_test(self):
        load.open_file(self)
        self.lbl_test.setText(shared.json_file["lbl_test"])