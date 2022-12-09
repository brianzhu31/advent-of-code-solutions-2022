ans = 0

with open('day6-input.txt') as f:
  packet = f.readlines()

cur = packet[0][:4]

for i in range(4, len(packet[0])):
  cur = cur[1:]
  cur += packet[0][i]
  s = set()
  for c in cur:
    s.add(c)
  if(len(s) == 4):
    ans = i+1
    break

print(ans)

  