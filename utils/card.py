class Symbol:
    icons = ['\u2666', '\u2665', '\u2663', '\u2660']

    """

    """
    def __init__(self, color = "", icon = 0):
        self.color = color
        self.icon = icon

    def __str__(self):
        return " A card with {self.color} and {self.icon}".format(self=self)


class Card(Symbol):
     values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
     def __init__(self, color, icon, value):

         super().__init__(color, icon)
         self.value = value

     def __str__(self):
          return "Your card value is {self.value}".format(self=self)

card = Card("rouge", '\u2665', '4')






