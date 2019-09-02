#!/usr/bin/env python3

from bbs import BlumBlumShub
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))
  bbs = BlumBlumShub(11, 19, 3)

if __name__ == "__main__":
  main()
