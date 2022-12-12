# format -> start1-end1,start2-end2
# split on comma, then split on -
# check overlapping schedules
# if start1 >= start2 and end1 <= end2 - overlapping

def strListToInt(toConvert):
  for i in range(len(toConvert)):
    toConvert[i] = int(toConvert[i])
  return toConvert

def isFullyOverlapping(schedule1, schedule2):
  if schedule1[0] >= schedule2[0] and schedule1[1] <= schedule2[1]:
    return True
  elif schedule2[0] >= schedule1[0] and schedule2[1] <= schedule1[1]:
    return True
  else:
    return False

def isOverlapping(schedule1, schedule2):
  if schedule1[1] < schedule2[0] or schedule2[1] < schedule1[0]:
    return False
  else:
    return True

def formatSchedules(schedules):
  formatted = []
  for schedule in schedules:
    formatted.append(strListToInt(schedule.split('-')))
  return formatted

def totalFullyOverlapping():
  fileReader = open("day_4/day_4.txt", "r")
  total = 0
  for pairs in fileReader:
    schedules = pairs.strip('\n').split(',')
    formatted = formatSchedules(schedules)
    if isFullyOverlapping(formatted[0], formatted[1]):
      total += 1
  return total

def totalOverlapping():
  fileReader = open("day_4/day_4.txt", "r")
  total = 0
  for pairs in fileReader:
    schedules = pairs.strip('\n').split(',')
    formatted = formatSchedules(schedules)
    if isOverlapping(formatted[0], formatted[1]):
      total += 1
  return total

print('-*-  DAY FOUR  -*-')
print('Fully Overlapping Schedules:', totalFullyOverlapping())
print('Partially Overlapping Schedules:', totalOverlapping())
print()