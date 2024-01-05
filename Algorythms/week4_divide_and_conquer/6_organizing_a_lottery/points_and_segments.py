from sys import stdin


def points_cover_naive(starts, ends, points):
    print(f'Start {starts}, ends: {ends}')
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
    result = [0] * var
    i = 0

    for n in range(len(start)):
        if points[i] < start[n]:
            i += 1
        else:
            if points[i] < end[n]:
                result[i] += 1

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
