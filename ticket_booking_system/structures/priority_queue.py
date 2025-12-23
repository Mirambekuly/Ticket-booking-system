import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        # user_id используется как tiebreaker при одинаковом приоритете
        heapq.heappush(self.heap, (priority, item.user_id, item))

    def pop(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)[2]

    def is_empty(self):
        return len(self.heap) == 0

