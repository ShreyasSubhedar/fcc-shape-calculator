class Rectangle:
  height=0
  width=0
  def __init__(self,height,width):
    self.height =height
    self.width = width
  
  def set_width(self,width):
    self.width=width
  
  def set_height(self,height):
    self.height =height
  
  def get_area(self):
    return self.width*self.height
  
  def get_perimeter(self):
    return (2*self.width)+(2*self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  
  def get_picture(self):
    if self.height>=50 or self.weight>=50:
      return False
      output=""
      for h in range(self.height):
        output+="*"*self.width+"\n"
    return output




class Square:
  pass