from math import gcd
from sys import exit
from colors import red, yellow

# https://en.wikipedia.org/wiki/Blum_Blum_Shub

class LinearCongruentialGenerator:
  def __init__(self, a, x0, c, m):
    print(yellow("Linear Congruential Generator algorithm"))
    print(f"a = {a}\nx0 = {x0}\nc = {c}\nm = {m}\n")

    self.a = a
    self.x = x0
    self.c = c
    self.m = m

  def next(self):
    # x[n+1] = ((a*x[n]) + c) % m
    self.x = ((self.a * self.x) + self.a) % self.m
    return(self.x)