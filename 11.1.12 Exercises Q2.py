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

p1 = point(3,4)
q1 = p1.reflect_x()
print(q1)    
