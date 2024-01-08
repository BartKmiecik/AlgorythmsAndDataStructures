def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def quick_sort(elements:list):
    if len(elements) > 1:
        mid = len(elements) // 2
        left = elements[:mid]
        right = elements[mid:]
        quick_sort(left)
        quick_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                elements[k] = left[i]
                i += 1
            else:
                elements[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            elements[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            elements[k] = right[j]
            j += 1
            k += 1

def majority_element(elements):
    quick_sort(elements)
    mid = len(elements) // 2
    if elements.count(elements[mid]) > len(elements) / 2:
        return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
