from recipeClass import Recipe
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit
import sys

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 700, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle('MD Recipe Viewer')
        self.setStyleSheet('''
            QWidget {
                font-size: 17px;
                }
        ''')


        self.main_window = QWidget()
        self.layout = QHBoxLayout(self.main_window)
        self.setCentralWidget(self.main_window)

        self.init_ui()

    def init_ui(self):
        self.md_viewer = QTextEdit(readOnly=True)
        
        self.layout.addWidget(self.md_viewer)

    def markdown_update(self, path):
        md_text = 0 # Read path of md file
        self.md_viewer.setMarkdown(md_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = AppWindow()
    myApp.show()

    sys.exit(app.exec())