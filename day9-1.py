visited = set()
h = [0, 0]
t = [0, 0]

def isTouching(c1, c2):
  if(c1[0] < c2[1]-1 or c1[0] > c2[0]+1 or c1[1] < c2[1]-1 or c2[1] > c2[1]+1):
    return False
  return True

while True:
  command = input()
  if(command == 'q'):
    break
  moves = int(command[2:])
  direction = 1
  if(command[0] == 'L'):
    direction = -1
    moves *= -1

  if(command[0] == 'R' or command[0] == 'L'):
    for i in range(h[0], h[0]+moves, direction):
      h[1] += direction
      if(not isTouching(h, t)):
        if(t[0] == h[0]):
          t[1] += direction
          visited.add((t[0], t[1]))
          


