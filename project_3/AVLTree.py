from bridges.bridges import *
from bridges.avl_tree_element import *
import sys


# Remember to change these params before running the script
YOUR_USER_ID = 'tungtran'
YOUR_API_KEY = '361152011190'


# Python code to insert a node in AVL tree 
  
# Generic tree node class 
class Node(AVLTreeElement): 

    def __init__(self, key, value): 
        super().__init__(key, value)
        self.height = 1
        self.label = str(value)

  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(): 
    def __init__(self, assignment_number=0):
        self.bridges = Bridges(assignment_number, YOUR_USER_ID, YOUR_API_KEY)
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key, value): 
      
        if root == None: 
            return Node(key, value) 
        elif key < root.key: 
            root.left = self.insert(root.left, key, value) 
        elif key > root.key: 
            root.right = self.insert(root.right, key, value)
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.key: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.key: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.key: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.key: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.key), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    def visualize(self, root):
        self.bridges.set_data_structure(root)
        self.bridges.visualize()
      


def main():
  # Driver program to test above function 
  myTree = AVL_Tree() 
  root = None
    
  root = myTree.insert(root, 10) 
  root = myTree.insert(root, 20) 
  root = myTree.insert(root, 30) 
  root = myTree.insert(root, 40) 
  root = myTree.insert(root, 50) 
  root = myTree.insert(root, 25) 
    
  """The constructed AVL Tree would be 
              30 
            /  \ 
          20   40 
          /  \     \ 
        10  25    50"""
    
  # Preorder Traversal 
  print("Preorder traversal of the", 
        "constructed AVL tree is") 
  myTree.preOrder(root) 
  print() 
  myTree.visualize(root)

if __name__ == '__main__':
  main()
