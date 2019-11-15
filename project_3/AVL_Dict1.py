import csv

#set beat to 10 because the beat numbers are listed in the 10th column:
BEAT = 10

#read the data from the file and create a list of lists called "finalList"
def readData():
    with open('Chicago_Crimes_2018-2019_Train.csv', 'r') as data:
        reader = csv.reader(data)
        finalList = list(reader)
    return finalList

#create a Dictionary where beatCount is the number of occurences of each Beat number and the actual Beat number is the key
def create_loc():
    finalList = readData()
    table1_dict = {}
    for i in range(len(finalList)):
        newBeat = (finalList[i][BEAT])
        try:
            table1_dict[newBeat] += 1
        except:
            table1_dict[newBeat] = 1
    return table1_dict

def printDict(table1_dict):
    print(60*'-')
    print(11*'-', 'Beats and their Priorities', 11*'-')
    print(60*'-')
    print(' {0:^20s} {1:^14s} '.format("Location", "Priority"))
    print(60*'-')
    # print keys and values
    count = 0
    for key, value in table1_dict.items():
        print(' {0:^20s} {1:^14,} '.format(key, value))
        count += 1

