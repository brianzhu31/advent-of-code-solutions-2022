elves = []
quit = False

while True:
  if quit:
    break
  calories = 0
  while True:
    meal = input()
    if meal == '':
      elves.append(calories)
      break
    elif meal == 'q':
      quit = True
      break
    else:
      calories += int(meal)

elves = sorted(elves)

size = len(elves)
total = elves[size-1] + elves[size-2] + elves[size-3]
print(total)
  