import random
from random import randint


def partition3(array, left, right):
    pivot = array[left]
    i = left + 1
    for n in range(left+1,right+1):
        if array[n] < pivot:
            array[i], array[n] = array[n], array[i]
            i += 1
    array[left], array[i-1] = array[i-1], array[left]

    n = i - 1
    m = n
    # while m < len(array) - 10000 and array[n] == array[m + 10000]:
    #     m += 10000
    # while m < len(array) - 1000 and array[n] == array[m + 1000]:
    #     m += 1000
    # while m < len(array) - 100 and array[n] == array[m + 100]:
    #     m += 100
    # print(f'M<len: {m < len(array) - 10}, arrayn == arr[m+9]: {array[n] == array[m + 9]}')
    # while m < len(array) - 10 and array[n] == array[m + 10]:
    #     # print('AAAAAAAAAAAAAAAAAAAAAA')
    #     # print(f'10!! m: {m}, arr{array[m]}, m+10: {m+9}, arrM: {array[m+9]}, n: {n}, arrN: {array[n]}')
    #     m += 10
    while m < len(array) - 1 and array[n] == array[m + 1]:
        m += 1

    return n - 1, m + 1


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    n, m = partition3(array, left, right)

    randomized_quick_sort(array, left, n)
    randomized_quick_sort(array, m, right)
    # print(f'M:{m}, arraym: {array[m]} and m+: {m+1}, arraym+: {array[m+1]}')



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    # elements = []
    # for i in range(100000):
    #     elements.append(random.randint(0, 100000))
    assert len(elements) == input_n
    if len(elements) > 1:
        randomized_quick_sort(elements, 0, len(elements)-1)
        print(*elements)
    else:
        print(elements[0])
    # is_sorted = all(a <= b for a, b in zip(elements, elements[1:]))
    #
    # # print the result
    # if is_sorted:
    #     print("Yes, the list is sorted.")
    # else:
    #     print("No, the list is not sorted.")

    # flag = 0
    # i = 1
    # while i < len(elements):
    #     if (elements[i] < elements[i - 1]):
    #         flag = 1
    #         print(f'Not correct: {elements[i]} and elements: {elements[i - 1]}')
    #
    #     i += 1
    #
    # # printing result
    # if (not flag):
    #     print("Yes, List is sorted.")
    # else:
    #     print("No, List is not sorted.")

# 5
# 2 3 9 2 2