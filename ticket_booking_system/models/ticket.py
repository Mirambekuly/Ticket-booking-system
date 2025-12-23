class Ticket:
    def __init__(self, ticket_id, seat, category='Standard', price=100):
        self.ticket_id = ticket_id
        self.seat = seat
        self.category = category
        self.price = price
        self.is_booked = False

    def book(self):
        if self.is_booked:
            return False
        self.is_booked = True
        return True

    def cancel(self):
        self.is_booked = False

    def __repr__(self):
        status = "Booked" if self.is_booked else "Free"
        return f"Ticket {self.ticket_id} | Seat {self.seat} | {self.category} | {status}"
