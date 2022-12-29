import sys
from typing import List

def main():
  text: list[str] = list(sys.argv[1])
  reversedTextList = list(reversed(text))
  print("".join(reversedTextList))

if __name__ == '__main__':
    main()