def lcs2(first_sequence, second_sequence,n, m, memo = {}):
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0
    # if first_sequence[0] == -6:
    #     print('asd')
    index = 0
    if first_sequence[0] in second_sequence:
        index = second_sequence.index(first_sequence[0])
    key = f'{n - len(first_sequence), index + m - len(second_sequence) }'
    if key in memo:
        return memo[key]
    result,res1 = 0, 0
    if first_sequence[0] in second_sequence:
        res1 = lcs2(first_sequence[1:], second_sequence[index + 1:], n, m) + 1
    res2 = lcs2(first_sequence[1:], second_sequence, n, m)
    result = max(res1, res2)
    memo[key] = result

    return result


def lcs2_full(first_sequence, second_sequence,n, m):
    total_result = 0
    for i in range(len(first_sequence)):
        result = lcs2(first_sequence[i:], second_sequence,n, m)
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

    print(lcs2_full(a, b, n, m))
    # print(GR)