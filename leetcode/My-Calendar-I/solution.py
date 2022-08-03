class MyCalendar:

    def __init__(self):
        self.book_list = []

    def book(self, start: int, end: int) -> bool:
        if len(self.book_list) == 0:
            self.book_list.append([start,end])
            return True
        else:
            flag = True
            for book in self.book_list:
                if book[0] <= start and start < book[1]:
                    flag = False
                    break
                if book[0] < end and end <= book[1]:
                    flag = False
                    break
                if start <= book[0] and book[0] < end:
                    flag = False
                    break
                if start < book[1] and book[1] < end:
                    flag = False
                    break
            if flag:
                self.book_list.append([start, end])
            
            self.book_list = sorted(self.book_list)
            
            return flag

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)