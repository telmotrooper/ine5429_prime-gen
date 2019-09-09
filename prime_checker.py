from random import randrange
from colors import red

def miller_rabin(num):
  # return(None)

  s = 0
  d = num-1

  # write "n - 1" as "2^s * d"
  while d % 2 == 0:
    d >>= 1 # shift right 1 bit (divide by 2)
    s += 1
  
  if not (pow(2,s) * d == num-1):
    print(red(f"Error: Couldn't factor {num}."))
    exit(1)

  a = randrange(2, num-2)
  # print(a)