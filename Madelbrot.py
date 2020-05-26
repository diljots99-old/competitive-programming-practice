# There are up to 15 test cases, one per line, up to end of file. 
# Each test case is described by a single line containing three numbers: two real numbers −3≤x,y≤3, and an integer 0≤r≤10000. 
# Each real number has at most 4 digits after the decimal point.
#  The value of c for this case is x+yi, and r is the maximum number of iterations to compute.

import time

def takeInput():
    res= []
    i = 0
    while True:
        try:
            a = input().split()
            a = list(map(float,a))
            
                
               
            res.append('Case '+str(i+1)+': '+solve(complex(a[0],a[1]),a[2]))
        
        
            i += 1

                
        except:
            break
    print(*res, sep = "\n") 
            
            



def solve(x,r):
    result  = 'IN'
    z = [complex(0.0,0.0)]
    for i in range(int(r)):
        # print
        z.append((z[-1]**2)+x)
        if abs(z[-1])>2.0:
            result = 'OUT'
            break
            
        
            
    
    return result
    




takeInput()


    

