"""Application Entry Point"""

import core, sys

def main():
  if len(sys.argv) > 1:
    core.alphabetize(sys.argv[1])
  else: core.alphabetize()

if __name__ == '__main__':
  main()
