from cs50 import get_int


def main():
    # Checks whether a number between 1 and 8 was entered
    while True:
        height = get_int("Height: ")
        if height < 9 and height > 0:
            break
    spaces = height - 1
    hashes = 1

    # Defines the lines of the pyramids
    for i in range(height):
        # Print the spaces
        espacos(spaces)
        # Print the hashes
        asterisco(hashes)

        print("  ", end="")

        # Print the hashes
        asterisco(hashes)
        print("")
        spaces = spaces - 1
        hashes = hashes + 1


# Print the spaces
def espacos(quantidade):
    for i in range(quantidade):
        print(" ", end="")


# Print the hashes
def asterisco(quantidade):
    for i in range(quantidade):
        print("#", end="")


main()
