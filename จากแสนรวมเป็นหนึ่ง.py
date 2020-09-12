def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

num = int(input())
result = add_digits(num)
print(result)

      