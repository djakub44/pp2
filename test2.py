import math as m

class ve():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def sum(self):
        return self.x + self.y

    def __add__(self,U):
        return ve(self.x+U.x,self.y+U.y)

def SquareVe(v: ve):
    return int(m.sqrt((v.x*v.x)+(v.y*v.y)))


if __name__ == "__main__":
    
    myVect = ve(0,0)
    myVect2 = ve(3,4)

    myVect3 = myVect + myVect2
    print(myVect3.sum())
    
    print(SquareVe(myVect3))
