# Kenny De Klerck
# 2018.11.17

# classes
class Part:
    """__init__() class constructor"""
    def __init__(self, id, x, y, l, w):
        self.id = id
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.c = False

class Combination:
    """__init__() class constrtuctor"""
    def __init__(self, first=Part, second=Part):
        self.first = first
        self.second = second
        self.x = min(self.first.x, self.second.x)
        self.y = min(self.first.y, self.second.y)
        self.l = max(self.first.x + self.first.l, self.second.x + self.second.l)
        self.w = max(self.first.y + self.first.w, self.second.y + self.second.w)


# main routine
if __name__ == "__main__":
    # rectangle input list
    coordinates = [["a",0,0,400,200]
        ,["b",400,0,400,200]
        ,["c",0,200,1000,600]]

    # lists
    partList = []
    groupList = []

    # create objects from input data
    for item in coordinates:
        partList.append(Part(item[0], item[1], item[2], item[3], item[4]))

    # loop through all parts as first part of a bounding rectangle
    for firstpart in partList:
        # if part is used in stored combination, skip
        if (firstpart.c):
            print ("id in use: " + firstpart.id)

        # else use it as first part
        else:
            # run through parts for second part in combination
            for secondpart in partList:
                # if same as first part, or in use, skip
                if (firstpart.id == secondpart.id or secondpart.c):
                    print ("id in use or skipped: secondpart.id")
                
                # else use as second part in combination
                else:
                    # create combination
                    firstpart.id + secondpart.id = Combination(firstpart, secondpart)

                    # print bounding
                    print (pipo.l)

