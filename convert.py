# Kenny De Klerck
# 2019.01.19

# classes
class Group:
    """__init__() class constructor"""
    def __init__(self, id, x1, y1, x2, y2, d):
        self.id = id
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.c = False
        # direction: <empty>: none, V = /-division, H = ,-division
        self.d = d


# functions
def findBounding (first=Group, second=Group):
    # define list
    bounding =  [0] * 6

    # add items to list
    bounding[0] = min (first.x1, second.x1)
    bounding[1] = min (first.y1, second.y1)
    bounding[2] = max (first.x2, second.x2)
    bounding[3] = max (first.y2, second.y2)
    bounding[4] = first.id
    bounding[5] = second.id

    # return result
    return bounding
    

def checkCollision (bounding=[], groupList=[]):
    # loop through list and check whether they collide with the bounding rectangle
    for item in groupList:
        # set starting value
        collision = False

        # filter id's in group
        if (bounding[4] != item.id and bounding[5] != item.id):
            # check collision
            if not (bounding[0] >= (item.x2) or bounding[2] <= item.x1 or bounding[1] >= (item.y2) or bounding[3] <= item.y1):
                collision = True
                return collision
    
    # return value
    return collision


def checkValid (first=Group, second=Group):
    # get bounding
    bounding = findBounding (first, second)

    # check collision
    collision = checkCollision (bounding, groupInList)

    # return result
    return not (collision)


# main routine
if __name__ == "__main__":
    # rectangle input list
    # coordinates = [["a",0,0,400,200]
    #     ,["d",0,200,800,200]
    #     ,["c",0,400,1000,600]
    #     ,["b",400,0,400,200]
    #     ,["e",800,0,300,200]]

    # coordinates = [["a", 0, 50, 40, 140]
    #     ,["b", 50, 160, 110, 30]
    #     ,["c", 50, 120, 40, 30]
    #     ,["d", 100, 140, 30, 10]
    #     ,["e", 100, 120, 30, 10]
    #     ,["f", 140, 120, 20, 30]
    #     ,["g", 50, 80, 110, 30]
    #     ,["h", 50, 50, 70, 20]
    #     ,["i", 130, 50, 30, 20]
    #     ,["j", 0, 0, 160, 40]
    #     ,["k", 170, 0, 50, 190]
    #     ]

    coordinates = [["a", 0, 0, 50, 100]
        ,["b", 60, 0, 100, 30]
        ,["c", 60, 60, 70, 20]
        ,["d", 140, 60, 20, 50]
        ,["e", 0, 110, 130, 20]]

    # lists
    groupInList = []
    groupOutList = []

    # create objects from input data
    for item in coordinates:
        groupInList.append(Group(item[0], item[1], item[2], item[1] + item[3], item[2] + item[4], ""))
    
    groupOutList = groupInList.copy()

    # while routine to iteratie figure definition
    while len(groupOutList) > 1:
        # reset group out
        groupOutList.clear()

        # loop through all groups
        for firstGroup in groupInList:
            # if group is used in stored combination, skip
            if not (firstGroup.c):
                # run through groups for second item in combination
                for secondGroup in groupInList:
                    # if same as first group, or in use, skip
                    if not (firstGroup.id == secondGroup.id or firstGroup.c or secondGroup.c):
                        # check valid combination
                        valid = checkValid (firstGroup, secondGroup)

                        # if valid, create new combination
                        if valid:
                            # set id's as used
                            firstGroup.c = True
                            secondGroup.c = True

                            # create combination id
                            # 1 left of 2
                            if firstGroup.x2 <= secondGroup.x1:
                                d = "H"
                                if (firstGroup.d == "V" and secondGroup.d == "V"):
                                    combId = "(" + firstGroup.id + "),(" + secondGroup.id + ")"
                                elif (firstGroup.d == "V"):
                                    combId = "(" + firstGroup.id + ")," + secondGroup.id
                                elif (secondGroup.d == "V"):
                                    combId = firstGroup.id + ",(" + secondGroup.id + ")"
                                else:
                                    combId = firstGroup.id + "," + secondGroup.id

                            # 1 right of 2
                            elif firstGroup.x1 >= secondGroup.x2:
                                d = "H"
                                if (secondGroup.d == "V" and firstGroup.d == "V"):
                                    combId = "(" + secondGroup.id + "),(" + firstGroup.id + ")"
                                elif (secondGroup.d == "V"):
                                    combId = "(" + secondGroup.id + ")," + firstGroup.id
                                elif (firstGroup.d == "V"):
                                    combId = secondGroup.id + ",(" + firstGroup.id + ")"
                                else:
                                    combId = secondGroup.id + "," + firstGroup.id

                            # 1 below 2
                            elif firstGroup.y1 >= secondGroup.y2:
                                d = "V"
                                if (firstGroup.d == "H" and secondGroup.d == "H"):
                                    combId = "(" + firstGroup.id + ")/(" + secondGroup.id + ")"
                                elif (firstGroup.d == "H"):
                                    combId = "(" + firstGroup.id + ")/" + secondGroup.id
                                elif (secondGroup.d == "H"):
                                    combId = firstGroup.id + "/(" + secondGroup.id + ")"
                                else:
                                    combId = firstGroup.id + "/" + secondGroup.id
                                    
                            # 1 above 2
                            else:
                                d = "V"
                                if (secondGroup.d == "H" and firstGroup.d == "H"):
                                    combId = "(" + secondGroup.id + ")/(" + firstGroup.id + ")"
                                elif (secondGroup.d == "H"):
                                    combId = "(" + secondGroup.id + ")/" + firstGroup.id
                                elif (firstGroup.d == "H"):
                                    combId = secondGroup.id + "/(" + firstGroup.id + ")"
                                else:
                                    combId = secondGroup.id + "/" + firstGroup.id

                            # append combination to groupOutList
                            bounding = findBounding (firstGroup, secondGroup)
                            groupOutList.append(Group(combId, bounding[0], bounding[1], bounding[2], bounding[3], d))

        
        # add remaining not grouped items in new group
        for item in groupInList:
            if not (item.c):
                groupOutList.append(Group(item.id, item.x1, item.y1, item.x2, item.y2, item.d))

        # set new group for loop
        groupInList = groupOutList.copy()

    # Check final figure definition
    print ("result: " + str(groupOutList[0].id))
