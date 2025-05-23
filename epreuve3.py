with open('grid25.txt', 'r', encoding="utf-16") as file:
    content = file.readlines()
    liste = []
    for line in content:
      liste.append(line.split())
    print(liste)
