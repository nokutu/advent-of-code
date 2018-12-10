import datetime
import numpy as np

from functional import seq

events = []

with open('input.txt', 'r') as f:
    for line in f:
        date_str = line.strip().split(']')[0][1:]
        text = line.strip().split(']')[1].strip()

        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')

        events.append((date, text))

current_guard: int = None
data: np.ndarray = None
guards: [int] = []
minute_sleep = 0

for date, text in seq(events).order_by(lambda p: p[0]):
    print(date.day, date.minute, text)
    if 'Guard' in text:
        current_guard = int(text.split(' ')[1][1:])
        minute_sleep = 0
        guards.append(current_guard)

        if data is None:
            data = np.zeros((1, 60), np.bool)
        else:
            data = np.vstack([data, np.zeros(60, np.bool)])
    elif 'falls' in text:
        minute_sleep = date.minute
    elif 'wakes' in text:
        data[-1, minute_sleep:date.minute] = True

accum = dict()
for pos, guard in enumerate(guards):
    if guard not in accum:
        accum[guard] = 0

    accum[guard] += np.sum(data[pos, :])

most_sleep = seq(accum).map(lambda k: (k, accum[k])).max_by(lambda p: p[1])
print("Most asleep [id, minutes]:", most_sleep)

most_sleep_turns = seq(guards).enumerate(0).filter(lambda p: p[1] == most_sleep[0]).map(lambda p: p[0]).to_list()
most_sleep_minute = np.argmax(np.sum(data[most_sleep_turns, :], axis=0))

print("Most sleep minute:", most_sleep_minute)

print('Solution:', most_sleep_minute * most_sleep[0])
