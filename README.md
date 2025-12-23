# Ticket-booking-system
Project description

A ticket booking system implemented in Python, with support for queues and user priorities.
The project demonstrates the practical application of data structures and algorithms, including: queues, priority queues, dynamic arrays, and sets.  

The system allows you to:
- Reserve tickets for VIP and regular users.
- Ensure priority for VIP users.
- Check ticket availability and prevent double bookings.
- Display the current status of tickets.
  
Project structure

ticket_booking_system/
├── main.py # Entry point, demonstration of operation
├── models/
│ ├── user.py # User class
│ ├── ticket.py # Ticket class
│ └── event.py # Event class
├── structures/
│ ├── simple_queue.py # Simple queue
│ └── priority_queue.py # Priority queue (Heap)
└── services/
└── booking_service.py # Ticket booking service

Data structures used

- **List (`list`)** — storage of event tickets (dynamic array).
- **Queue (`SimpleQueue`)** — processing of regular users (FIFO).  
- **Priority queue (`PriorityQueue`)** — processing VIP users (Min-Heap).
- **Set (`set`)** — storing reserved seats and quick search.

---

Algorithms

- **Linear search** — searching for a free ticket in an array.  
- **Greedy algorithm** — VIP users are served first.  
- **Heap** — implementation of a VIP priority queue.  
