# -------------------->>>>>    MENU  ----  MAKER    <<<<<--------------------
def menuLoad(menu):
    count = 1
    for z in menu:
        print(f"{count}. {z}")
        count += 1
    print(f"0. EXIT")
    selection = input("\nEnter Number: ")

    if selection.isnumeric():
        selection = int(selection)
        if selection not in range(0, count):
            print("\nError: Number outside range\n")
            selection = 99
    else:
        print("\nError: Input must be a Number\n")
        selection = 99

    return selection


# -------------------->>>>>    RENTAL  Functions    <<<<<--------------------
def rNew(vRent, cRent):
    rCost = int(0)

    if cRent.currRental != None:
        print(f"Client currently renting: {cRent.currRental.vYear} {cRent.currRental.vMake} {cRent.currRental.vModel}")
    else:
        cDays = int(input("Enter Number of Rental Days: "))
        rCost = cDays * vRent.vCost

        cRent.currRental = vRent
        cRent.cOwing = rCost

        vRent.vRenter = cRent
        vRent.vStatus = False

        print(f"{cRent.cFName} {cRent.cLName} {vRent.vYear} {vRent.vMake} {vRent.vModel} = {rCost}")

def rUnpaid():
    for u in cList:
        if u.cOwing > 0:
            print(f"{u.cFName} {u.cLName} = {u.cOwing}")


def rPay():
    payMenu = []

    for u in cList:

            payMenu.append(f"{u.cFName} {u.cLName} = {u.getMoney( branch)}")


            payAcct = menuLoad(payMenu)

    if payAcct != 0 or payAcct != 99:
       amt = int(input("Enter Amount to Pay: "))
      cPay = cList[payAcct - 1]
      cPay.cOwing -= amt
      print(f"Total Owing = {cPay.cOwing}")

      if cPay.cOwing == 0:
           cPay.currRental.vRenter = None
           cPay.currRental.vStatus = True

           cPay.prevRentals.append(cPay.currRental)
           cPay.currRental = None




# -------------------->>>>>    VEHICLE Functions    <<<<<--------------------
def vFind():

    vTemp = []
    found = 0

    for v in vList:
        if v.vStatus == True:
            vTemp.append(f"{v.vYear} {v.vMake} {v.vModel}: Cost Per Day = {v.vCost}")


    test = menuLoad(vTemp)

    if test != 0:
        found = vList[test - 1]

    return found

"""
    if len(vTemp) == 0:
        print("Nothing Rented")
    else:
        for t in vTemp:
            printf"{t.vYear} {t.vMake} {v.vModel}( "
                  f"Renter: {t.vRenter.cFName} {t.vRenter.cLName}")
"""

def vAdd():
    print("Create Code")


# -------------------->>>>>   CUSTOMER Functions    <<<<<--------------------
def cFind():
    tempFind = []
    found = 0
    for t in cList:
        tempFind.append(f"{t.cFName} {t.cLName}")
    cSeek = menuLoad(tempFind)

    if cSeek != 0:
        found = cList[cSeek - 1]
        print(found)

    return found



def cEdit(clientToEdit):
    print("Create Code")


def cAdd():
    print("Create Code")


# -------------------->>>>>      MAIN  PROGRAM      <<<<<--------------------

from Clients import Client
from Vehicles import Vehicle

# -------------------->>>>>       CLASS Lists       <<<<<--------------------
vList = []
cList = []
unPaid = []
# -------------------->>>>>           DATA          <<<<<--------------------
vDat01 = Vehicle("FORD", "Everest", 2020, "IXL595", 80, 23243)
vDat02 = Vehicle("FORD", "Focus", 2020, "VNV530", 75, 70167)
vDat03 = Vehicle("FORD", "Focus", 2021, "ITH219", 85, 36666)
vDat04 = Vehicle("FORD", "Mondeo", 2019, "MDB711", 70, 40235)
vDat05 = Vehicle("FORD", "Mondeo", 2020, "XTF180", 80, 25576)
vDat06 = Vehicle("HOLDEN", "Captiva", 2019, "INB968", 70, 69428)
vDat07 = Vehicle("HOLDEN", "Captiva", 2020, "ANV107", 80, 66349)
vDat08 = Vehicle("HOLDEN", "Commodore", 2019, "TEO323", 90, 36713)
vDat09 = Vehicle("HOLDEN", "Commodore", 2020, "RZV716", 100, 55530)
vDat10 = Vehicle("HOLDEN", "Cruze", 2019, "IBT944", 70, 70741)

vList.extend([vDat01, vDat02, vDat03, vDat04, vDat05, vDat06, vDat07, vDat08, vDat09, vDat10])

cDat01 = Client("Harry", "Abraham", "(020) 403 6704", "harry.abraham@somemail.co.nz")
cDat02 = Client("Simon", "Brown", "(027) 185 9643", "simon.brown@somemail.co.nz")
cDat03 = Client("Carl", "Abraham", "(029) 061 5554", "carl.abraham@somemail.co.nz")
cDat04 = Client("Jonathan", "North", "(020) 632 1503", "jonathan.north@somemail.co.nz")
cDat05 = Client("Theresa", "Morgan", "(021) 393 7110", "theresa.morgan@somemail.co.nz")

cList.extend([cDat01, cDat02, cDat03, cDat04, cDat05])
# -------------------->>>>>       MENU  Lists       <<<<<--------------------
mainMenu = ["Rental Menu", "Vehicle Menu", "Client Menu"]
rMenu = ["New Rental", "Unpaid", "Pay Account"]
vMenu = ["Find Vehicle", "All Rented", "Show All Vehicles", "Create New Vehicle"]
cMenu = ["Find Client", "All Clients", "Edit Client", "Create New Client"]
# -------------------->>>>>        MAIN LOOP        <<<<<--------------------
while True:
    print("\n----->>>>> Welcome to the Car Rental Main Menu <<<<<-----")
    choice1 = menuLoad(mainMenu)

    if choice1 == 0:
        print("Goodbye")
        break
    # ---------->>>>> RENTAL  Menu <<<<<----------#
    elif choice1 == 1:
        rOut = menuLoad(rMenu)

        if rOut == 1:
            vGet = vFind()
            cGet = cFind()

            if vGet == 0 or cGet == 0:
                print("Something helpful!?")

            else:
                rNew(vGet, cGet)
        elif rOut == 2:
            rUnpaid()

        elif rOut == 3:
            rPay()

        else:
            continue

    # ---------->>>>> VEHICLE Menu <<<<<----------#
    elif choice1 == 2:
        vOut = menuLoad(vMenu)

        if vOut == 1:
            vFound = vFind()
            print(vFound)

        elif vOut == 2:
            test = 0
            for v in vList:
                if v.vStatus == False:
                    print(f"{v.vYear} {v.vMake} {v.vModel}")
                    test += 1
            if test == 0:
                print("Nothing Rented")

        elif vOut == 3:
            for v in vList:
                print(f"{v.vYear} {v.vMake} {v.vModel}")

        elif vOut == 4:
            vAdd()

        else:
            continue


    # ---------->>>>> CLIENT  Menu <<<<<----------#
    elif choice1 == 3:
        cOut = menuLoad(cMenu)

        if cOut == 1:
            cFound = cFind()

        elif cOut == 2:
            for c in cList:
                print(f"{c.cFName} {c.cLName}")

        elif cOut == 3:
            cFound = cFind()

            if cFound != 0:
               cEdit(cFound)

            else:
                 print("Client not found")

        elif cOut == 4:
            cAdd()

        else:
            continue








