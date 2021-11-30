# dunder methods :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""dunder method allow us to use python specific function, It works like a function
and we can also determine and change what that function does by modifying it's dunder method"""

class Toy:
    def __init__(self, color, age):
        self.toy_color = color
        self.toy_age = age
        self.my_dict = {"name": "Mojo Jojo",
                        "has_pets": True}

    def __str__(self):  # because we modified it,the  __str__ returns 'red' when called.
        return self.toy_color  # hash these two line to see what you get without modification.

    def __len__(self):
        return 100

    def __del__(self):
        return "deleted!"

    def __call__(self):
        return "yes??"

    def __getitem__(self, item):
        return self.my_dict[item]

action_figure = Toy("red", 4)

# __str__
print(action_figure.__str__())  # both do the same thing
print(str(action_figure))  # i.e, change the data type to string but we modified it

# __len__
print(action_figure.__len__())  # both do the same thing
print(len(action_figure))  # i.e, calculate number of characters but we modified it

# __del__
print(action_figure.__del__())  # avoid using delete(both dunder method and function)in real use,it can create some bug
# del action_figure   # for this to work you have to print the result in __del__.

# __call__
print(action_figure.__call__())  # __call__ is actually used(under the hood) to call different function in python
print(action_figure())  # hence we can use this syntax for call{() <-- we use this to call something in python}.

# __getitem__
print(action_figure["name"])  # __getitem__ was actually used to make the call for a value of key in a dictionary.
