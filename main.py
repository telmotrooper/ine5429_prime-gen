#!/usr/bin/env python3

from bbs import BlumBlumShub
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))
  # bbs = BlumBlumShub(11, 19, 3)
  # bbs = BlumBlumShub(5651, 5623, 53)
  bbs = BlumBlumShub(30000000091, 40000000003, 7604055830)

  for i in range(0,500):
    print(bbs.next())

if __name__ == "__main__":
  main()
