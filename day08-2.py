matrix = []
ans = 0

while True:
  inp = input()
  if(inp == 'q'):
    break
  row = []
  for t in inp:
    row.append(int(t))
  matrix.append(row)

for i in range(1, 98):
  for j in range(1, 98):
    l = 0
    r = 0
    u = 0
    d = 0
    for x in range(j+1, 99):
      r += 1
      if(matrix[i][x] >= matrix[i][j]):
        break
    for x in range(j-1, -1, -1):
      l += 1
      if(matrix[i][x] >= matrix[i][j]):
        break
    for x in range(i+1, 99):
      u += 1
      if(matrix[x][j] >= matrix[i][j]):
        break
    for x in range(i-1, -1, -1):
      d += 1
      if(matrix[x][j] >= matrix[i][j]):
        break
    score = l*r*u*d
    if score > ans:
      ans = score

print(ans)
