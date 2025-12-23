from models.user import User
from models.ticket import Ticket
from models.event import Event
from services.ticket_booking_system import TicketBookingSystem

# Создание события
event = Event(1, "Concert")

# Добавление билетов
for i in range(1, 11):
    category = "VIP" if i <= 3 else "Standard"
    price = 200 if category == "VIP" else 100
    event.add_ticket(Ticket(i, seat=i, category=category, price=price))

# Создание системы бронирования
system = TicketBookingSystem(event)

# Пользователи
users = [
    User(1, "Alice", is_vip=True),
    User(2, "Bob"),
    User(3, "Charlie", is_vip=True),
    User(4, "David"),
    User(5, "Eve")
]

# Добавление пользователей
for user in users:
    system.add_user(user)

# Обработка бронирования
system.process_bookings()

# Вывод результатов
print("\n📊 Итоговое состояние билетов:")
for ticket in system.get_ticket_status():
    print(ticket)

# Пример отмены последнего бронирования
ticket, user = system.cancel_last_booking()
print(f"\n♻ Отмена последнего бронирования: {user.name} -> {ticket}")
