# There are up to 15 test cases, one per line, up to end of file. 
# Each test case is described by a single line containing three numbers: two real numbers −3≤x,y≤3, and an integer 0≤r≤10000. 
# Each real number has at most 4 digits after the decimal point.
#  The value of c for this case is x+yi, and r is the maximum number of iterations to compute.

import time

def takeInput():
    A = []
    while True:
        try:
            a = input().split()
            a = list(map(float,a))
            if (len(a))<3:
                break
                
            else: 
                A.append([complex(a[0],a[1]),a[2]])
            
        except:
            pass
    return A



def solve(x,r):
    result  = None
    x = complex(A[0],A[1])
    r = A[2]
    z = [complex(0.0,0.0)]
    zMod = [abs(z[-1])]
    for i in range(int(r)):
        # print
        z.append((z[-1]**2)+x)
        if abs(z[-1])<2.0:
            result = 'IN'
            
        else:
            result = 'OUT'
            break
            
    
    return result
    

if __name__ == "__main__":

    start_time = time.time()
    A = takeInput()
    print(A)
    # for i in range(len(A)):
    #     result = solve(A[i])
    #     print('Case '+str(i+1)+': '+result)
   
    end_time = time.time()
    print(end_time-start_time)