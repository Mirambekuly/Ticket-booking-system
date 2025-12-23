class Event:
    def __init__(self, event_id, name):
        self.event_id = event_id
        self.name = name
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_free_tickets(self):
        return [t for t in self.tickets if not t.is_booked]