n = int(input())
li = []
for i in range (n):
  x = int(input())
  li.append(x)
    
new = li[::-1]
for j in new:
  print(j)