
class point:
    
    def __init__ (self,x=0,y=0,):
        self.x = x
        self.y = y
        
        
        
def distance(p1,p2):
    dx = p2.x-p1.x
    dy = p2.y-p2.y
    return dx*2 + dy*2
    

p1 = point(1,2)
p2 = point(3,4)
print(distance(p1,p2))
