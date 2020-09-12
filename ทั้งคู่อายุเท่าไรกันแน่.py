n, m, y  = input().split()
x = ((int(n)+int(y))*int(m)-int(y))/(int(m)-1)
A = int(x)
B = int(x-int(n))

print(A,B,sep=' ')
# Advanced Math equation