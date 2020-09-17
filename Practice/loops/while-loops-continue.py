'''
Print numbers 1 to 10, but skip 3
'''

number = 0
while number <= 10:

  if number == 3:
    number += 1
    continue
  
  print(number)
  number += 1