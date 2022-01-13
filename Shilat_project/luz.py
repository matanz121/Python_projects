days = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6,
}


class Datetime:
    def __init__(self, date_time):
        splitted_data_time = date_time.split(" ")
        str_day = splitted_data_time[0]
        print("str_day", str_day)
        self.day = days[str_day]
        str_time = splitted_data_time[1].split("-")
        self.start_hour = str_time[0].replace(":", "")
        self.end_hour = str_time[1].replace(":", "")


def solution(S):
    times = sort_meetings_times(S)
    times_diff = []
    for i in range(0, len(times) - 1):
        time_diff = int(times[i].end_hour) - int(times[i + 1].start_hour)
        times_diff.append(time_diff)
    max_time = max(times_diff)
    return max_time


def sort_meetings_times(S):
    times = []
    meetings_times = S.split("\n")
    for time in meetings_times:
        times.append(Datetime(time.strip()))
    times = sorted(times, key=lambda x: (x.day, x.start_hour), reverse=True)
    return times


def test_date_time():
    dt = Datetime("Sun 10:00-20:00")
    print(dt.day, dt.start_hour, dt.end_hour)
    t = """Sun 10:00-20:00
            Fri 05:00-10:00
            Fri 16:30-23:50
            Sat 10:00-24:00
            Sun 01:00-04:00
            Sat 02:00-06:00
            Tue 03:30-18:15
            Tue 19:00-20:00
            Wed 04:25-15:14
            Wed 15:14-22:40
            Thu 00:00-23:59
            Mon 05:00-13:00
            Mon 15:00-21:00"""
    print(solution(t))
