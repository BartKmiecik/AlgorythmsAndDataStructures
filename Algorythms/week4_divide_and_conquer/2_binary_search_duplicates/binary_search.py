def binary_search(keys, query):
    # write your code here
    result = -2
    left = 0
    right = len(keys)
    while result == -2:
        result = -2
        middle = int((left + right) / 2)
        if keys[middle] == query:
            while middle > 1000000 and keys[middle] == keys[middle-1000000]:
                middle -= 1000000
            while middle > 100000 and keys[middle] == keys[middle-100000]:
                middle -= 100000
            while middle > 10000 and keys[middle] == keys[middle-10000]:
                middle -= 10000
            while middle > 1000 and keys[middle] == keys[middle-1000]:
                middle -= 1000
            while middle > 100 and keys[middle] == keys[middle-100]:
                middle -= 100
            while middle > 10 and keys[middle] == keys[middle-10]:
                middle -= 10
            while middle > 5 and keys[middle] == keys[middle-5]:
                middle -= 5
            while middle > 0 and keys[middle] == keys[middle-1]:
                middle -= 1
            result = middle
        if keys[middle] > query:
            right = middle
        if keys[middle] < query:
            left = middle + 1
        if left >= right:
            result = -1
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
