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

    
    def get_line_to(self,target):
 
        m = (target.y-self.y)/(target.x-self.x)
        c = target.y - (m*target.x) 
        return point(m,c)
    

print(point(4,11).get_line_to(point(6,15)))
