import grin
import unittest
import contextlib
import io

class testProcess(unittest.TestCase):
    def test_check_labels_no_label(self):
        p_line = grin.parse(["END", "."])
        run_class = grin.running(p_line)
        grin.token_processor.check_labels(run_class)
        self.assertEqual(run_class.labels, {})

    def test_check_labels_lenTwo_no_label(self):
        p_line = grin.parse(["LET A 1", "."])
        run_class = grin.running(p_line)
        grin.token_processor.check_labels(run_class)
        self.assertEqual(run_class.labels, {})

    def test_check_labels_label_exist(self):
        p_line = grin.parse(["HERE: LET A 1", "."])
        run_class = grin.running(p_line)
        grin.token_processor.check_labels(run_class)
        self.assertEqual(run_class.labels, {'HERE': 0})

    def test_len_one_END(self):
        p_line = grin.parse(["END", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_one(run_class, tokens)
        self.assertEqual(run_class.run, False)

    def test_len_one_RETURN_no_GOSUB(self):
        p_line = grin.parse(["RETURN", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.process_len_one(run_class, tokens)

    def test_len_one_RETURN_normal(self):
        p_line = grin.parse(["RETURN", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.GOSUB_origin.append(2)
        grin.token_processor.process_len_one(run_class, tokens)
        self.assertEqual(run_class.current, 3)

    def test_PRINT_literal(self):
        p_line = grin.parse(["PRINT 10", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.PRINT(run_class, tokens)
            self.assertEqual(output.getvalue(), '10\n')

    def test_PRINT_var_not_defined(self):
        p_line = grin.parse(["PRINT A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.PRINT(run_class, tokens)
            self.assertEqual(output.getvalue(), '0\n')

    def test_PRINT_var_int(self):
        p_line = grin.parse(["PRINT A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.intGrinObj(10)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.PRINT(run_class, tokens)
            self.assertEqual(output.getvalue(), '10\n')

    def test_PRINT_var_str(self):
        p_line = grin.parse(["PRINT A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.strGrinObj("'hi'")
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.PRINT(run_class, tokens)
            self.assertEqual(output.getvalue(), 'hi\n')

    def test_GOTO_var_undefined(self):
        p_line = grin.parse(["GOTO A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.GOTO(run_class, tokens)

    def test_GOTO_var_int_valid(self):
        p_line = grin.parse(["GOTO A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.intGrinObj(1)
        run_class.length = 5
        grin.token_processor.GOTO(run_class, tokens)
        self.assertEqual(run_class.current, 1)

    def test_GOTO_var_int_out_of_range(self):
        p_line = grin.parse(["GOTO A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.intGrinObj(3)
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.GOTO(run_class, tokens)

    def test_GOTO_literal_str_not_label(self):
        p_line = grin.parse(["GOTO \"hi\"", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.GOTO(run_class, tokens)

    def test_GOTO_literal_str_in_label_valid(self):
        p_line = grin.parse(["GOTO \"hi\"", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.labels['hi'] = 2
        run_class.length = 5
        grin.token_processor.GOTO(run_class, tokens)
        self.assertEqual(run_class.current, 2)

    def test_GOTO_literal_str_in_label_invalid(self):
        p_line = grin.parse(["GOTO \"hi\"", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.labels['hi'] = 2
        run_class.length = 1
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.GOTO(run_class, tokens)

    def test_GOSUB(self):
        p_line = grin.parse(["GOSUB 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.length = 3
        grin.token_processor.GOSUB(run_class, tokens)
        self.assertEqual(run_class.current, 1)

    def test_len_two_PRINT(self):
        p_line = grin.parse(["PRINT A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.intGrinObj(10)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.process_len_two(run_class, tokens)
            self.assertEqual(output.getvalue(), '10\n')

    def test_len_two_GOTO(self):
        p_line = grin.parse(["GOTO A", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.intGrinObj(1)
        run_class.length = 5
        grin.token_processor.process_len_two(run_class, tokens)
        self.assertEqual(run_class.current, 1)

    def test_len_two_GOSUB(self):
        p_line = grin.parse(["GOSUB 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.length = 3
        grin.token_processor.process_len_two(run_class, tokens)
        self.assertEqual(run_class.current, 1)

    def test_initValues_var_undefined(self):
        p_line = grin.parse(["ADD A B", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        a = grin.token_processor.InitValues(run_class, tokens, 1)
        self.assertEqual((run_class.vars, a), ({'A': grin.intGrinObj(0)}, grin.intGrinObj(0)))

    def test_initValues_var_defined(self):
        p_line = grin.parse(["ADD A B", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.vars['A'] = grin.intGrinObj(12)
        a = grin.token_processor.InitValues(run_class, tokens, 1)
        self.assertEqual((run_class.vars, a), ({'A': grin.intGrinObj(12)}, grin.intGrinObj(12)))

    def test_initValues_literal_int(self):
        p_line = grin.parse(["LET A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        a = grin.token_processor.InitValues(run_class, tokens, 2)
        self.assertEqual(a, grin.intGrinObj(12))

    def test_init_values_literal_float(self):
        p_line = grin.parse(["LET A 1.5", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        a = grin.token_processor.InitValues(run_class, tokens, 2)
        self.assertEqual(a, grin.floatGrinObj(1.5))

    def test_init_values_literal_str(self):
        p_line = grin.parse(["LET A \"hi\"", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        a = grin.token_processor.InitValues(run_class, tokens, 2)
        self.assertEqual(a, grin.strGrinObj("\"hi\""))

    def test_InitLen3(self):
        p_line = grin.parse(["LET A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, var_name, value = grin.token_processor.InitLen3(run_class, tokens)
        self.assertEqual((command, var_name, value), ('LET', 'A', grin.intGrinObj(12)))

    def test_process_len_three_LET(self):
        p_line = grin.parse(["LET A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_three(run_class, tokens)
        self.assertEqual(run_class.vars, {'A': grin.intGrinObj(12)})

    def test_process_len_three_ADD(self):
        p_line = grin.parse(["ADD A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_three(run_class, tokens)
        self.assertEqual(run_class.vars, {'A': grin.intGrinObj(12)})

    def test_process_len_three_SUB(self):
        p_line = grin.parse(["SUB A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_three(run_class, tokens)
        self.assertEqual(run_class.vars, {'A': grin.intGrinObj(-12)})

    def test_process_len_three_MULT(self):
        p_line = grin.parse(["MULT A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_three(run_class, tokens)
        self.assertEqual(run_class.vars, {'A': grin.intGrinObj(0)})

    def test_process_len_three_DIV(self):
        p_line = grin.parse(["DIV A 12", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_three(run_class, tokens)
        self.assertEqual(run_class.vars, {'A': grin.intGrinObj(0)})

    def test_InitLen6_lt(self):
        p_line = grin.parse(["GOTO 1 IF 1 < 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, result = grin.token_processor.InitLen6(run_class, tokens)
        self.assertEqual((command, result), ('GOTO', False))

    def test_InitLen6_le(self):
        p_line = grin.parse(["GOTO 1 IF 1 <= 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, result = grin.token_processor.InitLen6(run_class, tokens)
        self.assertEqual((command, result), ('GOTO', True))

    def test_InitLen6_gt(self):
        p_line = grin.parse(["GOTO 1 IF 1 > 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, result = grin.token_processor.InitLen6(run_class, tokens)
        self.assertEqual((command, result), ('GOTO', False))

    def test_InitLen6_ge(self):
        p_line = grin.parse(["GOTO 1 IF 1 >= 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, result = grin.token_processor.InitLen6(run_class, tokens)
        self.assertEqual((command, result), ('GOTO', True))

    def test_InitLen6_equal(self):
        p_line = grin.parse(["GOTO 1 IF 1 = 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, result = grin.token_processor.InitLen6(run_class, tokens)
        self.assertEqual((command, result), ('GOTO', True))

    def test_InitLen6_not_equal(self):
        p_line = grin.parse(["GOTO 1 IF 1 <> 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        command, result = grin.token_processor.InitLen6(run_class, tokens)
        self.assertEqual((command, result), ('GOTO', False))

    def test_process_len_six_false(self):
        p_line = grin.parse(["GOTO 1 IF 1 <> 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        grin.token_processor.process_len_six(run_class, tokens)
        self.assertEqual(run_class.current, 1)

    def test_process_len_six_true(self):
        p_line = grin.parse(["GOTO 3 IF 1 = 1", "."])
        run_class = grin.running(p_line)
        tokens = run_class.parsed_lines[0]
        run_class.length = 5
        grin.token_processor.process_len_six(run_class, tokens)
        self.assertEqual(run_class.current, 3)

    def test_process_only_DOT(self):
        p_line = grin.parse(["."])
        run_class = grin.running(p_line)
        grin.token_processor.process(run_class)
        self.assertEqual(run_class.run, False)

    def test_process_one(self):
        p_line = grin.parse(["RETURN", "."])
        run_class = grin.running(p_line)
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.process(run_class)

    def test_process_two(self):
        p_line = grin.parse(["PRINT 2", "."])
        run_class = grin.running(p_line)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.process(run_class)
            self.assertEqual(output.getvalue(), '2\n')

    def test_process_three(self):
        p_line = grin.parse(["LET A 12", "."])
        run_class = grin.running(p_line)
        grin.token_processor.process(run_class)
        self.assertEqual(run_class.vars, {'A': grin.intGrinObj(12)})

    def test_process_six(self):
        p_line = grin.parse(["GOTO 3 IF 1 = 1", "."])
        run_class = grin.running(p_line)
        with self.assertRaises(grin.runtimeError):
            grin.token_processor.process(run_class)

    def test_process_multiple_lines(self):
        p_line = grin.parse(["LET A 2", "PRINT A", "."])
        run_class = grin.running(p_line)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.token_processor.process(run_class)
            self.assertEqual(output.getvalue(), '2\n')

if __name__ == '__main__':
    unittest.main()