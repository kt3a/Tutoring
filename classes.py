###This is the Example code for a grocery website class


class food:

    def __init__(self, price):
        self.price = price

 
    def get_price(self):
        return self.price
    
    def discount(self):
        return self.price - (self.price*(.95))

    def __str__(self):                  ##will return a string representation of an object 
        return "a food item of price {:.2f}".format(self.price)



class tomato(food):
    ##having a parameter in the class definition means that the tomato class is a
    ##sub-class or inherrited class of the food class
    ##tomato class can use any of the methods(functions) created in the food class

    
    def discount(self):
        return food.get_price(self) - food.get_price(self)*(.20)



class cherry_tomato(tomato):

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def discount(self):
        print("Sorry, out of stock")

    def __str__(self):
        return 'The cherry tomato is size {} and color {}'.format(self.size,self.color)
    


class chocolate_cake(food):

    print()



def main():
    ##main method is used as a means to run your program, this method is where you
    ##write the code to begin your program
    ##here you also want to create your objecs -- instances of a class

    jelly = food(5.00) ##this declares a food object called "Jelly" and jelly is $5

    print("Jelly is ", jelly.price ," dollars.\nJelly with the grocery store discount is: ", jelly.discount().__str__())

    
    
    ##this will call the __str__ method automatically
    print("jelly is", jelly)

    tomato1 = tomato(2.50)
    print("Tomato is", tomato1)

    print("The tomato grocery store discount price is", tomato1.discount().__str__())

    print()


main()

c_tom = cherry_tomato(11, "yellow")

print(c_tom)
