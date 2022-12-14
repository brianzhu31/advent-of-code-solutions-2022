visited = set()
visited.add((0, 0))
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
order = []

def isTouching(c1, c2):
  if(c1[0] < c2[0]-1 or c1[0] > c2[0]+1 or c1[1] < c2[1]-1 or c1[1] > c2[1]+1):
    return False
  return True

while True:
  command = input()
  if(command == 'q'):
    break
  moves = int(command[2:])

  for i in range(0, moves):
    if(command[0] == 'R'):
      rope[0][1] += 1
    elif(command[0] == 'L'):
      rope[0][1] -= 1
    elif(command[0] == 'D'):
      rope[0][0] += 1
    else:
      rope[0][0] -= 1

    for j in range(1, len(rope)):
      if(not isTouching(rope[j-1], rope[j])):
        if(rope[j][0] == rope[j-1][0]):
          if(rope[j-1][1] > rope[j][1]):
            rope[j][1] += 1
          else:
            rope[j][1] -= 1
        elif(rope[j][1] == rope[j-1][1]):
          if(rope[j-1][0] > rope[j][0]):
            rope[j][0] += 1
          else:
            rope[j][0] -= 1
        elif(rope[j-1][1] > rope[j][1]):
          rope[j][1] += 1
          if(rope[j-1][0] > rope[j][0]):
            rope[j][0] += 1
          else:
            rope[j][0] -= 1
        elif(rope[j][1] > rope[j-1][1]):
          rope[j][1] -= 1
          if(rope[j-1][0] > rope[j][0]):
            rope[j][0] += 1
          else:
            rope[j][0] -= 1

    visited.add((rope[9][0], rope[9][1]))

print(len(visited))

