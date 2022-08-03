# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        print("---")
        print(start, end)
        print(self.schedule)
        for s in self.schedule:
            if (s[0] <= start < s[1]) or (s[0] < end <= s[1]) or (start < s[0] and s[1] <= end):
                return False
        
        self.schedule.append([start, end])
        

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

schedule = ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
date = [[],[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]

cal = MyCalendar()
ans = []
for i in range(1, len(date)):
    ans.append(cal.book(date[i][0], date[i][1]))

print(ans)
