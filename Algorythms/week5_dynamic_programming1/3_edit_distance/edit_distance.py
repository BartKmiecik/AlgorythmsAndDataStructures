def edit_distance_recursive(first_string, second_string, i, j, grid):
    # print(f'I: {i}, J: {j}')
    if not (i, j) in grid:
        if i == 0:
            grid[i, j] = j
        elif j == 0:
            grid[i, j] = i
        else:
            diff = 0 if first_string[i-1] == second_string[j-1] else 1
            insertion = edit_distance_recursive(first_string, second_string, i, j -1, grid)
            deletion = edit_distance_recursive(first_string, second_string, i - 1, j, grid)
            missmatch = edit_distance_recursive(first_string, second_string, i -1, j -1, grid)
            grid[i,j] = min(insertion, deletion, missmatch) + diff


    return grid[i,j]

def edit_distance_iterative(first, second):
    arr2d = [[float("inf")] * (len(second) + 1) for _ in range(len(first)+1)]
    for i in range(len(first)+1):
        arr2d[i][0] = i
    for j in range(len(second)+1):
        arr2d[0][j] = j

    for i in range(1,len(first)+1):
        for j in range(1,len(second)+1):
            # print(f'Comparing: {first[i-1]} and {second[j-1]}')
            diff = 0 if first[i-1] == second[j-1] else 1
            arr2d[i][j] = min(arr2d[i-1][j] + 1, arr2d[i][j-1] + 1, arr2d[i-1][j-1] + diff)

    # print(arr2d)
    return arr2d[len(first)][len(second)]


if __name__ == "__main__":
    word1, word2 = input(), input()
    grid = dict()
    i = len(word1)
    j = len(word2)
    # result = edit_distance_recursive(word1, word2, i, j, grid)
    result = edit_distance_iterative(first=word1, second=word2)
    # diff = abs(i - j)
    # if result < diff:
    #     result = diff
    print(result)
    # print(grid)
