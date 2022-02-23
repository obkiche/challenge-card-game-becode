class Symbol:
    icons = ['\u2666', '\u2665', '\u2663', '\u2660']
    colors = ["red", "black"]

    """

    """
    def __init__(self, color , icon ):
        self.color = color
        self.icon = icon

    def __str__(self):

        print (f"Card icon {self.colors[self.color]}")
        return f"{ self.colors[self.color]} {self.icons[self.icon]}"


class Card(Symbol):

     values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
     def __init__(self, color, icon, value):

         super().__init__(color, icon)
         self.symbol =Symbol(color, icon)
         self.value = value

     def __str__(self):
         print ("Your card value is {self.value}".format(self=self))
         print("********")
         return f"{Card.values[self.value]} {self.symbol}"




cr = Card(0, 3, 12)
print(cr)





