def strListToInt(toConvert):
  for i in range(len(toConvert)):
    toConvert[i] = int(toConvert[i])
  return toConvert

boxes = []

def initBoxes():
  global boxes 
  boxes = [['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
         ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
         ['F', 'B', 'H', 'W', 'P', 'M', 'Q'], ['V', 'S', 'T', 'D', 'F'],
         ['Q', 'L', 'D', 'W', 'V', 'F', 'Z'], ['Z', 'C', 'L', 'S'],
         ['Z', 'B', 'M', 'V', 'D', 'F'], ['T', 'J', 'B'],
         ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H']]

# move N boxes from Stack X to Stack Y
# !! move is one at a time from the top (end) of the stack
# create a function that takes in List of Stacks and a single command line
# operates on the List of Stacks
# command[0] => number of boxes to move
# command[1] => origin stack
# command[2] => destination stack


# move one box from origin stack to destination stack
def moveOneBox(origin, destination):
  boxes[destination].append(boxes[origin].pop())


# move n boxes (and keep order) from origin to destination
def moveNBoxes(n, origin, destination):
  boxesToMove = []
  for i in range(n):
    boxesToMove.append(boxes[origin].pop())
  boxesToMove.reverse()
  boxes[destination].extend(boxesToMove)


def processCommandPartOne(command):
  for i in range(command[0]):
    moveOneBox(command[1] - 1, command[2] - 1)


def processCommandPartTwo(command):
  moveNBoxes(command[0], command[1] - 1, command[2] - 1)


def getMessage():
  message = ''
  for i in range(len(boxes)):
    message += (boxes[i].pop())
  return message


# command ex. "move 1 from 5 to 2" -> "[1, 5, 2]"
def parseCommands():
  fileReader = open('day_5/day_5.txt', 'r')
  commands = []
  for line in fileReader:
    digit_iterator = filter(lambda x: (x.isdigit()), line.split())
    commands.append(strListToInt(list(digit_iterator)))
  return commands


def runPartOne():
  initBoxes()
  commands = parseCommands()
  for command in commands:
    processCommandPartOne(command)
  return getMessage()


def runPartTwo():
  initBoxes()
  commands = parseCommands()
  for command in commands:
    processCommandPartTwo(command)
  return getMessage()


print('-*-  DAY FIVE  -*-')
print('Final Message (Part One):', runPartOne())
print('Final Message (Part Two):', runPartTwo())
print()
