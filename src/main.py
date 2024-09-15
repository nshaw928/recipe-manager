from recipeClass import Recipe
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QPushButton
import sys
import os

class AppWindow(QWidget):
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

        # File paths
        recipe_folder = '/home/nshaw928/Documents/Obsidian Vault/Recipes'

        # Define structure of boxes
        main_layout = QVBoxLayout(self)
        top_bar_layout = QHBoxLayout()
        split_layout = QHBoxLayout()

        # Top bar content
        button_toggle = QPushButton('Button 1')
        button_toggle.clicked.connect(self.toggle_mode)
        top_bar_layout.addWidget(button_toggle)

        # Left Widget
        left_widget = QListWidget()

        # Left widget content
        files = os.listdir(recipe_folder)
        for file_name in files:
            left_widget.addItem(file_name)

        left_widget.itemClicked.connect(lambda item: self.get_current_selection(item, recipe_folder, right_widget))
        
        # Right Widget
        right_widget = QTextEdit(readOnly=True)

        # Add left and right widgets to split layout
        split_layout.addWidget(left_widget)
        split_layout.addWidget(right_widget)

        # Add sub-layouts to main layout
        main_layout.addLayout(top_bar_layout)
        main_layout.addLayout(split_layout)
        self.setLayout(main_layout)

    def toggle_mode(self):
        button_add = QPushButton('Add to shopping list')
        button_email = QPushButton('Send shopping list')
        self.top_bar_layout.addWidget(button_add)
        self.top_bar_layout.addWidget(button_email)

    def markdown_update(self, path, right_widget):
        md_text = open(path, 'r').read()
        right_widget.setMarkdown(md_text)

    def get_current_selection(self, item, recipe_folder, right_widget):
        file_name = item.text()
        self.markdown_update(recipe_folder + '/' + file_name, right_widget)
        return file_name # Returns md file name as str, not full path

    def start_shopping_list(self):
        shopping_list_widget = QListWidget()
        split_layout.addWidget(shopping_list_widget)

    
    def add_to_shopping_list(self):
        print()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = AppWindow()
    myApp.show()

    sys.exit(app.exec())