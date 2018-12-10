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
        accum[guard] = np.zeros(60, np.int)

    accum[guard] += data[pos, :]

max_guard = None
max_minute = None
max_val = 0

for guard in accum:
    minute = np.argmax(accum[guard])
    val = accum[guard][minute]

    if val >= max_val:
        max_val = val
        max_minute = minute
        max_guard = guard


print('Solution:', max_minute * max_guard)
