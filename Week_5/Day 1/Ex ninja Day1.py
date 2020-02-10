class Menu_Manager:
    def __init__(self):
        self.menu = {'pasta': {'name': 'napolitana', 'price': '50', 'spice level': 'Not spicy', 'gluten_index':True},
                     'burger':{'name': 'Yankee', 'price': '70', 'spice level': 'a little spicy', 'gluten_index': False}}

    def add_item(self, name, price, spice, level, gluten_index, type):
            self.menu.update({type : {'name': 'sushi', 'price':'70', 'spice level':'Not spicy','gluten_index':False,}})
            print(self.menu)
#
#     def update_item(self, name, price, spice, gluten):
#         For key , value in menu:
#         print('New menu ready!')


m = Menu_Manager()
m.menu['pasta']['name']
print(m.menu)

