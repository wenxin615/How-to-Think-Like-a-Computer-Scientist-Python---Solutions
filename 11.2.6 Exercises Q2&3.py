class point:

  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y


class Rectangle:
    
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h
        
    def __str__(self):
        return "({0},{1},{2})".format(self.posn,self.width,self.height)
        
    def grow(self,delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
        
    def move(self,dx,dy):
        self.corner.x += dx
        self.corner.y += dy
        
    def area(self):
        return (self.width*self.height) 

    def perimeter(self):
      return (self.width*2 + self.height*2)  

    def flip(self):
      (self.height,self.width) = (self.width,self.height)

r = Rectangle(point(0, 0), 10, 5)
print(r.perimeter() == 30)

r=Rectangle(point(100,50),10,5)
print(r.width == 10 and r.height == 5)
r.flip()
print(r.width == 5 and r.height == 10)


        
