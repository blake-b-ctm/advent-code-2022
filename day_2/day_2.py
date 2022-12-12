fileReader = open("day_2/day_2.txt", "r")

def isRock(move):
  return move == 'A' or move == 'X'

def isPaper(move):
  return move == 'B' or move == 'Y'

def isScissors(move):
  return move == 'C' or move == 'Z'

def isAWin(moves):
  if isRock(moves[1]) and isScissors(moves[0]):
    return True
  elif isPaper(moves[1]) and isRock(moves[0]):
    return True
  elif isScissors(moves[1]) and isPaper(moves[0]):
    return True
  else:
    return False

def isADraw(moves):
  if isRock(moves[1]) and isRock(moves[0]):
    return True
  elif isPaper(moves[1]) and isPaper(moves[0]):
    return True
  elif isScissors(moves[1]) and isScissors(moves[0]):
    return True
  else: 
    return False

def moveScore(move):
  if isRock(move):
    return 1
  elif isPaper(move):
    return 2
  elif isScissors(move):
    return 3

def roundScore(moves):
  if isAWin(moves):
    return 6
  elif isADraw(moves):
    return 3
  else:
    return 0

totalScore = 0
for round in fileReader:
  moves = round.split()
  totalScore += moveScore(moves[1])
  totalScore += roundScore(moves)

print('-*-  DAY TWO  -*-')
print('Total Score (part one):', totalScore)