def lcs2(first_sequence, second_sequence, result):
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0
    # result = 0
    for n in range(len(first_sequence)):
        index = -1
        if first_sequence[n] in second_sequence:
            result += 1
            index = second_sequence.index(first_sequence[n])
        if n != len(first_sequence) - 1:
            lcs2(first_sequence[n+1:], second_sequence[index+1:], result)

    return result


def lcs2_full(first_sequence, second_sequence, grid):
    lcs2(first_sequence, second_sequence, grid)
    grid = sorted(grid.items(), reverse=True, key=lambda v: v[1])
    return grid[0][1]


if __name__ == '__main__':
    GR = {0:0}
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b, 0))
    # print(GR)