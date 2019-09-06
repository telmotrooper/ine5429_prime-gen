from math import gcd
from sys import exit
from colors import red, yellow

# https://en.wikipedia.org/wiki/Blum_Blum_Shub

class BlumBlumShub:
  def __init__(self, p, q, s):
    print(yellow("Blum Blum Shub algorithm"))
    print(f"p = {p}\nq = {q}\ns = {s}\n")

    self.p = p
    self.q = q
    self.s = s
    self.x = s # x[0] = s
    self.m = p * q

    self.check_seed()

  def check_seed(self):
    coprime = gcd(self.s, self.m) == 1

    # The seed x0 should be an integer that is co-prime to M
    # (i.e. p and q are not factors of x0) and not 1 or 0. 
    if self.s == 0 or self.s == 1:
      print(red("Error: 0 and 1 are not valid values for the seed."))
      exit(1)
    elif not coprime: 
      print(red(f"Error: The seed {self.s} is not a coprime to m."))
      exit(1)

  def next(self):
    # x[n+1] = x[n]^2 % m
    self.x = pow(self.x, 2, self.m)
    return(self.x)
