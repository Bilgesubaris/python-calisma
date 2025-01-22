class GeometricObject:
  def__int__(self._colour=="green",filed=True):
    self.__colour=colour
    self.__filed=filed

  def getColour(self):
    return self.__colour
  def setColour(self,colour):
     self.__colour=colour
  def isFiled(self):
    return self.__filed
  def setFiled(self,filed):
    self.__filed=filed


class Circle(GeometricObject):
  def__init__(self,radius):
    super().__init__()
    self.__radius=radius
  def getRadius(self):
    return self.__radius
  def setRadius(self,radius):
    self.__radius=radius
  def getArea(self):
    return self.__radius
  def getPerimeter(self):
    return self.__radius
  def getDiameter(self):
    return self.__radius


class Rectangle(GeometricObject):
  def__init__(self,widht=1,height=1):
    super().__init__()
    self.__widht=widht
    self.__height=height
  def detWidht(self):
    return self.__widht
  def setWidth(self,widht):
    self.__widht=widht
  def getHeight(self):
    return self.__height()
  def setHeight(self,height):
    self.__height=height




