from bridges.bridges import *
from bridges.avl_tree_element import *
import sys


# Remember to change these params before running the script
YOUR_USER_ID = 'tungtran'
YOUR_API_KEY = '361152011190'


class Node(AVLTreeElement):
    ''' 
    Inherits from class AVLTreeElement
    
    Create another attribute "num"
    :param num: number of nodes with the same key
    '''
    
    def __init__(self, key, data):
    
        super().__init__(key, data)
        self.data = data
        self.num = 1
        self.height = 1
        self.label = 'Priority: ' + str(data) + '\n' + 'Key: ' + str(key)
        
    def append(self, data):
        self.num += 1


class AVL_Tree:
    ''' AVL Tree (Self-balancing Tree) '''

    def __init__(self, treetype, 
                 assignment_number=0, 
                 title='AVLTree', 
                 descr='Self-balancing Tree'):
                          
        # Create bridges instance
        self.bridges = Bridges(assignment_number, YOUR_USER_ID, 
                               YOUR_API_KEY)
        self.bridges.set_title(title)
        self.bridges.set_description(descr)

        if treetype == "loc":
            self.minmax = [1,1197,1206,1674,1711,5245]
        elif treetype == "crime":
            self.minmax = [0,12,13,20,21,30]
        
        self.root = None
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, root, key):
        if root is None:
            return None
            
        if root.key == key:
            return self.root.data

        elif root.key > key:
            return self._search(root.left, key)
        
        elif root.key < key:
            return self._search(root.right, key)
            
        print(key)
    
    def insert(self, key, data):
        ''' Insert a node into Tree 
        
        :param key: We use key to determine where to insert node at
        :param value: Any value to associate with the key
        '''
        
        # If self.root does not hold anything yet then set self.root
        if self.root == None:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)          
            
    def _insert(self, parent, key, data, grandparent=None): 
        ''' Recursively insert & balance the tree 
        
        :param parent: The parent node we start from
        :param key: We use key to determine where to insert node at
        :param value: Any value to associate with the key
        
        :return: None
        '''
        # Insert
        if parent == None:
            parent.num += 1
            return
            
        if key == parent.key:
            parent
            
        elif key < parent.key:
            if parent.left == None:
                parent.left = Node(key, data)
                parent.height = 1
            else:
                self._insert(parent.left, key, data, grandparent=parent)
                    
        else:
            if parent.right == None:
                parent.right = Node(key, data)
                parent.height = 1
            else:
                self._insert(parent.right, key, data, grandparent=parent)
        
        # Set parent's height
        parent.height = 1 + max( self.get_height(parent.left), self.get_height(parent.right) )
                    
        # Rotate if the difference between two children is 2 or more
        
        # Find balance factor
        parent.balance_factor = self.get_height(parent.right) - self.get_height(parent.left) 
        
        if parent.balance_factor < -1 and parent.left.balance_factor < 0:
            # Case 1
            parent = self.rotate_right(grandparent, parent)
            if grandparent == None:
                self.root = parent
        elif parent.balance_factor < -1 and parent.left.balance_factor > 0:
            # Case 2
            parent.left = self.rotate_left(parent, parent.left)
            parent = self.rotate_right(grandparent, parent)
            
            if grandparent == None:
                self.root = parent
        elif parent.balance_factor > 1 and parent.right.balance_factor > 0:
            # Case 3
            parent = self.rotate_left(grandparent, parent)
            if grandparent == None:
                self.root = parent
        elif parent.balance_factor > 1 and parent.right.balance_factor < 0:
            # Case 4
            parent.right = self.rotate_right(parent, parent.right)
            parent = self.rotate_left(grandparent, parent)
            
            if grandparent == None:
                self.root = parent 
            
    def rotate_right(self, grandparent, parent):
        original_parent = parent
        parent = parent.left
        temp = parent.right
        parent.right = original_parent
        original_parent.left = temp
        
        self.set_height(original_parent, 1 + max(self.get_height(original_parent.left),
                                            self.get_height(original_parent.right)))
        self.set_height(parent, 1 + max(self.get_height(parent.left),
                                   self.get_height(parent.right)))
        
        if grandparent != None:
            if grandparent.left == original_parent: grandparent.left = parent
            else: grandparent.right = parent      
        return parent
            
    def rotate_left(self, grandparent, parent):
        original_parent = parent
        parent = parent.right
        temp = parent.left
        parent.left = original_parent
        original_parent.right = temp
        
        self.set_height(original_parent, 1 + max(self.get_height(original_parent.left),
                                            self.get_height(original_parent.right)))
        self.set_height(parent, 1 + max(self.get_height(parent.left),
                                   self.get_height(parent.right)))
        
        if grandparent != None:
            if grandparent.left == original_parent: grandparent.left = parent
            else: grandparent.right = parent
        return parent
        
    def get_height(self, node):
        if node == None:
            return 0
        else:
            return node.height
            
    def get_balance_factor(self, node):
        if node == None:
            return -1
        else:
            return node.balance_factor
            
    def set_height(self, node, height):
        if node == None:    
            return
        else:
            node.height = height
        
    def level_order(self):
        ''' level order traversal 
        
        Used to print the tree out, level by level 
        '''
        return self._level_order([self.root])
        
    def _level_order(self, current_level_nodes, more=None, result=''):
        if current_level_nodes == []:
            return result

        next_level_nodes = []
        #result += '||'
        for node in current_level_nodes:
            #result += '{} ,'.format(node.key)
            if node.data >= self.minmax[0] and node.data <= self.minmax[1]:
                node.visualizer.color = "green"
            elif node.data >= self.minmax[2] and node.data <= self.minmax[3]:
                node.visualizer.color = "yellow"
            else:
                node.visualizer.color = "red"
            if node.left != None:
                next_level_nodes.append(node.left)
            if node.right != None:
                next_level_nodes.append(node.right)
                
        return self._level_order(next_level_nodes, result=result)
        
    def visualize(self):
        ''' Upload the graph onto Bridges '''
        self.level_order()
        self.bridges.set_data_structure(self.root)
        self.bridges.visualize()
        
        
