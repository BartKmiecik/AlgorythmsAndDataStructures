def lcs2(first_sequence, second_sequence, grid):
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0
    result = 0
    for n in range(len(first_sequence)):
        if first_sequence[n] in second_sequence:
            result += 1
            if not first_sequence[n] in grid:
                grid[first_sequence[n]] = 1
            else:
                index = second_sequence.index(first_sequence[n])
                next_res = lcs2(second_sequence[index:], first_sequence[n+1:], grid)
                grid[first_sequence[n]] = next_res + result
    return result


if __name__ == '__main__':
    grid = dict()
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b, grid))
