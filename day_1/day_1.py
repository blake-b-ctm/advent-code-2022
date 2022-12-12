import numpy as np

calorieCounts = [0]
index = 0

fileReader = open("day_1/day_1.txt", "r")

for calories in fileReader:
  if calories == '\n':
    calorieCounts.append(0)
    index += 1
  else:
    calorieCounts[index] += int(calories)

def return_top_n_values(list, n):
  top_n_total = 0
  for i in range(n):
    max_value = np.max(list)
    top_n_total += max_value
    list.remove(max_value)
  return top_n_total

print('-*-  DAY ONE  -*-')
print('Maximum Calorie Total:', return_top_n_values(calorieCounts, 1))
print('Calorie Total of Top 3:', return_top_n_values(calorieCounts, 3))