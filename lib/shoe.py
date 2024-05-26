#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand, size):
        self.brand =brand
        self.size =size
        self._condition = None
    def get_shoe_size(self):
        return self._size
    def set_shoe_size (self,size):
        if type(size) is not int:
            print("size must be an integer")
        else:
             self._size = size
    size=property(get_shoe_size,set_shoe_size) 
    def cobble(self):
        print("Your shoe is as good as new!") 
        self.condition=("New")       



shoe=Shoe("Adidas", 9)        
shoe.cobble()
shoe.condition =" New"        