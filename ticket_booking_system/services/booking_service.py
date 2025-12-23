class BookingService:
    def __init__(self, event):
        self.event = event
        self.booked_seats = set()

    def book_ticket(self, user):
        ticket = self.event.get_free_ticket()

        if not ticket:
            print("❌ No free tickets available")
            return

        ticket.book()
        self.booked_seats.add(ticket.seat)

        print(f"✅ Ticket booked for {user.name}: {ticket}")
