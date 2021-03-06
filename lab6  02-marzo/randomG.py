"""
@Cm
@param seed
@param Maxgenerator  { generator n numbers random}
@return {array with N elements random }
"""
import numpy as np

def Cm(Maxgenerator=1):
    nums= []
    Xn = 7
    a = 7
    c = 1
    m = 16547
    
    
    for iterator in range(Maxgenerator):        
        Xn_1 = (a*Xn + c)% m        
        out = float(Xn_1)/float(m)    
        nums.append(out)
        Xn = Xn_1
    return nums


def GenVAD(N,x,px):
    
    X = []
    u =  Cm(N)    
    Px = np.cumsum(px)    
    

    print "------"
    for index in range(N):
        for i in range (1,len(Px)):
           
            if(u[index]<Px[0] ):
                X.append(x[0])
                break
                
            if(u[index]<Px[i] and u[index]>=Px[i-1]  ):                
                X.append(x[i-1])
                break
            
                
    return X
