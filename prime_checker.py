from random import randrange
from colors import red

num_rounds = 40

def miller_rabin(num):
  continue_outer_loop = False

  s = 0
  d = num-1

  # write "n - 1" as "2^s * d"
  while d % 2 == 0:
    d >>= 1 # shift right 1 bit (divide by 2)
    s += 1
  
  if not (pow(2,s) * d == num-1):
    print(red(f"Error: Couldn't factor {num}."))
    exit(1)

  for i in range(0, num_rounds):
    a = randrange(2, num-2 + 1) # [2,num-2]
    x = pow(a,d, num)

    if x == 1 or x == num - 1:
      continue

    for j in range(0, s-1):
      x = pow(x,2,num)

      if x == num-1:
        continue_outer_loop = True
        break
    
    if continue_outer_loop:
      continue
    
    return False
  
  return True

def fermat(num):
  for i in range(0, num_rounds):
    a = randrange(2, num-2 + 1) # [2,num-2]
    x = pow(a,num-1, num)

    if x != 1:
      return False
  
  return True
