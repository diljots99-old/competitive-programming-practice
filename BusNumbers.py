import itertools  
def takeInput():

    try:
        a = input()
        b = input().split()
        a = int(a)
        b = list(map(int,b))
 

        
    except:
        pass
    
    return a,b

def solve():
    A,B = takeInput()
    B.sort()
    result = []
    if A == len(B):
        C = B
        C.append(99999999999999999999999)
        temp = []
        temp.append(C[0])
        for i in range(A):
            
            try:
                x , y = C[i] , C[i+1]
                # print(y-x)
                if (y-x) == 1:
                    temp.append(y)
                else:
                    
                    if len(temp) <= 2:
                        for xx in temp :
                            result.append(str(xx)) 
                    else:
                        result.append(str(temp[0]) + '-' + str(temp[-1]))
                    
                    temp= [y]    
                    
                
            except:
                pass    
            
        for res in result:
            print(res,end =" ")
    

solve()