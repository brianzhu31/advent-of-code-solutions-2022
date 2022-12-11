visited = set()
visited.add((0, 0))
h = [0, 0]
t = [0, 0]

def isTouching(c1, c2):
  if(c1[0] < c2[0]-1 or c1[0] > c2[0]+1 or c1[1] < c2[1]-1 or c1[1] > c2[1]+1):
    return False
  return True

while True:
  command = input()
  if(command == 'q'):
    break
  moves = int(command[2:])
  hDirection = 1
  vDirection = 1
  if(command[0] == 'L'):
    hDirection = -1
  if(command[0] == 'U'):
    vDirection = -1

  if(command[0] == 'R' or command[0] == 'L'):
    for i in range(0, moves):
      h[1] += hDirection
      if(isTouching(h, t) == False):
        if(t[0] == h[0]):
          t[1] += hDirection
        else:
          if(h[0] > t[0]):
            t[0] += 1
          else:
            t[0] -= 1
          t[1] += hDirection
        visited.add((t[0], t[1]))
  elif(command[0] == 'U' or command[0] == 'D'):
    for i in range(0, moves):
      h[0] += vDirection
      if(isTouching(h, t) == False):
        if(t[1] == h[1]):
          t[0] += vDirection
        else:
          if(h[1] > t[1]):
            t[1] += 1
          else:
            t[1] -= 1
          t[0] += vDirection
      visited.add((t[0], t[1]))

print(len(visited))
