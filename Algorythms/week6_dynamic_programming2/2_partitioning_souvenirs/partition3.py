import copy
from sys import stdin



def check_possibilities(values, goal):
    new_values = copy.copy(values)
    current = 0
    for i in values:
        if current + i <= goal:
            new_values.remove(i)
            current += i
        if current == goal:
            stage2_values = new_values
            for j in stage2_values:
                if current + j <= goal * 2:
                    new_values.remove(j)
                    current += j
                if current == goal * 2:
                    return True
    for i in range(1,len(values)-1):
        new_values = copy.copy(values)
        current = 0
        new_values.remove(values[i-1])
        if current + values[i] <= goal:
            new_values.remove(values[i])
            current += values[i]
        if current == goal:
            stage2_values = new_values
            for j in stage2_values:
                if current + j <= goal * 2:
                    new_values.remove(j)
                    current += j
                if current == goal * 2:
                    return True

    return False


def partition3(values:list):
    total_sum = sum(values)
    third_of_sum = total_sum // 3
    var = all(i > third_of_sum for i in values)
    if len(values) < 3 or total_sum % 3 != 0 or all(i > third_of_sum for i in values):
        return 0
    values = sorted(values, reverse=True)
    new_poss = check_possibilities(values, third_of_sum)
    result = 1 if new_poss else 0
    return result


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
