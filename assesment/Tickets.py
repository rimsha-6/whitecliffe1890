class Ticket():

    tickStat = None
    tickDes = None
    ticket_counter = 2000
    new_password = None
    tickRes = None

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






