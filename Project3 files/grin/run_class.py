class running:
    def __init__(self, parsed_lines):
        """
        A class of one running of the program.
        Parameter:
            parsed_lines: Iterable of lists that contain token objects.
        Attributes:
            current = integer representing current line - 1.
            GOSUB_origin = list containing all line numbers which called GOSUB and hasn't returned yet.
            vars = dictionary of all variables created, with variable name as keys and their value as values.
            parsed_lines = list version of input parsed_lines.
            length = Number of lines in the parsed_lines.
            run = boolean value indicating if the programming is running or not.
            labels = dictionary of all labels established, with label name as keys and line number as values.
        """
        # The module does not have an unittest as it does not have any methods defined.
        self.current = 0
        self.GOSUB_origin = []
        self.vars = {}
        self.parsed_lines = list(parsed_lines)
        self.length = len(self.parsed_lines)
        self.run = False
        self.labels = {}

