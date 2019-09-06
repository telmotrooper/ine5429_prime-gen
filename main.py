#!/usr/bin/env python3

import sys
from bbs import BlumBlumShub
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))

  bbs = BlumBlumShub(
    3000003453453450009130000034534534500091,
    23432424245353535353452342343242424535353535345234,
    23432424245353535353452341)

  for i in range(0,500):
    num = bbs.next()
    print(f"{num} ({sys.getsizeof(num)} bytes)")

if __name__ == "__main__":
  main()
