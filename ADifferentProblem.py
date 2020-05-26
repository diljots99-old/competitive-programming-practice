import itertools  
def takeInput():
    A = []
    B = []
    while True:
        try:
            a ,b = input().split()
            a = int(a)
            b = int(b)
            A.append(a)
            B.append(b)

            
        except:
            break
    return A,B

def solve():
    A,B = takeInput()

    for (a, b) in zip(A,B): 
        result   =None
        if a > b:
            result = a-b
        else:
            result = b-a

        print(result)

solve()