class Recipe:
    
    def __init__(self, title):
        self.title = title
        self.ingredient_quantities = []
        self.ingredient_units = []
        self.ingredient_names = []
        self.steps = []
        self.tags = []
        self.desciption = None
        self.text = []
    
    # Ingredient Methods
    def add_ingredient(self, quanity, unit, name):
        self.ingredient_quantities.append(quanity)
        self.ingredient_units.append(unit)
        self.ingredient_names.append(name)

    def return_ingredient_list(self):
        ingredient_list = []
        for i in range(0, len(self.ingredient_names)):
            ingredient_list.append(
                [self.ingredient_quantities[i],
                 self.ingredient_units[i],
                 self.ingredient_names[i]
                 ]
            )
        return ingredient_list

    # Instructions Methods
    def add_step(self, step):
        self.steps.append(step)
    
    def return_steps(self):
        return self.steps
    
    # Tags Methods
    def add_tag(self, tag):
        self.tags.append(tag)
    
    def return_tags(self):
        return self.tags

    # Extra Methods
    def add_description(self, description):
        self.desciption = description
    
    def return_description(self):
        return self.description
    
    def add_text(self, text):
        self.text.append(text)

    def return_text(self):
        text = ""
        for i in range(0, len(self.text)):
            text += self.text[i] + "\n"
    
    def return_recipe(self):
        recipe = [
            self.title,
            self.description,
            self.return_ingredient_list(),
            self.steps,
            self.return_text(),
            self.tags
        ]
        return recipe