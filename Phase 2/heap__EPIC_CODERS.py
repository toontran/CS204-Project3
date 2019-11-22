from bridges.bridges import *
from bridges.avl_tree_element import *
import math
import sys
from time import sleep
from random import randint


# Remember to change these params before running the script
YOUR_USER_ID = 'tungtran'
YOUR_API_KEY = '361152011190'


class Node(AVLTreeElement):
    ''' 
    Inherits from class AVLTreeElement
    
    Create another attribute "num"
    :param num: number of nodes with the same key
    '''
    
    def __init__(self, key, data=''):
    
        if str( type(data) ) != "<class 'list'>":
            self.data = [data]
    
        super().__init__(key, data)
        self.num = 1
        self.height = 1
        self.label = str(data)
        
    def append(self, data):
        self.num += 1
        self.data.extend(data) 


class Heap:
    
    def __init__(self, is_min_heap=True):
        
        # Heap stored in a list
        self.list = []
        self.is_min_heap = is_min_heap
        
    def __len__(self):
        return len(self.list)
        
    def __str__(self):
        return str( self._level_order([self.list[0]]) )
        
    def insert(self, key, value=''):
        if len(self) == 0:
            root = Node(key, value)
            self.list.append(root)
        else:
            node = Node(key, value)
            self.list.append(node)
            self._sift_up( len(self)-1 )
        
    def _sift_up(self, child_idx):
        if child_idx == 0: # Stop
            return
    
        current_layer = self.get_layer(child_idx)
        parent_layer = current_layer - 1
        
        difference = ( child_idx-self.get_first_index(current_layer) ) // 2
        parent_idx = self.get_first_index(parent_layer) + difference
        is_left_node = ( child_idx-self.get_first_index(current_layer) ) % 2 == 0
        
        # swap_children
        if self.is_min_heap:
            if self.list[child_idx].key >= self.list[parent_idx].key:
                if is_left_node:
                    self.list[parent_idx].left = self.list[child_idx]
                else:
                    self.list[parent_idx].right = self.list[child_idx]
                return # Stop
            else:
                temp = self.list[child_idx]
                self.list[child_idx], self.list[parent_idx] = \
                    self.list[parent_idx], temp
                    
                self.connect(parent_idx, child_idx, is_left_node) # Connect
                self._sift_up(parent_idx) # Recurse
        else:
            if self.list[child_idx].key <= self.list[parent_idx].key:
                if is_left_node:
                    self.list[parent_idx].left = self.list[child_idx]
                else:
                    self.list[parent_idx].right = self.list[child_idx]
                return # Stop
            else:
                temp = self.list[child_idx]
                self.list[child_idx], self.list[parent_idx] = \
                    self.list[parent_idx], temp
                    
                self.connect(parent_idx, child_idx, is_left_node) # Connect
                self._sift_up(parent_idx) # Recurse
        
    def connect(self, parent_idx, child_idx, is_left_node):
        #print('Parent_idx {}, child_idx {}'.format(parent_idx, child_idx) )
        if is_left_node:
            parent_left = self.list[parent_idx].left
            parent_right = self.list[parent_idx].right
            child_left = self.list[child_idx].left
            child_right = self.list[child_idx].right
            
            self.list[parent_idx].left = self.list[child_idx] # Real connection
            self.list[parent_idx].right = child_right
            self.list[child_idx].left = parent_left
            self.list[child_idx].right = parent_right
        else:
            parent_left = self.list[parent_idx].left
            parent_right = self.list[parent_idx].right
            child_left = self.list[child_idx].left
            child_right = self.list[child_idx].right
            
            self.list[parent_idx].left = child_left 
            self.list[parent_idx].right = self.list[child_idx] # Real connection
            self.list[child_idx].left = parent_left
            self.list[child_idx].right = parent_right
            
        
    def get_layer(self, index):
        return int( math.log(index+1,2) ) # log2 of index+1
        
    def get_first_index(self, layer:int):
        ''' Get the index of the first node of a specified layer '''
        return 2**layer-1 
    
    def pop(self): 
        #find a node with a certain value then remove it from the end
        last_index = len( self.list ) - 1
        last_node = self.list[last_index]
        if last_index % 2 == 1:
            parent_index = (last_index-1) // 2
            self.list[parent_index].left = None
        else:
            parent_index = (last_index-2) // 2
            self.list[parent_index].right = None
        
        # Replace the root with the last node and set all the connections
        root = self.list[0]
        self.list[0] = last_node
        self.list[0].left = root.left
        self.list[0].right = root.right
        
        self.list.pop()
        self.sift_down(self.list, 0, len(self.list), is_min_heap=self.is_min_heap)
        self.make_connection()
        
    def visualize(self, assignment_number=0):
        ''' Upload the graph onto Bridges '''
        # Create a bridges instance
        self.bridges = Bridges(assignment_number, YOUR_USER_ID, 
                               YOUR_API_KEY)
        
        self.bridges.set_data_structure(self.list[0])
        self.bridges.visualize()
        
    def _level_order(self, current_level_nodes, more=None, result=''):
        if current_level_nodes == []:
            return result

        next_level_nodes = []
        result += '||'
        for node in current_level_nodes:
            result += '{},'.format(node.key)
            if node.left != None:
                next_level_nodes.append(node.left)
            if node.right != None:
                next_level_nodes.append(node.right)
                
        return self._level_order(next_level_nodes, result=result)
        
    def get_list(self):
        return [x.key for x in self.list]
        
    def sift_down(self, lst, idx, size, is_min_heap=True):
        lchild = 2*idx + 1
        rchild = 2*idx + 2
        if lchild > size-1:
            return
        elif rchild > size-1:
            rchild = None
        
        if is_min_heap:
            if lst[idx].key <= lst[lchild].key and ((rchild != None and lst[idx].key <= lst[rchild].key) or \
                                            rchild == None):
                return
            elif rchild == None or lst[lchild].key < lst[rchild].key:
                lst[lchild], lst[idx] = lst[idx], lst[lchild]
                self.sift_down(lst, lchild, size, is_min_heap=is_min_heap)
            else:
                lst[rchild], lst[idx] = lst[idx], lst[rchild]
                self.sift_down(lst, rchild, size, is_min_heap=is_min_heap)
        else:
            if lst[idx].key >= lst[lchild].key and ((rchild != None and lst[idx].key >= lst[rchild].key) or \
                                            rchild == None):
                return
            elif rchild == None or lst[lchild].key > lst[rchild].key:
                lst[lchild], lst[idx] = lst[idx], lst[lchild]
                self.sift_down(lst, lchild, size, is_min_heap=is_min_heap)
            else:
                lst[rchild], lst[idx] = lst[idx], lst[rchild]
                self.sift_down(lst, rchild, size, is_min_heap=is_min_heap)
                
    def make_connection(self, idx=0):
        lchild = 2*idx + 1
        rchild = 2*idx + 2
        
        if lchild > len(self.list)-1:
            lchild = None
        if rchild > len(self.list)-1:
            rchild = None
        
        
        if lchild != None:
            self.list[idx].left = self.list[lchild]
            self.make_connection(idx=lchild)
        else:
            self.list[idx].left = None
        
        if rchild != None:
            self.list[idx].right = self.list[rchild]
            self.make_connection(idx=rchild)
        else:
            self.list[idx].right = None
            return
                
            
