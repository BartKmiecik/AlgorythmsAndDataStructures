from itertools import combinations


def merge(arr, temp, left, mid, right):
    i = left
    k = left
    j = mid + 1
    num_of_inversions = 0

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            num_of_inversions += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    return num_of_inversions


def merge_sort(arr, temp, left, right) -> int:
    num_of_inversions = 0

    if left < right:
        mid = int((left + right)/2)

        num_of_inversions += merge_sort(arr, temp, left, mid)

        num_of_inversions += merge_sort(arr, temp, mid + 1, right)

        num_of_inversions += merge(arr, temp, left, mid, right)

    return num_of_inversions


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def inversion(a):
    n = len(a)
    temp_array = [0] * n
    return merge_sort(a, temp_array, 0, n-1)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversion(elements))
