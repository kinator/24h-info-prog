SAME_LEVEL = 1
UP_LEVEL = 4
DOWN_LEVEL = 2

class Node:
  def __init__(self, val, x, y):
    self.l = None
    self.r = None
    x = x
    y = y
    self.v = val

class Tree:
  def __init__(self):
    self.root = None

  def get_root(self):
    return self.root

  def add(self, x, y, val):
    if not self.root:
      self.root = Node(val, x, y)
    else:
      if not self.find(val, x, y):
        self._add(val, x, y, self.root)

  def _add(self, val, x, y, node):
    if val < node.v:
      if node.l:
        self._add(val, x, y, node.l)
      else:
        node.l = Node(val, x, y)
    else:
      if node.r:
          self._add(val, y, x, node.r)
      else:
          node.r = Node(val, x, y)

  def find(self, val, x, y):
    if self.root:
      return self._find(val, self.root, x, y)

  def _find(self, val, node, x, y):
    if val == node.v and node.x == x and node.y == y:
      return node
    elif val < node.v and node.l:
      return self._find(val, x, y, node.l)
    elif val > node.v and node.r:
      return self._find(val, x, y, node.r)

  def delete_tree(self):
    # garbage collector will do this for us.
    if self.root:
      self.root = None

  def view_tree(self):
    if self.root:
      self._view_tree(self.root)

  def _view_tree(self, node):
    if node:
      self._view_tree(node.l)
      print(node.v, end = " ")
      self._view_tree(node.r)


with open('course1.txt', 'r', encoding="utf-8") as file:
  length = file.readline()
  content = file.readlines()
  liste = []
  
  
  maximum = 0
  for line in content:
    liste.append(line.split())

def create_tree(liste, x, y):
  tree = Tree(liste[x][y], x, y)
  if x == 3000 and y == 4000:
    return tree
  if x < 3000:
    tree_left = create_tree(liste, x+1, y)
    tree.add(tree_left)
  if y < 4000:
    tree_right = create_tree(liste, x, y+1)
    tree.add(tree_right)
  return tree

tree = create_tree(liste, 0, 0)
print(tree)