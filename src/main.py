from recipeClass import Recipe
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget
import sys
import os

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
        self.load_sidebar_items('/home/nshaw928/Documents/Obsidian Vault/Recipes')
        self.markdown_update('/home/nshaw928/Documents/Obsidian Vault/Recipes/German Curry Sauce.md')

    def init_ui(self):
        self.sidebar = QListWidget()
        self.md_viewer = QTextEdit(readOnly=True)
        
        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.md_viewer)

    def load_sidebar_items(self, recipe_folder_path):
        files = os.listdir(recipe_folder_path)
        print(files)
        for file_name in files:
            self.sidebar.addItem(file_name)

    def markdown_update(self, path):
        md_text = open(path, 'r').read()
        self.md_viewer.setMarkdown(md_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = AppWindow()
    myApp.show()

    sys.exit(app.exec())