# How many trees are visible from outside the grid?
# Visible if there is another tree in either direction that has a lower height
# Try to minimize storage needs

# 30373
# 25512
# 65332
# 33549
# 35390

# Search outwards to find if your height matches or is higher than yours
# If so, your tree is not visible from that direction

colLowHeights = []
rowLowHeights = []

def storeMinimumHeight(height, col, row):
  if col >= len(colLowHeights):
    colLowHeights.append(height)
  elif colLowHeights[col] > height:
    colLowHeights[col] = height
  if row >= len(rowLowHeights):
    rowLowHeights.append(height)
  elif rowLowHeights[row] > height:
    rowLowHeights[row] = height

def isOnAnEdge(col, row):
  return (col == 0 or row == 0 or col == len(colLowHeights) - 1 or row == len(rowLowHeights) - 1)

def isVisible(height, col, row):
  return isOnAnEdge(col, row) or height > colLowHeights[col] or height > rowLowHeights[row]

#fileReader = open('day_8/day_8.txt', 'r')
fileReader = open('day_8/day_8_test.txt', 'r')
for row, line in enumerate(fileReader):
  line = line.strip('\n')
  for col, char in enumerate(line):
    storeMinimumHeight(int(char), col, row)

fileReader = open('day_8/day_8_test.txt', 'r')
numberVisible = 0
for row, line in enumerate(fileReader):
  line = line.strip('\n')
  for col, char in enumerate(line):
    if isVisible(int(char), col, row):
      numberVisible += 1
print('-*-  DAY EIGHT  -*-')
print('Number of Trees Visible', numberVisible)