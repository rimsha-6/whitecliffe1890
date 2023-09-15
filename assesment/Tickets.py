class Ticket():

    tickDes = None
    ticket_counter = 2000

    def __init__(self, tickCrName, staffID, emailID, tickDes, tickRes, tickStat):
        self.status = tickStat
        self.ticket_number = Ticket.ticket_counter  # Assign a unique ticket number
        Ticket.ticket_counter += 1
        self.tickCrName = tickCrName
        self.staffID = staffID
        self.emailID = emailID
        self.tickDes = tickDes
        self.tickRes = tickRes
        self.tickStat = tickStat
        self.response = "Not Yet Provided."


    @classmethod
    def generate_password(cls):
        pass


def generate_password(self):
    # Combine the first two characters of staffID and the first 3 characters of tickCrName
    new_password = self.staffID[:2] + self.tickCrName[:3]
    return new_password

if Ticket.tickDes == "Password Change":
    new_password = Ticket.generate_password()
    print(f"Generate New Password: {new_password}")