# If run this file (e.g. python3 AVLTree.py)
# this part of code will run 
# 
# Used to test our AVLTree       
if __name__ == '__main__':
    # Case 1
    tree1 = AVL_Tree()
    tree1.insert(10, 'some')
    tree1.insert(5, 'thing')
    tree1.insert(3, 'cool')
    print(tree1.search(5))

    #print( tree1.level_order() ) # Should be ||5, ||3, 10

    # Case 2
    tree2 = AVL_Tree()
    tree2.insert(10, 'some')
    tree2.insert(5, 'thing')
    tree2.insert(8, 'cool')
    print( tree2.level_order() ) # Should be ||8, ||10, 5
    
    # Case 3
    tree3 = AVL_Tree()
    tree3.insert(10, 'some')
    tree3.insert(20, 'thing')
    tree3.insert(30, 'cool')
    print( tree3.level_order() ) # Should be ||20, ||10, 30
    
    # Case 4
    tree4 = AVL_Tree()
    tree4.insert(10, 'some')
    tree4.insert(20, 'thing')
    tree4.insert(15, 'cool')
    print( tree4.level_order() ) # Should be ||15, ||10, 20
    
    # General Case
    tree = AVL_Tree()
    tree.insert(10, 'say')
    tree.insert(5, 'some')
    tree.insert(20, 'thing')
    print( tree.level_order() ) # Should be ||10, ||5, 20
    
    tree.insert(3, 'cool')
    tree.insert(2, 'that')
    print( tree.level_order() ) # Should be ||10,||3, 20,||2, 5
    
    tree.insert(4, 'is')
    print( tree.level_order() ) # Should be ||5, ||3, 10, ||2, 4, 20
    
    tree.insert(30, 'not')
    print( tree.level_order() ) # Should be ||5, ||3, 20, ||2, 4, 10, 30

    print( tree.search(4) )
