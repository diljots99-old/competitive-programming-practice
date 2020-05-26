def takeInput():

    try:
        a = input().split()
        b = input().split()
        a = list(map(int,a))
        b = list(map(int,b))
 

        
    except:
        pass
    
    return a,b

    
def solve():
    A , B = takeInput()
    W = A[0]
    P = A[1]
    partitions = B
    partitions.insert(0,0)
    partitions.append(W)

    listOfPossibleConfigration = []
    listOfLengthOfConfigration = []

    for i in range(len(partitions)):
        for j in range(i+1,len(partitions)):
            
            a = partitions[i]
            b = partitions[j]
            listOfPossibleConfigration.append([a,b])
            listOfLengthOfConfigration.append(b-a)

    result = list(sorted(set(listOfLengthOfConfigration)))

    print(*result , sep=" ")
solve()
