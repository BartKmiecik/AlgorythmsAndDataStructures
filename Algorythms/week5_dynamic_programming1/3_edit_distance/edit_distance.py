def edit_distance(first_string, second_string, i, j, grid):
    if not (i, j) in grid:
        if i == 0:
            grid[i, j] = j
        elif j == 0:
            grid[i, j] = i
        else:
            diff = 0 if first_string[i-1] == second_string[j-1] else 1
            insertion = edit_distance(first_string, second_string, i, j -1, grid)
            deletion = edit_distance(first_string, second_string, i - 1, j, grid)
            missmatch = edit_distance(first_string, second_string, i -1, j -1, grid)
            grid[i,j] = min(insertion, deletion, missmatch) + diff

    return grid[i,j]

if __name__ == "__main__":
    word1, word2 = input(), input()
    grid = dict()
    i = len(word1)
    j = len(word2)
    print(edit_distance(word1, word2, i, j, grid))
    print(grid)
