import sys
from typing import List

def main():
  text: list[str] = list(sys.argv[1])
  result: list[str] = list()

  for i in range(0, len(text)):
    if (i % 2 == 0):
      result.append(text[i])

  print("".join(result))

if __name__ == '__main__':
    main()