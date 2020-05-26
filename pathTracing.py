


A = []

while True:
    try:
        a = input()
        if a =="":
            break
        else:
            for x in a.split(" "):
             A.append(x)
        

        
    except:
        break
    


a = A



ver = 0
hor = 0
xlocation = [0]
ylocation = [0]
for mv in a:
    if mv.lower() == 'down':
        ver += 1
    elif mv.lower() == 'up':
        ver -= 1
    elif mv.lower() == 'right':
        hor  += 1
    elif mv.lower() == 'left':
        hor -=  1

    xlocation.append(hor)
    ylocation.append(ver)



xSet =  list(sorted(set(xlocation)))
ySet = list(sorted(set(ylocation)))
res = x = [[" " for _ in range(len(xSet))] for _ in range(len(ySet))]
xDic = {}
yDic = {}

for i in range(len(xSet)):
    xDic[xSet[i]] = i
for i in range(len(ySet)):
    yDic[ySet[i]] = i


newlocation = []

for i in range(len(xlocation)):
    newlocation.append([ yDic[ylocation[i]],xDic[xlocation[i]] ])

counter = 0
for r in newlocation:
    i = r[0]
    j = r[1]
   
    res[i][j] = '*'
    
i,j = newlocation[0][0],newlocation[0][1]
res[i][j] = 'S'
i,j = newlocation[-1][0],newlocation[-1][1]
res[i][j] = 'E'

header = "#" *(len(xSet)+2)
print(header)
for row in res:
    print("#"+ "".join(row) + "#")
    # print(*row,sep="")
print(header)
