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
    result = 0
    if A == len(B):
        for x in B:
            if x < 0:
                result += 1
        print(result)    

if __name__ == "__main__":
    solve()