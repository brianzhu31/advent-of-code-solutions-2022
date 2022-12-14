ans = 0

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
  r = input()
  if r == 'q':
    break
  r1 = r[:int(len(r)/2)]
  r2 = r[int(len(r)/2):]
  s1 = set()
  s2 = set()
  for x in r1:
    s1.add(x)
  for x in r2:
    s2.add(x)

  s3 = s1.intersection(s2)
  
  for x in s3:
    ans += alpha.index(x) + 1

print(ans)

  