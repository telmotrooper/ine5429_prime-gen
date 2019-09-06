#!/usr/bin/env python3

import sys
from bbs import BlumBlumShub
from lcg import LinearCongruentialGenerator
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))

  bbs = BlumBlumShub(
    3000003453453450009130000034534534500091,
    23432424245353535353452342343242424535353535345234,
    23432424245353535353452341)

  for i in range(0,5):
    num = bbs.next()
    print(f"{num} ({sys.getsizeof(num)} bytes)")

  print()

  lcg = LinearCongruentialGenerator(
    214445054984098409049809823424242434013,
    423423424242342342534801656010161045634,
    6465467547567567777854535156123477546456354,
    pow(2,256)
  )

  for i in range(0,5):
    num = lcg.next()
    print(f"{num} ({sys.getsizeof(num)} bytes)")

if __name__ == "__main__":
  main()
