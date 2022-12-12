fileReader = open("day_2/day_2.txt", "r")

def isRock(move):
  return move == 'A'

def isPaper(move):
  return move == 'B'

def isScissors(move):
  return move == 'C'

def isALoss(result):
  return result == 'X'
  
def isADraw(result):
  return result == 'Y'

def isAWin(result):
  return result == 'Z'

def moveScore(moves):
  if isAWin(moves[1]):
    if isRock(moves[0]):
      return 2 #paper beats rock
    elif isPaper(moves[0]):
      return 3 #scissors beats paper
    else:
      return 1 #rock beats scissors
  elif isADraw(moves[1]):
    if isRock(moves[0]):
      return 1 #rock v rock
    elif isPaper(moves[0]):
      return 2 #paper v paper
    else:
      return 3 #scissors v scissors
  else: # is a loss
    if isRock(moves[0]):
      return 3 #rock beats scissors
    elif isPaper(moves[0]):
      return 1 #paper beats rock
    else:
      return 2 #scissors beats paper

def roundScore(result):
  if isAWin(result):
    return 6
  elif isADraw(result):
    return 3
  else:
    return 0

totalScore = 0
for round in fileReader:
  moves = round.split()
  totalScore += moveScore(moves)
  totalScore += roundScore(moves[1])

print('Total Score (part two):', totalScore)
print()