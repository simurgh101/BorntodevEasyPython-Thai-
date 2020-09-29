n=int(input())
m=int(input())
matrix = []
for _ in range (m):
    a=[]
    for _ in range(n):
        x=float(input())
        a.append(x)
    matrix += a
c = list(map(lambda x: round((x - min(matrix)) / (max(matrix) - min(matrix)),4) , matrix))

answer = []
for i in range(0,len(c)-1,n):
    a=[]
    for j in range(n):
        a.append(c[i+j])
    answer.append(a)
        
result = []
for i in range(len(answer)):
    a=[]
    for j in range(n):
        g= "%.4f" % answer[i][j]
        a.append(g)
    result.append(a)

for i in result:
    print(*i)
#for i in range(len(answer)):
    #for j in range(n-1):
        #print()

   