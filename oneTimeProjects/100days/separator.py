from datetime import datetime as dt


class DataSeparator:
    def __init__(self, data):
        workouts = ["Running", "Swimming", "Cycling", "Walking", "Pushups", "Jogging", "Yoga"]
        workouts_data = {
            workouts[0]: 11,
            workouts[1]: 6,
            workouts[2]: 6,
            workouts[3]: 4,
            workouts[4]: 4,
            workouts[5]: 9,
            workouts[6]: 3
        }
        now = dt.now()
        self.send_data = []
        a = data.title().split(" ")
        for i in a:
            if i in workouts:
                w_ind = workouts.index(i)
                minutes = a.index(i) + 1
                self.send_data.append(
                    [now.strftime("%X %d %b %Y"), i, a[minutes], int(a[minutes]) * workouts_data[workouts[w_ind]]])

    def sender(self):
        return self.send_data

