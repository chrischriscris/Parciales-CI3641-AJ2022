from tkinter.tix import Tree
import unittest
from random import randint
from tdiagram.Machine import Machine

class TestMachine(unittest.TestCase):
    def test_session(self):
        self.m = Machine()
        
        actions = [
            ('program', 'fib', 'LOCAL'),
            ('assert', 'fib', True),
            ('program', 'facto', 'Java'),
            ('assert', 'facto', False),
            ('interpreter', 'Java', 'C'),
            ('compiler', 'Java', 'C', 'C'),
            ('assert', 'facto', False),
            ('interpreter', 'C', 'LOCAL'),
            ('assert', 'facto', True),
            ('program', 'perapy', 'py'),
            ('interpretear', 'local', 'py'),
            ('assert', 'perapy', False),
            ('program', 'holaa', 'Python3'),
            ('compiler', 'Python3', 'LOCAL', 'wtf42'),
            ('assert', 'holaa', False),
            ('compiler', 'wtf42', 'Java', 'C'),
            ('assert', 'holaa', True),
        ]

        for el in actions:
            if el[0] == 'program':
                self.m.add_program(el[1], el[2])
            elif el[0] == 'interpreter':
                self.m.add_interpreter(el[1], el[2])
            elif el[0] == 'compiler':
                self.m.add_compiler(el[1], el[2], el[3])
            elif el[0] == 'assert':
                self.assertEqual(self.m.is_executable(el[1]), el[2])

class TestErrors(unittest.TestCase):
    def test_err1(self):
        self.m = Machine()
        self.assertRaises(ValueError, self.m.add_languages, 'hoal_py')
        self.assertRaises(ValueError, self.m.add_compiler, 'c++', 'jv_a', 'p_y')
        self.assertRaises(ValueError, self.m.add_interpreter, 'c-', 'h_o')

    def test_err2(self):
        self.m = Machine()
        self.assertRaises(ValueError, self.m.is_executable, 'QUÉ')