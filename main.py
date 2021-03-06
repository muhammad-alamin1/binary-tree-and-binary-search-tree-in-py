from tree import *

"""
         _2_
        /   \
       7     9
      / \     \
     1   6     8
        / \   / \
       5   10 3  4
"""


def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)

    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)

    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)

    eight = Node(8)
    nine.add_right(eight)

    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)

    # return the root node
    return two


if __name__ == '__main__':
    root = create_tree()
    print(root)
