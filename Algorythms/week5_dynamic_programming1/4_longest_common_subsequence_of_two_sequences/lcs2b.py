def lcs2(first_sequence, second_sequence):
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0
    result = 0
    index = -1
    if first_sequence[0] in second_sequence:
        result += 1
        index = second_sequence.index(first_sequence[0])
    result += lcs2(first_sequence[1:], second_sequence[index + 1:])
    return result


def lcs2_full(first_sequence, second_sequence):
    total_result = 0
    for n in range(len(first_sequence)):
        result = lcs2(first_sequence[n:], second_sequence)
        if result > total_result:
            total_result = result

    return total_result


if __name__ == '__main__':
    GR = {0:0}
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2_full(a, b))
    # print(GR)