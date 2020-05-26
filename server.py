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
    n = A[0]
    T = A[1]
    remaning = T
    listOfTasks = []
    for task in B:
        if task <= remaning:
            remaning -= task
            listOfTasks.append(task)
        else:
            break

    print(len(listOfTasks))

solve()