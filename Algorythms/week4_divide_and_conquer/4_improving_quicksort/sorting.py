from random import randint


def partition3(array, left, right):
    # print(array)
    i = 0
    j = 0
    for n in range(left+1, right):
        if array[left] > array[n]:
            j += 1
        else:
            i += 1
            temp = j + i
            array[temp], array[n] = array[n], array[temp]

    array[left], array[i] = array[i], array[left]
    left = i

    return left, right


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    # print(f'left: {array[left]}, k: {array[k]}')
    array[left], array[k] = array[k], array[left]
    # print(f'left: {array[left]}, k: {array[k]}')
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

#
# 5
# 2 3 9 2 2