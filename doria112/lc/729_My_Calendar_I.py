from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.intervals = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        pos = self.intervals.bisect_right([start, end])
        # get the intervals right before and at the position 
        if pos > 0:
            prev = pos -1
            prev_end = self.intervals[prev][1]
            if prev_end > start:
                return False
        if pos < len(self.intervals):
            next_start = self.intervals[pos][0]
            if end > next_start:
                return False
        self.intervals.add([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
