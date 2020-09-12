n = int(input())
print("--Customers Information--")
for i in range (n):
  name = input()
  year = 2017 - int(input())
  sex  = input()
  
  print( name + " " + "(age : " + str(year) + ")" )