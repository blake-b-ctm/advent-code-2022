fileReader = open("day_3/day_3.txt", "r")

characterPriorities = list(map(chr, range(97, 123)))
characterPriorities.extend(list(map(chr, range(65, 91))))

# split rucksack in half (two compartments)
# find the common item shared by both compartments
# find the priority value of that item + add to total list

#function which split the list into two halves
def splitRucksack(rucksack):
  middle = int(len(rucksack) / 2)
  compartments = [rucksack[i:i+middle] for i in range(0, len(rucksack), middle)]

  return compartments

def findFirstSharedItem(formattedRucksack):
  return set(formattedRucksack[0]).intersection(formattedRucksack[1]).pop()

def calculateSharedItemValue(sharedItem):
  return characterPriorities.index(sharedItem) + 1

def totalValueOfAllRucksacks(reader):
  totalValue = 0
  for rucksack in reader:
    sharedItem = findFirstSharedItem(splitRucksack(rucksack))
    totalValue += calculateSharedItemValue(sharedItem)

  return totalValue

def findSharedItemAcrossThree(rucksacks):
  return set(rucksacks[0]).intersection(rucksacks[1], rucksacks[2]).pop()

def totalForGroupsOfThreeElves():
  fileReader = open("day_3/day_3.txt", "r")
  lines = []
  totalValue = 0
  for line in fileReader:
    lines.append(line.strip('\n'))
    if len(lines) >= 3:
      print('lines', lines)
      totalValue += calculateSharedItemValue(findSharedItemAcrossThree(lines))
      lines = []
  return totalValue

print('-*-  DAY THREE  -*-')
print('Total Value of Shared Items:', totalValueOfAllRucksacks(fileReader))
print('Three Elves shared Values:', totalForGroupsOfThreeElves())