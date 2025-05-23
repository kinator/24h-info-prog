with open('grid25.txt', 'r', encoding="utf-16") as file:
    content = file.readlines()
    liste = []
    for line in content:
      liste.append(line.split())
# start position: (238, 174)

check = True
visitees = []
x = 238
y = 174
while check:
  position = (x, y)
  case = liste[position[0]][position[1]]
  if case not in visitees:
    visitees.append(case)
    val = int(case)
    x = val // 400
    y = val - x * 400
  else:
    print(val)
    check = False
    print(position)