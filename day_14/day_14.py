#A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

# For first grain of sand, find end space
# For next grain, start at the end space, undo the last action, and re-calculate 
# How many units of sand come to rest before sand starts flowing into the abyss below?

# Sand moves either STRAIGHT DOWN -> LEFT + DOWN -> RIGHT + DOWN -> STOP

numCol = 505
numRow = 11
caveMap = [['.' for x in range(numCol)] for y in range(numRow)]
currentCoordinate = [0, 0]
spawnCoordinate = [0, 500]
bottomFound = False
sandFallen = 0

def strListToInt(toConvert):
  for i in range(len(toConvert)):
    toConvert[i] = int(toConvert[i])
  return toConvert

def handleHorizontal(newCol):
  oldCol = currentCoordinate[1]
  start = min(oldCol, newCol)
  end = max(oldCol, newCol) + 1
  row = currentCoordinate[0]
  for col in range(start, end):
    caveMap[row][col] = '#'

def handleVertical(newRow):
  oldRow = currentCoordinate[0]
  start = min(oldRow, newRow)
  end = max(oldRow, newRow) + 1
  col = currentCoordinate[1]
  for row in range(start, end):
    caveMap[row][col] = '#'

def processMapMove(row, col):
  #print('processMove:', row, col)
  #print('currentCoord:', currentCoordinate)
  if col == currentCoordinate[1]:
    handleVertical(row)
  else:
    handleHorizontal(col)

def printCaveMap():
  for row in range(numRow):
    rowToPrint = ''
    for col in range(493, 506):
      if col < 505:
        rowToPrint += (caveMap[row][col])
      else:
        print(rowToPrint)
  print()

def isSpaceOpen(row, col):
  item = caveMap[row][col]
  return item == '.'

def getRestingCoordinate(row, col):
  if row == 10:
    caveMap[row][col] = 'o'
    printCaveMap()
    global bottomFound
    bottomFound = True
  # Straight Down
  elif isSpaceOpen(row + 1, col):
    getRestingCoordinate(row + 1, col)
  # Left + Down
  elif isSpaceOpen(row + 1, col - 1):
    getRestingCoordinate(row + 1, col - 1)
  # Right + Down
  elif isSpaceOpen(row + 1, col + 1):
    getRestingCoordinate(row + 1, col + 1)
  # Stop Moving
  else:
    caveMap[row][col] = 'o'
    printCaveMap()

fileReader = open('day_14/day_14_test.txt')
for line in fileReader:
  line.strip('\n')
  coordinates = line.split(' -> ')
  for i, coordinate in enumerate(coordinates):
    toProcess = strListToInt(coordinate.split(','))
    if i == 0:
      currentCoordinate = (toProcess[1], toProcess[0])
    else:
      processMapMove(toProcess[1], toProcess[0])
      currentCoordinate = (toProcess[1], toProcess[0])

caveMap[0][500] = '+'
printCaveMap()


while not bottomFound:
  sandFallen += 1
  getRestingCoordinate(0, 500)

print('Bottom Found, sand grains =>', sandFallen - 1)
