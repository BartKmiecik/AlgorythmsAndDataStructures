from itertools import combinations

def merge_sort(arr, num_of_inversion) -> int:

    if len(arr) > 1:
        # print(arr)
        mid = int(len(arr)/2)

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, num_of_inversion)
        merge_sort(right, num_of_inversion)

        g = i = j = k = 0

        while i < len(left) and j < len(right):
            # print(f'i: {i}, mid: {mid}, j: {j}, end: {len(arr)-1}, J<end: {j < len(right)}')
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                g = len(left) + j - i
                num_of_inversion += g
                # print(f'G: {g}, i: {i}, left[i]: {left[i]}, j: {j-1}, right[j]: {right[j-1]}')
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    # print(arr)
    return num_of_inversion


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def inversion(a):
    return merge_sort(a, 0)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversion(elements))
