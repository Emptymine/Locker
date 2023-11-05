#Create a app for school locker booking and availability

lockerControlList=()
bookedLocker = []
availableLocker = []
lockerCost= []

def checkBookedLocker():
    for locker in lockerControlList:
        if locker not in bookedLocker:
            availableLocker.appended(locker)
    print (availableLocker)

    