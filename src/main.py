from recipeClass import Recipe
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QPushButton
import sys
import os

# TODO integrate the recipe class for all recipes to be saved in the format, write function

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
        self.recipe_folder = '/home/nshaw928/Documents/Obsidian Vault/Recipes'

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
        files = os.listdir(self.recipe_folder)
        for file_name in files:
            left_widget.addItem(file_name)

        left_widget.itemClicked.connect(lambda item: self.get_current_selection(item, self.recipe_folder, right_widget))
        
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
            self.button_email.clicked.connect(self.return_shopping_list) # Change to email once function complete
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
        # TODO Convert list from return_shopping_list() to email
        print()

    def return_shopping_list(self):
        recipes = [self.shopping_list_widget.item(i).text() for i in range(self.shopping_list_widget.count())]
        ingredient_list = []

        for recipe in recipes:
            # Open .md file and pull ingredients
            path = self.recipe_folder + '/' + recipe
            recipe_text = open(path, 'r').read()
            ingredients = recipe_text.split('### Ingredients\n')[1].split('\n### Instructions')[0].split('\n')

            # Save all ingredients in a list of tuples
            # TODO add list of units to allow for the absense of units in the case of fruit/veg. example: '1 apple'
            for ingredient in ingredients:
                quantity = ingredient.split(' ')[1]
                unit = ingredient.split(' ')[2]
                item = ' '.join(ingredient.split(' ')[3:])
                
                ingredient_list.append((quantity, unit, item))

            print(ingredient_list)
            
        # TODO combine like ingredients
        # TODO allow for storage of pantry ingredients to not be returned

        return ingredient_list
            

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = AppWindow()
    myApp.show()

    sys.exit(app.exec())