class Rectangle:

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
    if self.height>=50 or self.width>=50:
      return "Too big for picture."
    output=""
    for h in range(self.height):
      output+="*"*self.width+"\n"
    return output


  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    




class Square(Rectangle):
  def __init__(self,side):
    self.height =side
    self.width = side
  
  def set_side(self,side):
    self.height =side
    self.width = side

  def set_width(self,side):
    self.width=side
  
  def set_height(self,side):
    self.height =side
    
  def __str__(self):
    output=f"Square(side={self.width})"
    return output