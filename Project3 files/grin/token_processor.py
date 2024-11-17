from grin.run_class import running
from grin.token import *
from grin.base_object_class import runtimeError
from grin.int_grin_object import intGrinObj
from grin.float_grin_object import floatGrinObj
from grin.str_grin_object import strGrinObj

def process(run_class: running):
    """
    Initialize some attributes of running class object
    and process each line in its parsed_line attribute.
    """
    run_class.run = True
    check_labels(run_class)
    while run_class.run:
        if len(run_class.parsed_lines) == 0:
            run_class.run = False
        else:
            tokens = run_class.parsed_lines[run_class.current]
            if len(tokens) == 1:
                process_len_one(run_class, tokens)
            elif len(tokens) == 2:
                process_len_two(run_class, tokens)
            elif len(tokens) == 3:
                process_len_three(run_class, tokens)
            else: # len is 6
                process_len_six(run_class, tokens)

            if run_class.current >= run_class.length:
                run_class.run = False



def check_labels(run_class):
    """
    Modify labels attribute of running class object.
    Whenever a line in parsed_line has label, save
    {label's name: line number} into the label dictionary.
    """
    row = 0
    for line in run_class.parsed_lines:
        if len(line) >= 2:
            if line[1].text() == ':':
                run_class.labels[line[0].text()] = row
                del line[:2]
        row += 1

def process_len_one(run_class, tokens):
    """
    Process parsed line with only one token.
    Statements handled:
        END: end the program by setting run attribute of running class to False.
        RETURN: return to line number of last GOSUB statement and move one line afterward.
                if GOSUB statement was not made before, runtimeError is raised.
    runtimeError is raised if given statement of length 1 is not handled.
    """
    if tokens[0].text() == 'END':
        run_class.run = False
    else:  # RETURN
        if len(run_class.GOSUB_origin) == 0:
            raise runtimeError('Called RETURN without place to return.')
        else:
            run_class.current = run_class.GOSUB_origin[-1] + 1
            del run_class.GOSUB_origin[-1]

def process_len_two(run_class, tokens):
    """
    process parsed line with two tokens.
    Statements handles:
        PRINT: calls PRINT function.
        INNUM: calls INNUM function.
        INSTR: stores input value as strGrinObj and proceed one line.
        GOTO: calls GOTO function.
        GOSUB: calls GOSUB function.
    runtimeError is raised if given statement of length 2 is not handled.
    """
    command = tokens[0].text()
    if command == 'PRINT':
        PRINT(run_class, tokens)

    elif command == 'INNUM':
        # Could not write unittest, as it requires user input.
        # Tested it in python shell, and it seemed to work.
        INNUM(run_class, tokens)

    elif command == 'INSTR':
        # Could not write unittest, as it requires user input.
        # Tested it in python shell, and it seemed to work.
        run_class.vars[tokens[1].text()] = strGrinObj(input())
        run_class.current += 1

    elif command == 'GOTO':
        GOTO(run_class, tokens)

    else: # GOSUB
        GOSUB(run_class, tokens)


def process_len_three(run_class, tokens):
    """
    process parsed line with three tokens.
    Statements handles:
        LET: assign given value to given variable.
        ADD: add given value to the given variable's value, then update the variable's value.
        SUB: subtract given value to the given variable's value, then update the variable's value.
        MULT: multiply given value to the given variable's value, then update the variable's value.
        DIV: divide given value to the given variable's value, then update the variable's value.
    runtimeError is raised if given statement of length 3 is not handled.
    """
    command, var_name, value = InitLen3(run_class, tokens)

    if command == 'LET':
        run_class.vars[var_name] = value
    elif command == 'ADD':
        run_class.vars[var_name] = run_class.vars[var_name] + value
    elif command == 'SUB':
        run_class.vars[var_name] = run_class.vars[var_name] - value
    elif command == 'MULT':
        run_class.vars[var_name] = run_class.vars[var_name] * value
    else: # DIV
        run_class.vars[var_name] = run_class.vars[var_name] / value

    run_class.current += 1

def process_len_six(run_class, tokens):
    """
    process parsed line with six tokens.
    Statements handles:
        GOTO with conditional statement: if condition is met, calls GOTO function.
        GOSUB with conditional statement: if condition is met, calls GOSUB function.
    runtimeError is raised if given statement of length 3 is not handled.
    """
    command, result = InitLen6(run_class, tokens)
    if result:
        process_len_two(run_class, tokens)
    else:
        run_class.current += 1

