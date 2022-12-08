from puzzle_8 import get_view_distance


def test_view_blocked_immediately_by_same_height_tree():
    current_tree = 4
    view = [4, 3, 2, 6]
    assert get_view_distance(current_tree, view) == 1


def test_view_blocked_after_a_while_by_same_height_tree():
    current_tree = 4
    view = [3, 3, 4, 2]
    assert get_view_distance(current_tree, view) == 3


def test_view_blocked_immediately_by_larger_tree():
    current_tree = 4
    view = [6, 3, 2, 6]
    assert get_view_distance(current_tree, view) == 1


def test_view_blocked_after_a_while_by_larger_tree():
    current_tree = 4
    view = [3, 3, 6, 2]
    assert get_view_distance(current_tree, view) == 3


def test_view_not_blocked():
    current_tree = 4
    view = [3, 3, 0, 2]
    assert get_view_distance(current_tree, view) == 4


if __name__ == '__main__':
    test_view_blocked_immediately_by_same_height_tree()
    test_view_blocked_after_a_while_by_same_height_tree()
    test_view_blocked_immediately_by_larger_tree()
    test_view_blocked_after_a_while_by_larger_tree()
    test_view_not_blocked()
