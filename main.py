#!/usr/bin/env python3

import sys
from bbs import BlumBlumShub
from lcg import LinearCongruentialGenerator
from prime_checker import miller_rabin
from colors import cyan

def main():
  print(cyan("Prime Number Generator"))
  print("Using keys of 1120 bits outputs numbers of 2048 bits")

  bbs = BlumBlumShub(
    1713354062718701689665040717406759049404216013526475280326864517966535932313224170152857602770029063181359807117405531485215291768478887666006486094187000158642266479268002967872677135698486141514581496932560572461741901040779994401017170012542713739602068588583,
    106661847744886185415813456321441520865870289655228339501951934756891589823901485986462490011500449771252907729112691791451031707300817800121404212543336752298946146797731935417567158706398326505669150118422688705393965079167850742801683997272598385310837664311,
    505681814266168811)

  print("RUNNING")

  for i in range(0,9999):
    # print(i, end='\r')
    # print("\nhey")
    num = bbs.next()
    # print(f"{num} ({sys.getsizeof(num)*8} bits)")
    if miller_rabin(num):
      print(f"\nPRIME: {num} ({sys.getsizeof(num)*8} bits) (iteration {i+1})")

  print("FINISHED")
  # print()

  # lcg = LinearCongruentialGenerator(
  #   214445054984098409049809823424242434013,
  #   423423424242342342534801656010161045634,
  #   6465467547567567777854535156123477546456354,
  #   pow(2,256)
  # )

  # for i in range(0,5):
  #   num = lcg.next()
  #   print(f"{num} ({sys.getsizeof(num)*8} bits)")

  # print(miller_rabin(961748941))

if __name__ == "__main__":
  main()
