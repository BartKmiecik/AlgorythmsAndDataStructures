import random


def longest_common_subsequence_lines(A, B):
    print('longest')
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    lcs = []

    i, j = m, n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs.insert(0, A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, lcs

# A = [2, 7, 5]
# B = [2, 5]

# A = [1, 2, 3, 4]
# B = [7]
#
# print(longest_common_subsequence_lines(A, B))

def generate_example():
    n = random.randint(0, 5)
    m = random.randint(0, 5)

    with open('generate.txt', 'w+') as d:
        # d.write('Test')
        d.write(f'{n}\n')
        for i in range(n):
            rand = random.randint(-10, 10)
            d.write(f'{rand} ')
        d.write(f'\n{m}\n')
        for i in range(m):
            rand = random.randint(-10, 10)
            d.write(f'{rand} ')

    # document.close()


# generate_example()

def lcs2(first_sequence, second_sequence, grid):
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return 0
    result = 0
    for n in range(len(first_sequence)):
        if first_sequence[n] in second_sequence:
            result = 1
            index = second_sequence.index(first_sequence[n])
            result += lcs2(first_sequence[n+1:], second_sequence[index+1:], grid)
            if not first_sequence[n] in grid:
                grid[first_sequence[n]] = result
            else:
                var = grid[first_sequence[n]]
                grid[first_sequence[n]] = max(result, var)

    # print(grid)

    # print(grid[0][0])
    return result

def lcs2_full(first_sequence, second_sequence, grid ):
    lcs2(first_sequence, second_sequence, grid)
    grid = sorted(grid.items(), reverse=True, key=lambda v: v[1])
    return grid[0][1]

result = True
# generate_example()

while result:
    generate_example()
    with open('generate.txt', 'r') as d:
        grid = {0: 0}
        n = d.readline().strip()
        arrN = d.readline().split()
        assert len(arrN) == int(n)
        m = d.readline().strip()
        arrM = d.readline().split()
        assert len(arrM) == int(m)
        lc2 = lcs2_full(arrN, arrM, grid)
        lc2a = longest_common_subsequence_lines(arrN, arrM)
        result = lc2 == lc2a[0]
        print(f'First {lc2}, second {lc2a} equal {result}')


