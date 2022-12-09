ans = ""

s = [
  ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
  ['Q', 'R', 'B'],
  ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
  ['D', 'V', 'F', 'R', 'Q', 'H'],
  ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
  ['W', 'R', 'T', 'Z'],
  ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
  ['R', 'N', 'F', 'H', 'W'],
  ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']
]


while True:
  instruct = input()
  if instruct == 'q':
    break
  num = 0
  fr = 0
  to = 0
  if instruct[6] == ' ':
    num = int(instruct[5])
    fr = int(instruct[12])
    to = int(instruct[17])
  else:
    num = int(instruct[5] + instruct[6])
    fr = int(instruct[13])
    to = int(instruct[18])

  for i in range(num):
    s[to-1].append(s[fr-1][-1])
    s[fr-1].pop()
  
for i in range(9):
  print(s[i][-1], end='')


