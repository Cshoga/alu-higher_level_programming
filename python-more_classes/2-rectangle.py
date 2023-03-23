#!/usr/bin/python3
def __init__(self, width=0, height=0):
  self.width = width
  self.height = height
  
  def width(self):
    return self.__width
  
  def width(self, value):
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
      elif value < 0:
        raise valueError("width must be >= 0")
        else:
          self.__width = value
          
          def height(self):
    return self.__height
  
  def height(self, value):
    if not isinstance(value, int):
      raise TypeError("height must be an integer")
      elif value < 0:
        raise valueError("height must be >= 0")
        else:
          self.__height = value
          
          def area(self):
    """Return the area of the Rectangle"""
    return self.__width * self.__height

def perimeter(self):
    """Return the perimeter of the Rectangle"""
    if self.__width == 0 or self.__height == 0:
        return 0
    return (self.__width + self.__height) * 2
