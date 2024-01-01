# def binary_search(keys, query):
#     result = -2
#     left = 0
#     right = len(keys)
#     while result == -2:
#         result, left, right = recursive_binary(left, right, keys, query)
#         # print(f'Res: {result}, left: {left}, right: {right}, bigger:{result > 0}')
#     # write your code here
#     return result
#
# def recursive_binary(left, right, keys, query):
#     result = -2
#     middle = int((left + right)/2)
#     print(middle)
#     if keys[middle] == query:
#         result = middle
#     if keys[middle] > query:
#         right = middle - 1
#     if keys[middle] < query:
#         left = middle + 1
#     if left >= right:
#         result = -1
#     return result, left, right
#
# if __name__ == '__main__':
#     num_keys = int(input())
#     input_keys = list(map(int, input().split()))
#     assert len(input_keys) == num_keys
#
#     num_queries = int(input())
#     input_queries = list(map(int, input().split()))
#     assert len(input_queries) == num_queries
#
#     for q in input_queries:
#         print(binary_search(input_keys, q), end=' ')

maxi = 2097151
next =  int(maxi / 2)

for n in range(21):
    print(next)
    next = int((maxi-next)/2+next)

# while next <= maxi:
#     print(next)
#     next = int((maxi-next)/2+next)