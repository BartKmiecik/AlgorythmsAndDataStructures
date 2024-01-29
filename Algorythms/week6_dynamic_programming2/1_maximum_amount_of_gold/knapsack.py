import copy
from sys import stdin


def table_counting(capacity: int, weights: list):
    weights.append(0)
    weights = sorted(weights)
    row, cols = capacity+1, len(weights)
    arr = [[0 for i in range(row)] for j in range(cols)]
    # print(arr)
    for i in range(cols):
        for j in range(row):
            # print(f'I:{i}, j:{j}, weight: {weights[i]}')
            temp = j-weights[i]
            var = 0 if temp < 0 else arr[i-1][temp] + weights[i]
            arr[i][j] = max(arr[i-1][j], var)
            # print(f'i:{i}, j:{j}, arr[i][j]: {arr[i][j]}')
    # print(arr)
    return arr[cols-1][row-1]

# def max_gold(capacity, weights:list, value = 0):
#     weights = sorted(weights, reverse=True)
#     rest_weights = copy.copy(weights)
#     for n in weights:
#         if n <= capacity:
#             rest = capacity - n
#             rest_weights.remove(n)
#             value += n
#             return max_gold(rest, rest_weights, value)
#     return value
#
#
# def maximum_gold(capacity, weights):
#     total_weights = sum(weights)
#     if total_weights < capacity:
#         return total_weights
#     diff = total_weights - capacity
#     if diff in weights:
#         return total_weights - diff
#
#     max_result = max_gold(capacity, weights)
#     for i in weights:
#         new_weights = copy.copy(weights)
#         new_weights.remove(i)
#         new_result = max_gold(capacity, new_weights)
#         if new_result > max_result:
#             max_result = new_result
#     return max_result
#

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    # assert len(input_weights) == n
    print(table_counting(input_capacity, input_weights))
