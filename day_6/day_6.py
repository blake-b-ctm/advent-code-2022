# read in characters until there are 4 unique characters in a row
# initial idea: create a set out of last 4 characters, if len(set) = 4, then return index

lastN = []


def updateLastN(char, n):
  lastN.append(char)
  if len(lastN) > n:
    lastN.pop(0)


def isUniqueSequence(char, n):
  updateLastN(char, n)
  if len(set(lastN)) == n:
    return True
  else:
    return False


def findUniqueIndex(n):
  with open('day_6/day_6.txt') as fileReader:
    for line in fileReader:
      for index, char in enumerate(line):
        isUnique = isUniqueSequence(char, n)
        if isUnique:
          return index + 1


print('-*-  DAY SIX  -*-')
print('First Unique Sequence of 4 at:', findUniqueIndex(4))
print('First Unique Sequence of 14 at:', findUniqueIndex(14))
print()
