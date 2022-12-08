class Folder:
    def __init__(self, parent_folder):
        self.parent_folder = parent_folder
        self.child_folder_list = []
        self.folder_size = 0

    def append_dir(self, folder):
        self.child_folder_list.append(folder)

    def add_size(self, size):
        self.folder_size += size
        if self.parent_folder:
            self.parent_folder.add_size(int(size))


def get_total_size_less_than_100000(folder: Folder):
    total_size = 0
    for child_folder in folder.child_folder_list:
        if child_folder.folder_size <= 100000:
            total_size += child_folder.folder_size
        total_size += get_total_size_less_than_100000(child_folder)
    return total_size


def get_min_folder_size(folder: Folder, min_space, max_space):
    if min_space < folder.folder_size < max_space:
        max_space = folder.folder_size
    for child_folder in folder.child_folder_list:
        new_max_space = get_min_folder_size(child_folder, min_space, max_space)
        if min_space < new_max_space < max_space:
            max_space = new_max_space
    return max_space


def puzzle7():
    with open("input_7.txt", "r") as f:
        data = f.read().splitlines()

    root = Folder(parent_folder=None)
    current_folder = root
    for line in data:
        if line == "$ cd ..":
            current_folder = current_folder.parent_folder
        elif line[0].isnumeric():
            file_size = line.split(" ")[0]
            current_folder.add_size(int(file_size))
        elif line[0:4] == "$ cd":
            new_folder = Folder(parent_folder=current_folder)
            current_folder.append_dir(new_folder)
            current_folder = new_folder

    max_space = 70000000
    used_space = root.folder_size
    free_space = max_space - used_space
    needed_space = 30000000
    space_to_free_up = needed_space - free_space
    
    print(f"Part 1 answer: {get_total_size_less_than_100000(root)}")
    print(f"Part 2 answer: {get_min_folder_size(root, space_to_free_up, max_space)}")


if __name__ == "__main__":
    puzzle7()
