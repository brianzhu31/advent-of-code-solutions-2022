x = 1
sprite = [0, 1, 2]
image = ""
cycleCount = 1
commands = []

while True:
  command = input()
  if(command == 'q'):
    break
  commands.append(command)

curCommand = commands[0]
commandIndex = 0

for i in range(6):
  for j in range(40):
    if(j in sprite):
      image += '#'
    else:
      image += '.'

    curCommand = commands[commandIndex]
    if(curCommand[:4] == "addx"):
      if(cycleCount == 2):
        x += int(curCommand[5:])
        sprite[1] = x
        sprite[0] = x-1
        sprite[2] = x+1
        commandIndex += 1
        cycleCount = 1
      else:
        cycleCount += 1
    else:
      commandIndex += 1
      cycleCount = 1

  image += "\n"

print(image)