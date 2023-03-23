#!/usr/bin/python3
def __init__(self, width=0, height=0):
self.width = width
self.height = height

def width(self):
return self.__width

def width(self, value):
if not insistance(value, int):
raise TypeError("width must be an integer")
elif value < 0:
raise valueError("width must be >= 0")
else:
self.__width = value

def height(self):
return self.__height

def height(self, value):
if not insistance(value, int):
raise TypeError("height must be an integer")
elif value < 0:
raise valueError("height must be >= 0")
else:
self.__height = value


