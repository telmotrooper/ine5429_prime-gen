from math import gcd
from sys import exit

# https://en.wikipedia.org/wiki/Blum_Blum_Shub

def blum_blum_shub(p, q, s):
  print(f"p = {p}, q = {q}, s = {s}")
  check_seed(p,q,s)

def check_seed(p, q, s):
  m = p * q
  coprime = gcd(s, m) == 1

  # The seed x0 should be an integer that is co-prime to M
  # (i.e. p and q are not factors of x0) and not 1 or 0. 
  if s == 0 or s == 1:
    print("Error: 0 and 1 are not valid values for the seed.")
    exit(1)
  elif not coprime: 
    print(f"Error: The seed {s} is not a coprime to m.")
    exit(1)
  else:
    print(f"{s} is a valid seed.")
