f = {
    -2: 5,
    -1: 10,
    0: 15,
    1: 10,
    2: 10,
    3: 10,
    4: 10,
    5: 10,
    6: 10,
    7: 10,
    8: 10,
    9: 10,
    10: 10,
    11: 10,
    12: 10,
}


def sum_freq(start: int, end: int):
    total = 0
    for i in range(start, end + 1):
        total += f[i]
    return total


def sum_by_freq(start: int, end: int):
    total = 0
    for i in range(start, end + 1):
        total += (i * f[i])
    return total