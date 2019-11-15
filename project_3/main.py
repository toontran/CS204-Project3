import pandas as pd 
from AVLTree import *
from AVL_Dict2 import *


class ChicagoCrimeFun:

    def __init__(self):
        self.data = pd.read_csv("Chicago_Crimes_2018-2019_Train.csv")
       

    def build_loc_priority(self):
        """
        Should be used to build your location-priority AVL tree
        """
        self.loc_tree = AVL_Tree()
        self.root = None
        d = self.data['Beat'].value_counts()

        for key, value in d.iteritems():  
            self.root = self.loc_tree.insert( key, value )  

        self.loc_tree.visualize()

    def build_crime_priority(self):
        """
        Should be used to build your crime-priority AVL tree
        """
        self.crime_tree = AVL_Tree(assignment_number=1)
        self.root = None
        d = createDict()
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


