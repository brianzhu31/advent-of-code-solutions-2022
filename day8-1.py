matrix = []
visible = set()

while True:
  inp = input()
  if(inp == 'q'):
    break
  row = []
  for t in inp:
    row.append(int(t))
  matrix.append(row)

for i in range(99):
  tallest = -1
  for j in range(99):
    if(matrix[i][j] > tallest):
      visible.add((i, j))
      tallest = matrix[i][j]

for i in range(99):
  tallest = -1
  for j in range(98, -1, -1):
    if(matrix[i][j] > tallest):
      visible.add((i, j))
      tallest = matrix[i][j]

for j in range(99):
  tallest = -1
  for i in range(99):
    if(matrix[i][j] > tallest):
      visible.add((i, j))
      tallest = matrix[i][j]

for j in range(99):
  tallest = -1
  for i in range(98, -1, -1):
    if(matrix[i][j] > tallest):
      visible.add((i, j))
      tallest = matrix[i][j]

print(len(visible))