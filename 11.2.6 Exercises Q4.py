  
class point:
  def __init__(self,x=0,y=0):
     self.x = x 
     self.y = y




class Rectangle:

  def __init__ (self,pt,w,h):
    self.point = pt
    self.width = w
    self.height = h

  def contains(self,x=0,y=0):
    if self.point.x >= 0 & self.point.x <10:
      if self.point.y >=0 & self.point.y<5:
        flag = 1
    else:
      flag = 0
    return (flag == 1)

r = Rectangle(point(0,0),10,5)
print(r.contains(point(0, 0)))
print(r.contains(point(3, 3)))
print(not r.contains(point(3, 7)))
print(not r.contains(point(3, 5)))
print(r.contains(point(3, 4.99999)))
print(not r.contains(point(-3, -3)))
