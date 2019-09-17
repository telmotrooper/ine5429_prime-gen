from math import gcd
from colors import red, yellow
import time

# https://en.wikipedia.org/wiki/Linear_congruential_generator

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
    # start_time = time.time()
    self.x = ((self.a * self.x) + self.c) % self.m
    # print((time.time() - start_time)*1000000)
    return(self.x)
