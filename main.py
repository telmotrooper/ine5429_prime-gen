#!/usr/bin/env python3

from bbs import BlumBlumShub
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))
  bbs = BlumBlumShub(11, 19, 3)

  for i in range(0,5):
    print(bbs.next())

if __name__ == "__main__":
  main()
