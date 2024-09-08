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

        # File paths
        recipe_folder = '/home/nshaw928/Documents/Obsidian Vault/Recipes'

        self.init_ui()
        self.load_sidebar_items(recipe_folder)
        self.sidebar.itemClicked.connect(lambda item: self.get_current_selection(item, recipe_folder))
        self.markdown_update('/home/nshaw928/Documents/Obsidian Vault/Recipes/German Curry Sauce.md')

    def init_ui(self):
        self.sidebar = QListWidget()
        self.md_viewer = QTextEdit(readOnly=True)
        
        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.md_viewer)

    def load_sidebar_items(self, recipe_folder):
        files = os.listdir(recipe_folder)
        print(files)
        for file_name in files:
            self.sidebar.addItem(file_name)

    def markdown_update(self, path):
        md_text = open(path, 'r').read()
        self.md_viewer.setMarkdown(md_text)

    def get_current_selection(self, item, recipe_folder):
        file_name = item.text()
        self.markdown_update(recipe_folder + '/' + file_name)
        return file_name # Returns md file name, not full path

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = AppWindow()
    myApp.show()

    sys.exit(app.exec())