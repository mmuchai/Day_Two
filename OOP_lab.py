'''A dress is a sub class of the parent class clothing. 
It inherits the attributes defined in the super class.
'''
class Clothing (object):
  def __init__ (self, color, size, make):
    self.color = color
    self.size = size
    self.make = make
class Dress (Clothing):
  def __init__ (self):
    super (Dress, self).__init__()
  def buy_dress(self, make):
    if self.make == 'new':
      return "Price is 1000"
    elif self.make == 'second_hand':
      return "Price is 700"
    else:
      return "We do not have this make"
  def sizes_available(self, size):
    if self.size < 24:
      return "We have your size"
    else:
      return "Size not available"
  def dress_color (self, color):
    colors_available = [red, black, white, blue, beige]
    if self.color not in colors_available:
      return "Invalid color"
    else:
      return "Color is available"

