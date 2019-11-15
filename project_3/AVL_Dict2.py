import csv

#set description to 6 because the descriptions are listed in the 6th column:
prim_type = 5
iucr_row = 4

predes = ['NON-CRIMINAL (SUBJECT SPECIFIED)','NON-CRIMINAL','OTHER OFFENSE','OTHER NARCOTIC VIOLATION','OBSCENITY','PUBLIC PEACE VIOLATION','LIQUOR LAW VIOLATION','CONCEALED CARRY LICENSE VIOLATION','STALKING','PUBLIC INDECENCY','GAMBLING','PROSTITUTION','DECEPTIVE PRACTICE','ROBBERY','THEFT','BURGLARY','CRIMINAL DAMAGE','MOTOR VEHICLE THEFT','CRIMINAL TRESPASS','NARCOTICS','WEAPONS VIOLATION','INTERFERENCE WITH PUBLIC OFFICER','INTIMIDATION','BATTERY','ARSON','KIDNAPPING','OFFENSE INVOLVING CHILDREN','HUMAN TRAFFICKING','SEX OFFENSE','ASSAULT','CRIM SEXUAL ASSAULT','HOMICIDE']

def readData():
    with open('Chicago_Crimes_2018-2019_Train.csv', 'r') as data:
        reader = csv.reader(data)
        finalList = list(reader)
        	
    return finalList

#create a Dictionary where the priority is the value and the "IUCR" is the key
def createDict():
    finalList = readData()
    table1_dict = {}
    
    for i in range(1,len(finalList)):
        desc = (finalList[i][prim_type])
        iucr = (finalList[i][iucr_row])
        table1_dict[iucr] = predes.index(desc)
    return table1_dict

def printDict():
    table1_dict = createDict()
    print(60*'-')
    print(11*'-', 'IUCR and their Priorities', 11*'-')
    print(60*'-')
    print(' {0:^20s} {1:^14s} '.format("IUCR", "Priority"))
    print(60*'-')
    # print keys and values
    count = 0
    for key, value in table1_dict.items():
        print(' {0:^20s} {1:^14,} '.format(key, value))
        count += 1

