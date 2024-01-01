from sys import stdin


def min_refills(distance, tank, stops):
    stop_count = 0
    max_distance = tank
    counter = 0
    while max_distance < distance:
        # print(stop_count)
        if counter == len(stops)-1:
            if stops[-1] <= max_distance:
                max_distance += stops[-1]
                stop_count +=1
                if max_distance > distance:
                    break
            stop_count = -1
            break
        if stops[counter] <= max_distance:
            counter += 1
        else:
            max_distance = stops[counter-1] + tank
            stop_count += 1
    # write your code here
    return stop_count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    # d = 200
    # m = 250
    # stops = [100, 150]
    print(min_refills(d, m, stops))


