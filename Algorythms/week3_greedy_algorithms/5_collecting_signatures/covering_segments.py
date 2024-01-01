import copy
from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    cp_segments = copy.copy(segments)
    while len(cp_segments) > 0:
        shortes_end = 999999
        for s in cp_segments:
            if shortes_end > int(s.end):
                shortes_end = int(s.end)

        points.append(shortes_end)
        for s in reversed(range(len(cp_segments)+1)):
            # print(s)
            if s > 0 and shortes_end >= int(cp_segments[s-1].start):
                seg = cp_segments[s-1]
                # print(seg)
                cp_segments.remove(seg)
        #     pass
        # for s in segments:
        #     # print(s.start)
        #     if shortes_end >= int(s.start):
        #         # cp_segments.pop(s)
        #         pass
    # write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # print(segments)
    points = optimal_points(segments)
    print(len(points))
    print(*points)


# 3
# 1 3
# 2 5
# 3 6
