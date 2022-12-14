x = 1
cycle = 0
ans = 0

def incrementCycle():
  global cycle
  global ans
  global arr
  global x
  cycle += 1
  if(cycle in [20, 60, 100, 140, 180, 220]):
    ans += x*cycle

while True:
  command = input()
  if(command == 'q'):
    break
  incrementCycle()
  if(command.startswith("addx")):
    incrementCycle()
    x += int(command[5:])

print(ans)