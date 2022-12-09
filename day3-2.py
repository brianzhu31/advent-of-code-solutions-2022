ans = 0
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:

  r1 = input()
  if r1 == 'q':
    break
  r2 = input()
  r3 = input()

  s1 = set()
  s2 = set()
  s3 = set()
  for x in r1:
    s1.add(x)
  for x in r2:
    s2.add(x)
  for x in r3:
    s3.add(x)

  s1i_s2 = s1.intersection(s2)
  s3i_s1i2 = s3.intersection(s1i_s2)
  
  for x in s3i_s1i2:
    ans += alpha.index(x) + 1

print(ans)

  