
day = 1
init_year = 1900
sunday_count = 0
# 1900/ 2 times Sunday
class Year:
    week_days = 7
    def Count31(self):
        if self.day == 0:
            self.count += 1
        self.day += 3
        self.day %= self.week_days

    def Count30(self):
        if self.day == 0:
            self.count += 1
        self.day += 2
        self.day %= self.week_days

    def Count29(self):
        if self.day == 0:
            self.count += 1
        self.day += 1
        self.day %= self.week_days

    def Count28(self):
        if self.leap_flag:
            if self.day == 0:
                self.count += 1
            self.day += 1
        else :
            if self.day == 0:
                self.count += 1
        self.day %= self.week_days

    def isleap(self,y):
        return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

    def __init__(self, year, day):
        self.leap_flag = self.isleap(year)
        self.count = 0
        self.day = day
        # count Sunday
        # Jan.
        self.Count31()
        # Feb.
        self.Count28()
        # MArch
        self.Count31()
        # April
        self.Count30()
        # May
        self.Count31()
        # June
        self.Count30()
        # July
        self.Count31()
        # Aug.
        self.Count31()
        # Sep.
        self.Count30()
        # Oct.
        self.Count31()
        # Nov.
        self.Count30()
        # Dec.
        self.Count31()

print "input year"
this_year = int(raw_input())

for i in xrange(init_year,this_year+1):
    temp = Year(i,day)
    sunday_count += temp.count
    day = temp.day

print sunday_count