def InitLen6(run_class, tokens):
    """
    initialize values and determine if condition is met for processing parsed line of length 6.
    Returns:
        command: statement to execute if condition is met.
        result: boolean value indicating if condition is met. True if met, False if not.
    runtimeError is raised if given operation is not valid.
    """
    command = tokens[0].text()
    val1 = InitValues(run_class, tokens, 3)
    val2 = InitValues(run_class, tokens, 5)
    op = tokens[4].text()
    if op == '<':
        result = val1 < val2
    elif op == '<=':
        result = val1 <= val2
    elif op == '>':
        result = val1 > val2
    elif op == '>=':
        result = val1 >= val2
    elif op == '=':
        result = val1 == val2
    else: # <>
        result = val1 != val2

    return command, result


def InitLen3(run_class, tokens):
    """
    initialize values and variables for processing parsed line of length 3.
    Returns:
        command: statement to execute.
        var_name: name of the given variable.
        value: grinObject of given value.
    """
    command = tokens[0].text()
    var_name = tokens[1].text()

    _ = InitValues(run_class, tokens, 1)

    value = InitValues(run_class, tokens, 2)

    return command, var_name, value


def InitValues(run_class, tokens, ind):
    """
    given a value, convert it into one of three derived class of grinObject class, and return it.
    Numerical values with . are converted to floatGrinObj.
    Numerical values with no . are converted to intGrinObj.
    All other values are converted to strGrinObj.
    """
    if tokens[ind].kind().category() == GrinTokenCategory.IDENTIFIER:
        if tokens[ind].text() not in run_class.vars.keys():
            run_class.vars[tokens[ind].text()] = intGrinObj(0)
        value = run_class.vars[tokens[ind].text()]
    else:
        try:
            if '.' in tokens[ind].text():
                value = floatGrinObj(tokens[ind].text())
            else:
                value = intGrinObj(tokens[ind].text())
        except ValueError:
            value = strGrinObj(tokens[ind].text())

    return value

def PRINT(run_class, tokens):
    """
    print given value to the standard output, then proceed to the next line.
    If literal value is given, print the value.
    If a variable is given, if the variable is defined, print its value.
    if the variable is not defined, define it as intGrinObj of value 0, then print its value.
    """
    out = tokens[1]
    if out.kind().category() == GrinTokenCategory.LITERAL_VALUE:
        val = out.text()
    else:
        if out.text() not in run_class.vars.keys():
            run_class.vars[out.text()] = intGrinObj(0)
        val = run_class.vars[out.text()].value

    if (("'" in str(val)) or ('"' in str(val))) and (len(str(val)) >= 2):
        print(str(val)[1:-1])
    else:
        print(str(val))

    run_class.current += 1

def INNUM(run_class, tokens):
    """
    take user input, and store it as the value of given variable.
    If input value has ., floatGrinObj is stored.
    if input value does not have ., intGrinObj is stored.
    runtimeError is raised if input value is not numeric.
    """
    # Could not write unittest, as it required user input.
    # Tested it python shell, and it seemed to work.
    given = input()
    try:
        _ = float(given)
    except ValueError:
        raise runtimeError('Input given is not number value.')
    if '.' in given:
        run_class.vars[tokens[1].text()] = floatGrinObj(given)
    else:
        run_class.vars[tokens[1].text()] = intGrinObj(given)
    run_class.current += 1

def GOSUB(run_class, tokens):
    """
    records where the GOSUB is called, then calls GOTO.
    """
    run_class.GOSUB_origin.append(run_class.current)
    GOTO(run_class, tokens)

def GOTO(run_class, tokens):
    """
    change current line to the given line.
    If given value is a variable:
        if variable has integer value, current line updates by the value.
        if variable has string value, search for label with the given name.
            if label is found, move to the label's line.
    If given value is a literal:
        if literal has integer value, current line updates by the value.
        if literal has string value, search for label with the given name.
            if label is found, move to the label's line.
    runtimeError is raised when:
        string value is given but label with such name is not found.
        destination line number is not valid.
    """
    done = False
    if tokens[1].kind().category() == GrinTokenCategory.IDENTIFIER:
        if tokens[1].text() not in run_class.vars.keys():
            run_class.vars[tokens[1].text()] = intGrinObj(0)
        jump = run_class.vars[tokens[1].text()].value
    else:
        jump = tokens[1].text()

    try:
        jump = int(jump)
    except ValueError:
        if jump[1:-1] not in run_class.labels.keys():
            raise runtimeError(f'Tried to go to nonexistent label of {jump[1:-1]}.')
        else:
            destination = run_class.labels[jump[1:-1]]
            if (destination == run_class.current) or (destination not in range(run_class.length)):
                raise runtimeError('Tried to go to inappropriate line number (To current line or line out of range).')
            run_class.current = destination
            done = True

    if not done:
        if (jump == 0) or (run_class.current + jump not in range(run_class.length)):
            raise runtimeError('Tried to go to inappropriate line number (To current line or line out of range).')
        else:
            run_class.current += jump