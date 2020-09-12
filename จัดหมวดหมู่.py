men = int(input())
n = int(input())
for _ in range(n):
      F, T, name = input().split()
      if men in range (int(F),int(T)+1):
            print(name)
      else:
            pass