#!/usr/bin/env python3

import sys
from bbs import BlumBlumShub
from lcg import LinearCongruentialGenerator
from prime_checker import miller_rabin
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))

  bbs = BlumBlumShub(
    961748941,
    982451653,
    879190841)

  for i in range(0,5):
    num = bbs.next()
    print(f"{num} ({sys.getsizeof(num)} bytes)")
    print(f"Miller-Rabin: {miller_rabin(num)}")


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

  print(miller_rabin(961748941))

if __name__ == "__main__":
  main()
