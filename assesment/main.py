# -------------------->>>>>     MENU  --  MAKER     <<<<<--------------------
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

def respondToTicket(ticket):
            if ticket.status == "Closed":
                         print("This ticket is already closed. You cannot respond to it.")
            else:
               response = input("Enter your response: ")
               ticket.response = response
               print("Response added successfully.")
               return ticket.status == "Closed"

               

# -------------------------------------<SUBMIT NEW TICKET>---------------------------------------------------------- #
def tickSub():
    newStaffID = input("Enter Staff ID: ")
    newtickCrName = input("Ticket Creator Name: ")
    newEmailID = input("Enter Email ID: ")
    tickDes = input("Enter Description of Issue: ")

    newTick = Ticket(newtickCrName, newStaffID, newEmailID, tickDes, tickStat = False, tickRes= "NOT YET PROVIDED")

    tickCrList.append(newTick)

    print("New Ticket Added")
    choice2 = input("Do you want to respond to this ticket now? (yes/no):")
    if choice2.lower() == "yes":
        respondToTicket(newTick)

    else: return

# -------------------------------------<PRINTING TICKETS>---------------------------------------------------- #

def printingticks():
    if not tickCrList:
        print("No Tickets Available.")
    else:
        for ticket in tickCrList:
            print(f"Ticket Number: {ticket.ticket_number}\n"
                  f"Ticket Creator Name: {ticket.tickCrName}\n"
                  f"Staff ID: {ticket.staffID}\n"
                  f"Email ID: {ticket.emailID}\n"
                  f"Description: {ticket.tickDes}\n"
                  f"Response: {ticket.tickRes}\n"
                  f"Ticket Status: {ticket.status}\n")
# --------------------------------------Display Ticket Statistics---------------------------------------------------
def display():

         def tickssubmitted():
             return len(tickCrList)

         def ticksresolved():
             resolved_count = sum(1 for ticket in tickCrList if ticket.status == "Closed")
             return resolved_count

         def ticksunresolved():
             unresolved_count = sum(1 for ticket in tickCrList if ticket.status != "Closed")
             return unresolved_count

         submitted = tickssubmitted()
         resolved = ticksresolved()
         unresolved = ticksunresolved()

         print(f"No. of Tickets Submitted: {submitted}\n"
               f"No. of Tickets Resolved: {resolved}\n"
               f"No. of Tickets Unresolved: {unresolved}\n")




# ---------------------------------------<MAIN-PROGRAMME>---------------------------------------------------------- #


from Tickets import Ticket
from TicketCreators import TicketCreator

tickCrList = []

tickCrdata01 = Ticket("Julian", "JULIANM", "julian@whitecliffe.co.nz", "My monitor stopped working", "Not Yet Provided", "Open")
tickCrdata02 = Ticket("Mary", "MARYL", "mary@whitecliffe.co.nz", "Request for a video camera to conduct webinars", "Not Yet Provided", "Open")
tickCrdata03 = Ticket("Sammy", "SAMMYP", "sammy@whitecliffe.co.nz", "Password change", "New password generated: SOSsp", "Closed")
tickCrList.extend([tickCrdata01, tickCrdata02, tickCrdata03])

menu1 = ["DISPLAY TICKET STATISTICS", "SUBMIT NEW TICKET","RESPOND TO TICKET", "PRINTING TICKETS"]





while True:
    choice1 = menuLoad(menu1)

    if choice1 == 0:

        print("Goodbye")

        break

    elif choice1 == 1:
        display()


    elif choice1 == 2:
      tickSub()

    elif choice1 == 3:
        respondToTicket(ticket)

    elif choice1 == 4:
        printingticks()

    else :
        continue