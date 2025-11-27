import sys
from PyQt6.QtWidgets import QApplication

import util

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = util.MainWindow()
    main_window.showMaximized()

    sys.exit(app.exec())