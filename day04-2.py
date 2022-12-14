ans = 0

while True:
  pair = input()
  if pair == 'q':
    break
  arr = []
  cur = ""
  for c in pair:
    if c != ',' and c != '-':
      cur += c
    else:
      arr.append(int(cur))
      cur = ""
  arr.append(int(cur))
  if (arr[0] >= arr[2] and arr[0] <= arr[3]) or (arr[1] >= arr[2] and arr[1] <= arr[3]) or (arr[2] >= arr[0] and arr[2] <= arr[1]) or (arr[3] >= arr[0] and arr[3] <= arr[1]):
    ans += 1

print(ans)

