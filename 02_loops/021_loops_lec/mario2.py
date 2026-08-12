def main():                                 ### Printing horizontal and vertical
    print_square(3)

def print_square(size):

    # for each row in sqare
    for i in range(size):

        # for each brick in row
        for j in range(size):

            # print brick
            print("#", end="")

        print()                             ### Print a new blank line

main()


"""
def main():                                     ### Print horizontal
    print_row(4)


def print_row(width):
    print("?" * width)

main()
"""