from bridges.bridges import *
from bridges.avl_tree_element import *
import sys


# Remember to change these params before running the script
YOUR_USER_ID = 'XXX'
YOUR_API_KEY = 'XXXXXXXXXXX'


class Node(AVLTreeElement):
    ''' 
    Inherits from class AVLTreeElement
    
    Create another attribute "num"
    :param num: number of nodes with the same key
    '''
    
	def __init__(self, key, data):
	    super().__init__(key, data)
	    self.num = 1


class AVLTree:
    ''' AVL Tree (Self-balancing Tree) '''

	def __init__(self, 
	             assignment_number=0, 
	             title='AVLTree', 
	             descr='Self-balancing Tree'):
	                      
		# Create bridges instance
		self.bridges = Bridges(assignment_number, YOUR_USER_ID, 
		                       YOUR_API_KEY)
		bridges.set_title(title)
		bridges.set_description(descr)
		
		self.root = None
		
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
            
    def _insert(self, parent, key, data): #TODO
        ''' Recursively insert & balance the tree 
        
        :param parent: The parent node we start from
        :param key: We use key to determine where to insert node at
        :param value: Any value to associate with the key
        
        :return: ???
        '''
        pass
        
    def level_order(self):
        ''' Level order traversal 
        
        Used to print the tree out, level by level 
        '''
        return self._level_order([self.root])
        
    def _level_order(self, current_level_nodes, more=None, result=''):
        if current_level_nodes == []:
            return result

        next_level_nodes = []
        result += '||'
        for node in current_level_nodes:
            result += node.data + ','
            if node.left != None:
                next_level_nodes.append(node.left)
            if node.right != None:
                next_level_nodes.append(node.right)
                
        return self._level_order(next_level_nodes, result=result)
        
    def visualize(self):
        ''' Upload the graph onto Bridges '''
        bridges.set_data_structure(self.root)
        bridges.visualize()
        
        
# If run this file (e.g. python3 AVLTree.py)
# this part of code will run 
# 
# Used to test our AVLTree       
if __name__ == '__main__':
    # Case 1
    tree1 = AVLTree()
    tree1.insert(10, 'some')
    tree1.insert(5, 'thing')
    tree1.insert(3, 'cool')
    print( tree1.level_order() ) # Should be ||5, ||3, 10
    
    # Case 2
    tree2 = AVLTree()
    tree2.insert(10, 'some')
    tree2.insert(5, 'thing')
    tree2.insert(8, 'cool')
    print( tree2.level_order() ) # Should be ||8, ||10, 5
    
    # Case 3
    tree3 = AVLTree()
    tree3.insert(10, 'some')
    tree3.insert(20, 'thing')
    tree3.insert(30, 'cool')
    print( tree3.level_order() ) # Should be ||20, ||10, 30
    
    # Case 4
    tree4 = AVLTree()
    tree4.insert(10, 'some')
    tree4.insert(20, 'thing')
    tree4.insert(15, 'cool')
    print( tree4.level_order() ) # Should be ||15, ||10, 20
    
    # General Case
    tree = AVLTree()
    tree.insert(10, 'say')
    tree.insert(5, 'some')
    tree.insert(20, 'thing')
    print( tree.level_order() ) # Should be ||10, ||5, 20
    
    tree.insert(3, 'cool')
    tree.insert(2, 'that')
    print( tree.level_order() ) # Should be ||10,||3, 20,||2, 5
    
    tree.insert(4, 'is')
    print( tree.level_order() ) # Should be ||5, ||3, 10, ||2, 4, 20
    
    tree.insert(15, 'not')
    print( tree.level_order() ) # Should be ||5, ||3, 20, ||2, 4, 10, 30 
    
