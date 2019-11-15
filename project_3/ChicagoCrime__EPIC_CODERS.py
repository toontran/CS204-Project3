from AVLTree import *
from AVL_Dict2 import *
from AVL_Dict1 import *


class ChicagoCrimeFun:

    def __init__(self):
        self.loc_tree = AVL_Tree()
        self.crime_tree = AVL_Tree(assignment_number=1)

    def build_loc_priority(self):
        """
        Should be used to build your location-priority AVL tree
        """
        d = create_loc()

        for key in d:  
            self.root = self.loc_tree.insert( key, d[key] )  

        self.loc_tree.visualize()

    def build_crime_priority(self):
        """
        Should be used to build your crime-priority AVL tree
        """
        d = create_crime()
        
        for key in d:
            self.root = self.crime_tree.insert( key, d[key] )
          
        self.crime_tree.visualize()

    def decide_next_patrol(self, new_request=None):
        """
        You will need this later, but I'm just giving this here for you to keep it as a placeholder
        """
        pass

c = ChicagoCrimeFun()
c.build_crime_priority()
c.build_loc_priority()


