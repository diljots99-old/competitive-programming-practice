import math
def takeInput():

    try:
        a = int(input())
        b = []
        for _ in range(a):
            b.append(input())

    except:
        pass
    
    return a,b

def encrypt(msg):
    n = len(msg)
    L =  math.ceil(n**0.5)
    res = [['*' for _ in range(L)]for _ in range(L)]
    counter = 0
    for i in range (L):
        for j in range(L):
            if counter < len(msg):
                res[i][j] = msg[counter]
                counter += 1
    newRes = list(zip(*res[::-1]))
    result = ""
    for i in range (L):
        for j in range(L):
            ch = newRes[i][j]
            if ch == '*':
                pass
            else:
                result = result + ch
    
    return result

def solve():
    a,listOfMessages = takeInput()

    for message in listOfMessages:
        encryptedMesseage = encrypt(message)
        print(encryptedMesseage)

solve()