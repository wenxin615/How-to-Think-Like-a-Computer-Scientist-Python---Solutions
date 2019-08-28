
class MyTime:
    
    def __init__ (self,hrs=0,mins=0,secs=0):
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600 # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        print("{0}:{1}:{2}".format(self.hours,self.minutes,self.seconds))
         
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
        
    def add_time(t1,t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime (0,0,secs)
    
    def compare(self,others1,others2):
        t3 = self.to_seconds()
        t1 = others1.to_seconds()
        t2 = others2.to_seconds()
        if t3 >= t1 & t3 < t2:
            return True
        else:
            return False
    
    def __gt__ (self,others):
        others1 = self.to_seconds()
        others2 = others.to_seconds()
        if others1 > others2:
            return True
        else:
            return False
            
    def increment(self,second):
        totalsecs = self.to_seconds()+second
        self.hours = totalsecs // 3600 # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60     
        print("{0}:{1}:{2}".format(self.hours,self.minutes,self.seconds))
    
    
t1 = MyTime(3,3,60)
print(t1.increment(-60))
