def getCode() -> list[str]:
    """
    take user input and convert them into list, with each line converted to a string.
    One line from user input is one element of the list.
    """
    # Does not have unittest, as I do not know how to write one for function involving user input.
    # Although I could not write unittest, I tested it in python shell, and seemed to work fine.
    reading = True
    lines = []

    while reading:
        line = input()

        if line == '.':
            reading = False

        lines.append(line)

    return lines