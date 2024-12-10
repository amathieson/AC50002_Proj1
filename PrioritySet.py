import heapq


# Based on Priority Set implementation by https://stackoverflow.com/a/5997409
class PrioritySet(object):
    def __init__(self):
        self.heap = []
        self.set = set()

    def add(self, d, pri):
        if d not in self.set:
            heapq.heappush(self.heap, (pri, d))
            self.set.add(d)

    def pop(self):
        if len(self.heap) > 0:
            pri, d = heapq.heappop(self.heap)
            self.set.remove(d)
            return pri, d
        return None, None

    def intersection(self, b):
        return self.set.intersection(b.set)

    def remove(self, d):
        self.set.remove(d)
        for i, e in enumerate(self.heap):
            if e[1] == d:
                self.heap.remove(e)
