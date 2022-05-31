import os
os.mkdir('src/__imgcache__')
import sys
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    graphs = MainWindow()
    graphs.show()
    sys.exit(app.exec())