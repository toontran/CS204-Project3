#Our Method

We started by reading in the data from the csv file and creating two dictionaries. One dictonary holds data used in our Location Priority AVL Tree, and another dictionary holds the data used in our Crime Priority AVL Tree.

The first AVL Tree uses a beat as the key. A beat is a unique four-digit number which represents a location in Chicago. The value (the priority) is the number of times that the beat appears in the crime data. Essentially this means that more crime reports filed in one location, equates to a higher priority for that beat. 

The second AVL Tree uses the IUCR number as the key. The IUCR number is a unique four-digit number which represents a specific type of crime located in the csv file. The value is the indice of a list we created ranking the "badness" of an individual crime. We obviously understand this list is subjective and we're not experts so that priority might have to be something we reconsider in later phases. For example, the first thing in the list has an indice of 0 so it also has a low priority.

##The list we used to determine priority for our second tree
'''
['NON-CRIMINAL (SUBJECT SPECIFIED)','NON-CRIMINAL','OTHER OFFENSE','OTHER NARCOTIC VIOLATION','OBSCENITY','PUBLIC PEACE VIOLATION','LIQUOR LAW VIOLATION','CONCEALED CARRY LICENSE VIOLATION','STALKING','PUBLIC INDECENCY','GAMBLING','PROSTITUTION','DECEPTIVE PRACTICE','ROBBERY','THEFT','BURGLARY','CRIMINAL DAMAGE','MOTOR VEHICLE THEFT','CRIMINAL TRESPASS','NARCOTICS','WEAPONS VIOLATION','INTERFERENCE WITH PUBLIC OFFICER','INTIMIDATION','BATTERY','ARSON','KIDNAPPING','OFFENSE INVOLVING CHILDREN','HUMAN TRAFFICKING','SEX OFFENSE','ASSAULT','CRIM SEXUAL ASSAULT','HOMICIDE']
'''

To create an AVL Tree, we added code to the "insert" function of a normal Binary Search Tree. We started on paper, working on balancing trees to understand the process before moving into the code. We used conditional cases to determine how we needed to balance the tree.

We used Bridges to visualize our two trees, and visualize the key/value pairs created from these dictionaries. 
We also learned to use a little bit of github to help with workflow.
