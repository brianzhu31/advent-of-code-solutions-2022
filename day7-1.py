class Folder:

   def __init__(self, name="", id=0, parent=None, children=[], size=0):
    self.name = name
    self.id = id
    self.parent = parent
    self.children = children
    self.size = size

class File:

  def __init__(self, name="", id=0, parent=None, size=0):
    self.name = name
    self.id = id
    self.parent = parent
    self.size = size

main = Folder("main", 0)
nextID = 1
arr = [main]
curParentID = 0
curCommand = ""

while True:
  if(curCommand == ''):
    curCommand = input()
  if curCommand == 'q':
    break

  elif(curCommand == "$ ls"):
    while True:
      new = input()
      if(new == 'q'):
        curCommand = 'q'
        break
      elif(new[0] == '$'):
        curCommand = new
        break
      elif(new[:3] == "dir"):
        newFolder = Folder(new[4:], nextID, arr[curParentID], [], 0)
        arr.append(newFolder)
        arr[curParentID].children.append(newFolder)
        nextID += 1
        curCommand = ''
      else:
        fileName = ''.join([i for i in new if not i.isdigit() and i != ' '])
        newFile = File(fileName, nextID, arr[curParentID], int(new[:new.index(' ')]))
        arr.append(newFile)
        arr[curParentID].children.append(newFile)
        nextID += 1
        curCommand = ''

  elif(curCommand[:4] == "$ cd"):
    if(curCommand == "$ cd .."):
      curParentID = arr[curParentID].parent.id
    elif(curCommand == "$ cd /"):
      curParentID = 0
    else:
      for child in arr[curParentID].children:
        if child.name == curCommand[5:]:
          curParentID = child.id
          break
    curCommand = ''

for c in main.children[0].children[0].children:
  print(c.name)

sizes = [-1]*len(arr)  

def calcSize(f):
  if(type(f) is File):
    return f.size
  if(sizes[f.id] != -1):
    return sizes[f.id]
  size = 0
  for c in f.children:
    size += calcSize(c)
  sizes[f.id] = size
  return size

x = calcSize(main)

ans = 0
for x in sizes:
  if(x != -1 and x < 100000):
    ans += x

print(ans)