from recipeClass import Recipe
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QPushButton
import sys
import os

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 900, 700
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
        self.main_layout = QVBoxLayout(self)
        self.top_bar_layout = QHBoxLayout()
        self.split_layout = QHBoxLayout()

        # Top bar content
        self.toggle_var = False
        self.button_toggle = QPushButton('Toggle Mode')
        self.button_toggle.clicked.connect(self.toggle_mode)
        self.top_bar_layout.addWidget(self.button_toggle)

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
        self.split_layout.addWidget(left_widget)
        self.split_layout.addWidget(right_widget)

        # Add sub-layouts to main layout
        self.main_layout.addLayout(self.top_bar_layout)
        self.main_layout.addLayout(self.split_layout)
        self.setLayout(self.main_layout)

    def toggle_mode(self):
        if self.toggle_var == False:
            self.toggle_var = True
            # Add buttons
            self.button_add = QPushButton('Add to shopping list')
            self.button_email = QPushButton('Send shopping list')
            self.button_add.clicked.connect(self.add_to_shopping_list)
            self.button_email.clicked.connect(self.email_shopping_list)
            self.top_bar_layout.addWidget(self.button_add)
            self.top_bar_layout.addWidget(self.button_email)

            self.shopping_list_widget = QListWidget()
            self.split_layout.addWidget(self.shopping_list_widget)
        else:
            self.toggle_var = False
            # Remove added buttons
            self.top_bar_layout.removeWidget(self.button_add)
            self.top_bar_layout.removeWidget(self.button_email)
            self.button_add.deleteLater()
            self.button_email.deleteLater()
            self.button_add = None
            self.button_email = None
            # Remove shopping list panel
            self.split_layout.removeWidget(self.shopping_list_widget)
            self.shopping_list_widget.deleteLater()
            self.shopping_list_widget = None

    def markdown_update(self, path, right_widget):
        md_text = open(path, 'r').read()
        right_widget.setMarkdown(md_text)

    def get_current_selection(self, item, recipe_folder, right_widget):
        file_name = item.text()
        self.markdown_update(recipe_folder + '/' + file_name, right_widget)
        self.last_selected_recipe = file_name
    
    def add_to_shopping_list(self):
        self.shopping_list_widget.addItem(self.last_selected_recipe)

    def email_shopping_list(self):
        print()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = AppWindow()
    myApp.show()

    sys.exit(app.exec())