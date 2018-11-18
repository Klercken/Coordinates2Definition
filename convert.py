# Kenny De Klerck
# 2018.11.17

# classes
class Group:
    """__init__() class constructor"""
    def __init__(self, id, x, y, l, w):
        self.id = id
        self.x1 = x
        self.y1 = y
        self.l = l
        self.w = w
        self.x2 = x + l
        self.y2 = y + w
        self.c = False


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
    coordinates = [["a",0,0,400,200]
        ,["d",0,200,800,200]
        ,["c",0,400,1000,600]
        ,["b",400,0,400,200]
        ,["e",800,0,300,200]]

    # lists
    groupInList = []
    groupOutList = []

    # create objects from input data
    for item in coordinates:
        groupInList.append(Group(item[0], item[1], item[2], item[3], item[4]))
    
    groupOutList = groupInList.copy()

    # while routine to iteratie figue definition
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
                    if not (firstGroup.id == secondGroup.id or secondGroup.c):
                        # check valid combination
                        valid = checkValid (firstGroup, secondGroup)

                        # if valid, create new combination
                        if valid:
                            # set id's as used
                            firstGroup.c = True
                            secondGroup.c = True

                            # create combination id
                            if firstGroup.x2 <= secondGroup.x1:
                                combId = firstGroup.id + "," + secondGroup.id
                            elif firstGroup.x1 >= secondGroup.x2:
                                combId = secondGroup.id + "," + firstGroup.id
                            elif firstGroup.y2 <= secondGroup.y1:
                                combId = firstGroup.id + "/" + secondGroup.id
                            else:
                                combId = secondGroup.id + "/" + firstGroup.id

                            # append combination to groupOutList
                            bounding = findBounding (firstGroup, secondGroup)
                            groupOutList.append(Group(combId, bounding[0], bounding[1], bounding[2], bounding[3]))

        
        # add remaining not grouped items in new group
        for item in groupInList:
            if not (item.c):
                groupOutList.append(Group(item.id, item.x1, item.y1, item.x2, item.y2))

        # set new group for loop
        groupInList = groupOutList.copy()

    # Check final figure definition
    print ("result: " + str(groupOutList[0].id))
