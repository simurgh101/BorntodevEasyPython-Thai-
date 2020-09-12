n =int(input())
li = []
for i in range (n):
  x = int(input())
  li.append(x)
  
mi = sorted(li)
ma = mi[::-1]
for j in ma:
  print(j)