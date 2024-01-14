import math
import random
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    print(f'F1: {first_point}, f2: {second_point}')
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def partitione(array ,left, right, axis):
    if axis == 'x':
        pivot = array[left].x
    else:
        pivot = array[left].y
    i = left + 1
    for n in range(left+1, right+1):
        if axis == x:
            if pivot > array[n].x:
                array[n], array[i] = array[i], array[n]
                i += 1
        else:
            if pivot > array[n].y:
                array[n], array[i] = array[i], array[n]
    array[left], array[i-1] = array[i-1], array[left]
    return i-1

def quick_sort(array, left, right, axis):
    if left < right:
        k = random.randint(left, right)
        array[k], array[left] = array[left], array[k]
        m = partitione(array, left, right, axis)
        quick_sort(array, left, m, axis)
        quick_sort(array, m+1, right, axis)


def brute_force(points):
    min_distance = 99999999
    for i in range(len(points)-1):
        distance = math.sqrt((points[i].x - points[i+1].x) ** 2 + (points[i].y - points[i+1].y) ** 2)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def dist(A, B):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)

def strip_closest(points: list, mid_dist):
    quick_sort(points, 0, len(points)-1, 'y')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (points[j].y - points[i].y) >= mid_dist:
                break
            disty = dist(points[i], points[j])
            if disty < mid_dist:
                mid_dist = disty
    return mid_dist

def minimum_distance_squared(points: list):
    if len(points) <= 1:
        return 0
    if len(points) <= 3:
        return brute_force(points)
    mid = len(points)//2
    d1 = minimum_distance_squared(points[:mid])
    d2 = minimum_distance_squared(points[mid:])
    d = min(d1, d2)

    strip = []
    for i in range(len(points)):
        if abs(points[i].x - points[mid].x) < d:
            strip.append(points[i])

    s = strip_closest(strip, d)

    return min(s, d)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # print(input_points[0].x)

    # print(quick_sort(input_points, 0, len(input_points)-1, 'x'))
    # print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    print("{0:.9f}".format(minimum_distance_squared(input_points)))
