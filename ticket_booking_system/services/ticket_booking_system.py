from structures.simple_queue import SimpleQueue
from structures.priority_queue import PriorityQueue

class TicketBookingSystem:
    def __init__(self, event):
        """
        Инициализация системы бронирования.
        Время: O(1)
        Память: O(1)
        """
        self.event = event
        self.vip_queue = PriorityQueue()      # O(1)
        self.regular_queue = SimpleQueue()    # O(1)
        self.booked_seats = set()             # O(1)
        self.history = []                     # Stack для истории бронирований

    def add_user(self, user):
        """
        Добавление пользователя в соответствующую очередь.
        Время: O(1) для обычного, O(log n) для VIP
        Память: O(1)
        """
        if user.is_vip:
            self.vip_queue.push(0, user)  # O(log n)
        else:
            self.regular_queue.enqueue(user)  # O(1)

    def get_free_ticket(self):
        """
        Поиск первого свободного билета (жадный выбор).
        Время: O(n) — n = количество билетов
        Память: O(1)
        """
        free_tickets = self.event.get_free_tickets()  # O(n)
        if free_tickets:
            return free_tickets[0]
        return None

    def book_ticket(self, user):
        """
        Бронирование первого свободного билета.
        Время: O(n) на поиск + O(1) на бронирование
        Память: O(1)
        """
        ticket = self.get_free_ticket()  # O(n)
        if not ticket:
            return None
        ticket.book()                     # O(1)
        self.booked_seats.add(ticket.seat) # O(1)
        self.history.append((ticket, user)) # O(1)
        return ticket

    def cancel_last_booking(self):
        """
        Отмена последнего бронирования (стек).
        Время: O(1)
        Память: O(1)
        """
        if not self.history:
            return None
        ticket, user = self.history.pop()   # O(1)
        ticket.cancel()                     # O(1)
        self.booked_seats.remove(ticket.seat) # O(1)
        return ticket, user

    def process_bookings(self):
        """
        Обработка всех пользователей в очередях:
        VIP -> обычные.
        Время: O(m*log m + k), где m = количество VIP, k = количество обычных
        Память: O(m + k)
        """
        # VIP
        while not self.vip_queue.is_empty():
            user = self.vip_queue.pop()      # O(log m)
            self.book_ticket(user)           # O(n)
        # Обычные
        while not self.regular_queue.is_empty():
            user = self.regular_queue.dequeue() # O(1)
            self.book_ticket(user)               # O(n)

    def get_ticket_status(self):
        """
        Получение списка всех билетов с их статусом.
        Время: O(n)
        Память: O(n)
        """
        return self.event.tickets