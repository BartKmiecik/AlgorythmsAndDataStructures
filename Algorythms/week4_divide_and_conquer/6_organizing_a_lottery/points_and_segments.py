from sys import stdin


def points_cover_naive(starts, ends, points):
    # print(f'Start {starts}, ends: {ends}')
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

def merge_sort(start, end):
    if len(start) > 1:
        mid = int(len(start) / 2)
        l = start[:mid]
        l2 = end[:mid]
        r = start[mid:]
        r2 = end[mid:]

        merge_sort(l, l2)
        merge_sort(r, r2)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                start[k] = l[i]
                end[k] = l2[i]
                i += 1
            else:
                start[k] = r[j]
                end[k] = r2[j]
                j += 1
            k += 1

        while i < len(l):
            start[k] = l[i]
            end[k] = l2[i]
            k += 1
            i += 1

        while j < len(r):
            start[k] = r[j]
            end[k] = r2[j]
            k += 1
            j += 1


def points(start, end, points):
    var = len(points)
    temp = {}
    for n in points:
        temp[n] = 0

    # print(f'Temp {temp}')
    i = 0
    j = 0
    # print(points)
    points.sort()
    # print(points)

    while j < len(points):
        # print(f'i: {i}, j: {j}')
        if points[j] < start[i]:
            j += 1
        else:
            if points[j] < end[i]:
                # print(f'Should increase, {points[j]}, and value: {temp[points[j]]}')
                temp[points[j]] += 1
            i += 1
        if i >= len(start):
            break


    # for n in range(len(points)):
    #     print(f'n: {n}, points: {points[n]}, i: {i}, start: {start[i]}, end: {end[i]}')
    #     if points[n] < start[i]:
    #         n += 1
    #     else:
    #         if points[n] < end[i]:
    #             print(f'Should increase, {points[n]}, and value: {temp[points[n]]}')
    #             temp[points[n]] += 1
    #             i += 1
    #     if i >= len(start):
    #         break


    #
    # for n in range(len(start)):
    #     print(f'i: {i}, points: {points[i]}, n: {n}, start: {start[n]}')
    #     print(points[i] < start[n])
    #     print(f'i: {i}, points: {points[i]}, n: {n}, end: {end[n]}, point<end: {points[i] < end[n]}')
    #     if points[i] < start[n]:
    #         i += 1
    #     else:
    #         if points[i] < end[n]:
    #             print('Should increase')
    #             temp[points[i]] += 1

    result = [0] * len(points)
    i = 0
    for _, value in temp.items():
        result[i] = value
        i += 1

    return result


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    # print(f'Start: {input_starts}, end: {input_ends}')
    merge_sort(input_starts, input_ends)
    # print(f'Start: {input_starts}, end: {input_ends}')

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
