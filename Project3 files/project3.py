# project3.py
#
# ICS 33 Spring 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin


def main() -> None:
    """
    function that runs the whole program.
    called functions:
        getCode(): Takes user input and convert them into list of lines.
        parse(iterable): Takes iterables of lines and convert them to list of tokens, with each list representing a line.
        process(running): Takes running class object and execute statements parsed by previous functions.
    Handles runtimeError, printing reason for the error, then ending the program.
    """
    # Does not have any unittest due to the getCode() function. I do not know how to write unittest for code involving user input.
    # Although I could not write unittest, I tested it in python shell, and seemed to work fine.
    try:
        lines = grin.getCode()

        parsed = grin.parse(lines)

        grin.process(grin.running(parsed))
    except grin.runtimeError as e:
        print(f'runtimeError: {e.reason}')


if __name__ == '__main__':
    main()
