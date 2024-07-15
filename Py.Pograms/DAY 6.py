class Node:
  def __init__ (self,key):
    self.key=key
    self.left=None
    self.right=None

def height_trees(A):
    if(A==None):
        return 0
    else:
        ldepth = height_trees(A.left)

        rdepth = height_trees(A.right)

        if(ldepth > rdepth):
            return(1+ldepth)
        else:
            return(1+rdepth)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.right = Node(7)

root.right.left = Node(8)
root.left.left.right.right = Node(9)



print(height_trees(root))
