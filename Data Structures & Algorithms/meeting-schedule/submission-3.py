"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)

        # for i in range(intervals):
        #     intervals2.append(intervals[i].start)

        i = 0
        

        print(intervals)

        while i <= len(intervals) - 1:
            print("hi")
            j = i+1
            while j <= len(intervals) - 1:
                print("in i ", intervals[i].end)
                print("in j ", intervals[j].start)
                if intervals[i].end > intervals[j].start:
                    return False
                j+=1
            i+=1

        return True

