n = int(input())
#   *
#  ***
# *****
#  ***
#   *
l = 1
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
for j in range(n-1):
    print(' '*(j+1) + '*'*((2*(n-1)+1)-2*(j+1)))

#((2*(n-1)+1)-2*(j+1))
