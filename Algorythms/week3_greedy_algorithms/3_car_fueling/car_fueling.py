from sys import stdin


def min_refills(distance, tank, stops):
    stop_count = 0
    traveled = tank
    for i in range(len(stops)):
        if stops[i] < traveled and i < len(stops)-1:
            pass
        elif stops[i] == traveled:
            stop_count += 1
            traveled = stops[i] + tank
        elif i == len(stops)-1:
            stop_count += 1
            traveled = stops[i] + tank
        else:
            stop_count += 1
            traveled = stops[i-1] + tank
        # print(f'Station on {stops[i]}, max tank {traveled}')

    if traveled < distance:
        stop_count = -1

    # write your code here
    return stop_count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    # d = 200
    # m = 250
    # stops = [100, 150]
    print(min_refills(d, m, stops))


