def transpose_grid(grid):

    grid_length = len(grid)
    grid_width = len(grid[0])
    transposed_grid = []
    for i in range(0, grid_width):
        transposed_grid.append([0] * grid_length)

    for i in range(len(grid)):
        for j in range(len(grid)):
            transposed_grid[i][j] = grid[j][i]
    return transposed_grid


def get_view_distance(start_height, view):
    index = 0
    for index in range(len(view)):
        if view[index] >= start_height:
            break

    # Last tree also counts
    return index + 1


def puzzle8():
    with open("input_8.txt", "r") as f:
        data = f.read().splitlines()
        forest = []
        for line in data:
            forest.append([int(x) for x in line])
    transposed_forest = transpose_grid(forest)

    # All border trees minus 4 duplicate corner trees
    visible_trees = 2*len(forest[0]) + 2*len(transposed_forest[0]) - 4
    max_scenic_score = 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[i]) - 1):
            current_tree = forest[i][j]

            view_right = forest[i][j + 1:]
            view_left = forest[i][:j]
            view_down = transposed_forest[j][i + 1:]
            view_up = transposed_forest[j][:i]

            # Below is for part 1
            if min(max(view_right), max(view_left), max(view_down), max(view_up)) < current_tree:
                visible_trees += 1

            # Below is for part 2
            score_right = get_view_distance(current_tree, view_right)
            score_left = get_view_distance(current_tree, view_left[::-1])
            score_down = get_view_distance(current_tree, view_down)
            score_up = get_view_distance(current_tree, view_up[::-1])

            scenic_score = score_right * score_left * score_down * score_up
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(f"Part 1 answer: {visible_trees}")
    print(f"Part 2 answer: {max_scenic_score}")


if __name__ == "__main__":
    puzzle8()
