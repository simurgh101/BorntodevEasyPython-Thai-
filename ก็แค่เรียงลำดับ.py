li = []
for i in range(5):
  x=int(input())
  li.append(x)

mi = sorted(li)
ma = mi[::-1]
for j in ma:
  print(j)
