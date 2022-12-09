ans = 0
points = {'A': 1, 'B': 2, 'C': 3}
win = {'A': 'B', 'B': 'C', 'C': 'A'}
lose = {'A': 'C', 'B': 'A', 'C': 'B'}


while True:
  r = input()
  if r == 'q':
    break
  p1 = r[0]
  p2 = r[2]
  
  if p2 == 'X':
    ans += points[lose[p1]]
  elif p2 == 'Y':
    ans += 3 + points[p1]
  elif p2 == 'Z':
    ans += 6 + points[win[p1]]

print(ans)