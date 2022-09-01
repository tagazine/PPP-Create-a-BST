class BSTNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

  def __repr__(self):
    return str(self.data)

class BST:
  def __init__(self, root = None):
    self.root = root
    self.contents = []

  def __str__(self):
    if self.root == None:
      return "Empty Tree"
    else:
      self.output = ""
      self.print_tree(node = self.root)
      return self.output
  
  def __repr__(self):
    if self.root == None:
      return "Empty Tree"
    else:
      self.output = ""
      self.print_tree(node = self.root)
      return self.output

  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)

  def add(self, node):
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("We need an integer or BSTNode")
    
    if type(node) == int:
      node = BSTNode(node)

    if node.data in self.contents:
      return

    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return

    self.add_node(self.root, node)

  def add_node(self, cur_node, new_node):
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.contents.append(new_node.data)
        return
      else:
        self.add_node(cur_node.right, new_node)
    else:
      if cur_node.left == None:
        cur_node.left = new_node
        self.contents.append(new_node.data)
        return
      else:
        self.add_node(cur_node.left, new_node)

#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)
print(bst)

