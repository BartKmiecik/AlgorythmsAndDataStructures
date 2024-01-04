from random import randint


def partition3(array, left, right):
    pivot = array[left]
    # print(f'Left: {array[left]}')
    # print(array)
    i = left + 1
    for n in range(left+1,right+1):
        if array[n] < pivot:
            # print(f'N: {n} in array: {array[n]} less than: {pivot} i: {i} swapping: {array[i]}')
            array[i], array[n] = array[n], array[i]
            i += 1

    array[left], array[i-1] = array[i-1], array[left]

    # print(array)
    # print(f'i: {i} value {array[i]}')

    return i -1


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    # print(f'k: {array[k]}')
    array[left], array[k] = array[k], array[left]
    m1 = partition3(array, left, right)

    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m1 + 1, right)



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements)-1)
    print(*elements)


# 5
# 2 3 9 2 2