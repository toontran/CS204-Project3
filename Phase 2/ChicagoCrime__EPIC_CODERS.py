from AVLTree_EpicCoders import *
from AVL_Dict2 import *
from AVL_Dict1 import *
from Heap__EpicCoders import *
import numpy as np
import pandas


class ChicagoCrimeFun:

    def __init__(self):
        self.loc_tree = AVL_Tree("loc")
        self.crime_tree = AVL_Tree("crime", assignment_number=1)
        """
        Dispatch Queue
        """
        self.dispatch_queue = Heap()
        self.past_queue = Heap()
        self.build_loc_priority()
        self.build_crime_priority()
        
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

    def add_dispatch(self, dispatch_string):
        '''
        Method to add a dispatch to our dispatch_queue
        Parameters:
          dispatch_string: [string] A string that represents a recent 911 dispatch call request that is reported to the police
        '''
        split_dispatch_string = dispatch_string.split(', ')
        beat = int(split_dispatch_string[12])
        IUCR = int(split_dispatch_string[5])

        location_priority = self.loc_tree.search(beat)
        crime_priority = self.crime_tree.search(IUCR)
        
        if loc_priority == None:
            loc_priority = 1000
        if crime_priority == None:
            crime_priority = 10
        
        total_priority = location_priority + crime_priority

        self.dispatch_queue.insert(total_priority, dispatch_string)

    def get_surrounding_area(self, point):
        if str(point) == 'nan':
            return None
        
        point = point.strip(')').strip('(').split(', ')
        Latitude, Longitude = float(point[0]), float(point[1])
        Top_Left = ((Latitude-0.002), (Longitude+0.0025))
        Top_Right = ((Latitude+0.002), (Longitude+0.0025))
        Bottom_Left = ((Latitude-0.002), (Longitude-0.0025))
        Bottom_Right = ((Latitude+0.002), (Longitude-0.0025))

        location_area = (Top_Left, Top_Right, Bottom_Left, Bottom_Right)
        return location_area

    def get_coordinates(self, dispatch_string):
        '''
        Method to get a set of four tuples which will create an area around our BEAT
        Returns a tuple of 4 tuples
        '''
        split_dispatch_string = dispatch_string.split(', ')
        Latitude = int(split_dispatch_string[21])
        Longitude = int(split_dispatch_string[22])

        return self.get_surrounding_area( (Latitude, Longitude) )

    def decide_next_patrol(self, new_request = None):
        """
        You will need this later, but I'm just giving this here for you to keep it as a placeholder
        """
        if new_request != None:
            self.add_dispatch(new_request)

        if len(self.dispatch_queue) != 0:
            dispatch_string = self.dispatch_queue.pop()
            location = self.get_coordinates(dispatch_string)
            return location
        else:
            data = pandas.read_csv('Chicago_Crimes_2018-2019_Train.csv')
            self.crime_priority_list = []
            for i in range(data.shape[0]//15): # Can't read more than
                loc_priority = self.loc_tree.search(data['Beat'][i])
                crime_priority = self.crime_tree.search(data['IUCR'][i])
                
                if loc_priority == None:
                    loc_priority = 1000
                if crime_priority == None:
                    crime_priority = 10
                
                total_priority = loc_priority + crime_priority
                location_area = self.get_surrounding_area(data['Location'][i])
                if location_area == None:
                    continue
                self.past_queue.insert(total_priority, location_area)
                
            self.past_queue.visualize(assignment_number=3)
            self.crime_priority_list = heap_sort([[x.key, x.value] for x in self.past_queue.list])
            return self.crime_priority_list[0]


if __name__ == '__main__':
    c = ChicagoCrimeFun()
    print(c.decide_next_patrol())

#http://bridges-cs.herokuapp.com/assignments/3/tungtran
