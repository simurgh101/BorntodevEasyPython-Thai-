li = []
for _ in range(8):
      x = input()
      for i in x:
            if i.isalpha():
                  li.append(i)

    
PositiveP = "P"
PositiveN = "N"
PositiveB = "B"
PositiveR = "R"
PositiveQ = "Q"
PositiveK = "K"
Negativep = "p"
Negativen = "n"
Negativeb = "b"
Negativer = "r"
Negativeq = "q"
Negativek = "k"

num = 0 
for j in li:
      if j in PositiveP:   num += 1
      elif j in PositiveN: num += 3
      elif j in PositiveB: num += 3
      elif j in PositiveR: num += 5
      elif j in PositiveQ: num += 9
      elif j in PositiveK: num += 0
      elif j in Negativep: num -= 1
      elif j in Negativen: num -= 3
      elif j in Negativeb: num -= 3
      elif j in Negativer: num -= 5
      elif j in Negativeq: num -= 9
      elif j in Negativek: num -= 0
    
if num == 0:
      print("equal")
else:
      print(num)
