from copy import deepcopy
from typing import List


def transpose(grid: List[List[str]]):
    # Grid can not have jagged rows.

    grid_length = len(grid)
    grid_width = len(grid[0])

    # Create empty grid of same size, but with length/width transposed
    output_grid = []
    for i in range(0, grid_width):
        output_grid.append([""] * grid_length)

    # Fill transposed grid
    for i in range(0, grid_length):
        for j in range(0, grid_width):
            output_grid[j][i] = grid[i][j].replace("[", "").replace("]", "")
    return output_grid


def reverse_and_clean_grid(grid: List[List[str]]):
    output_grid = []

    for stack in grid:
        stack.reverse()

        max_crate = len(stack)
        for crate in stack:
            if crate == "":
                max_crate = stack.index(crate)
                break
        output_grid.append(stack[:max_crate])

    return output_grid


def get_list_of_top_crates(datagrid):
    output = ""
    for stack in datagrid:
        top_crate = stack.pop()
        output += top_crate
    return output


def puzzle5():
    with open("input_5.txt", "r") as f:
        data = f.read().split("\n\n")
        warehouse = data[0].splitlines()
        crates = warehouse[:-1]
        stacks = int(max(warehouse[-1:][0].split("   ")))
        moves = data[1].splitlines()

    datagrid = []
    for row in crates:
        row_list = row.split("    ")
        new_row_list = []
        for crate in row_list:
            new_row_list += crate.split(" ")

        while len(new_row_list) < stacks:
            new_row_list += [""]

        datagrid.append(new_row_list)

    transposed_datagrid = transpose(datagrid)
    grid_part_1 = reverse_and_clean_grid(transposed_datagrid)
    grid_part_2 = deepcopy(grid_part_1)

    for move in moves:
        m = move.split(" ")
        number_of_moving_crates = int(m[1])
        from_stack = int(m[3]) - 1
        to_stack = int(m[5]) - 1

        for x in range(0, number_of_moving_crates):
            crate = grid_part_1[from_stack].pop()
            grid_part_1[to_stack].append(crate)

        while number_of_moving_crates:
            crate_number = len(grid_part_2[from_stack]) - number_of_moving_crates
            crate = grid_part_2[from_stack].pop(crate_number)
            grid_part_2[to_stack].append(crate)
            number_of_moving_crates -= 1

    part_1_output = get_list_of_top_crates(grid_part_1)
    part_2_output = get_list_of_top_crates(grid_part_2)

    print(f"Part 1 answer: {part_1_output}")
    print(f"Part 2 answer: {part_2_output}")


if __name__ == "__main__":
    puzzle5()