def heap_sort(l, is_min_heap=True):
    # Not efficient, could be dealt w some other times

    heap = Heap(is_min_heap=is_min_heap)
    for x in l:
        heap.insert(x[0])
    l = [[x, l[i][1]] for i, x in enumerate(heap.get_list())]
    
    for i in range( len(l)-1 ):
        l[0], l[-1-i] = l[-1-i], l[0] # swap_children the root and the last element
        sift_down(l, 0, len(l)-i-1, is_min_heap=is_min_heap)
    return l
    
    
def sift_down(lst, idx, size, is_min_heap=True):
    lchild = 2*idx + 1
    rchild = 2*idx + 2
    if lchild > size-1:
        return
    elif rchild > size-1:
        rchild = None
    
    if is_min_heap:
        if lst[idx][0] <= lst[lchild][0] and ((rchild != None and lst[idx][0] <= lst[rchild][0]) or \
                                        rchild == None):
            return
        elif rchild == None or lst[lchild][0] < lst[rchild][0]:
            lst[lchild], lst[idx] = lst[idx], lst[lchild]
            sift_down(lst, lchild, size, is_min_heap=is_min_heap)
        else:
            lst[rchild], lst[idx] = lst[idx], lst[rchild]
            sift_down(lst, rchild, size, is_min_heap=is_min_heap)
    else:
        if lst[idx][0] >= lst[lchild][0] and ((rchild != None and lst[idx][0] >= lst[rchild][0]) or \
                                        rchild == None):
            return
        elif rchild == None or lst[lchild][0] > lst[rchild][0]:
            lst[lchild], lst[idx] = lst[idx], lst[lchild]
            sift_down(lst, lchild, size, is_min_heap=is_min_heap)
        else:
            lst[rchild], lst[idx] = lst[idx], lst[rchild]
            sift_down(lst, rchild, size, is_min_heap=is_min_heap)
            
    
    
if __name__ == '__main__':
    # Test heap sort
    min_heap = Heap()
    s = [[randint(1,100),1] for x in range(100)]
    print(s)
    s_sort = heap_sort(s, is_min_heap=False)
    print(s_sort)
    s.sort()
    print( s == s_sort )
    
    # Test pop
    heap = Heap()
    s = [[randint(1,100),x+1] for x in range(100)]
    for x in s:
        heap.insert(x[0], value=x[1:])
        
    heap.visualize(assignment_number=10)
    print(heap.pop())
    heap.visualize(assignment_number=11)
