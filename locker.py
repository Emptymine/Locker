#Create a app for school locker booking and availability

lockerControlList=("a1", "a2", "a3", "a4", "a5", "a6", "b7", "b8", "b9", "b10", "c3", "c4", "c5", "c6", "c7")
bookedLocker = []
availableLocker = []
lockerCost= []

class locker:
    def __init__(self,lockerName, lockerLocation, lockerBookedDate, lockerAvilableDate, lockerTenant, payment):
        self.lockerName = lockerName
        self.lockerLocation = lockerLocation
        self.lockerBookedDate = lockerBookedDate
        self.lockerAvailableDate = lockerAvilableDate
        self.lockerTenant = lockerTenant
        self.payment = payment
    def __str__(self):
        return f"{self.lockerName} -- {self.lockerLocation} -- {self.lockerAvailableDate} -- {self.lockerBookedDate} -- {self.lockerTenant} -- {self.payment}"

def checkBookedLocker():
    availableLocker = []
    for locker in lockerControlList:
        if locker not in bookedLocker:
            availableLocker.append(locker)
    print (f"{availableLocker}")
    print (f"The total available locker is {len(availableLocker)}.\n")

def showTotalLocker():
    for locker in lockerControlList:
        print (f"{locker}",end="--",sep="**")

def createlockerlist():
    lockerList = open("lockerlist.txt","w")

createlockerlist()

def showbooked():
    if bookedLocker:
        print (bookedLocker.count())
        print (bookedLocker)
    else:
        print ("There is no locked booked")


endProgram = False
while endProgram !=True: 
    print("Welcome to the locker control application. Please enter the function number you want:")
    Userinput = int(input("1. Check Total locker\n2. Check booked locker\n3. Check available locker\n4. Book a locker\n5. Reserve a locker\n6. Check next available date of the locker\n7. End program\n"))

    match Userinput:
        case 1:
            showTotalLocker()
        case 2: 
            showbooked()
        case 3:
            checkBookedLocker()
        case 7:
            endProgram = True
            print ("Thank you for using this program!")
