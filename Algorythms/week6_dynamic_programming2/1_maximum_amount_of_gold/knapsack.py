import copy
from sys import stdin

def max_gold(capacity, weights:list, value = 0):
    rest_weights = copy.copy(weights)
    for n in weights:
        if n < capacity:
            rest = capacity - n
            rest_weights.remove(n)
            value += n
            return max_gold(rest, rest_weights, value)
    return value

def maximum_gold(capacity, weights):
    max_result = max_gold(capacity, weights)
    for i in weights:
        new_weights = copy.copy(weights)
        new_weights.remove(i)
        new_result = max_gold(capacity, new_weights)
        if new_result > max_result:
            max_result = new_result

    return max_result


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    # assert len(input_weights) == n
    input_weights = sorted(input_weights, reverse=True)
    print(maximum_gold(input_capacity, input_weights))
