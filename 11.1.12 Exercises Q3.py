class point:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def reflect_x(self):
        x = self.x
        y = -1* self.y
        return point(x,y)
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def slope_from_origin(self):
        return (self.y/self.x)
    
p1 = point(4,10)
q1 = p1.reflect_x()
q1 = p1.slope_from_origin()
print(q1)    
