n = int(input())
#  *
# ***
#  *
# ***
#*****

for i in range(1,n+1):
    for j in range(0,i+1):
        print(' '*(n-j*1) + '*'*(2*j+1))

print(" " * n + "|")
print("=" * n + "V" + "=" * n)