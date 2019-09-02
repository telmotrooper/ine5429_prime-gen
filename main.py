#!/usr/bin/env python3

from bbs import blum_blum_shub
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))
  blum_blum_shub(11, 19, 3)

if __name__ == "__main__":
  main()
