
class MyTime:
    
    def __init__ (self,hrs=0,mins=0,secs=0):
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600 # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
       
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
        
    def add_time(t1,t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime (0,0,secs)
    
    def compare(self,others1,others2):
        t3 = self.to_seconds()
        print(t3)
        t1 = others1.to_seconds()
        print(t1)
        t2 = others2.to_seconds()
        print(t2)
        if t3 >= t1 & t3 < t2:
            return True
        else:
            return False
            

t3 = MyTime(4,4,60)
t2 = MyTime(2,2,60)
t1 = MyTime(3,3,60)
print(t1.compare(t2,t3))
        
        
    
        
