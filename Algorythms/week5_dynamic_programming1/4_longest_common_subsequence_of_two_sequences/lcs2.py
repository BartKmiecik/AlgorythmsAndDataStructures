def lcs2(first_sequence, second_sequence, grid, i , result):
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0

    for n in range(len(first_sequence)):
        if first_sequence[n] in second_sequence and i < first_sequence[n]:
            result =1
            index = second_sequence.index(first_sequence[n])
            result += lcs2(first_sequence[n+1:], second_sequence[index+1:], grid, n, result)
            grid[first_sequence[n]] = result

    # print(grid)
    grid = sorted(grid.items(), reverse=True, key=lambda v: v[1])
    # print(grid[0][0])
    return grid[0][0]


if __name__ == '__main__':
    grid = {0:0}
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b, grid, 0, 0))
