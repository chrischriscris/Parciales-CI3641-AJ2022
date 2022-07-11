import unittest
from boolev.BooleanEvaluator import BooleanEvaluator

class TestEvaluator(unittest.TestCase):
    def test_expressions_eval(self):
        self.assertEqual(BooleanEvaluator().evaluate('& true false', True), 'false')
        self.assertEqual(BooleanEvaluator().evaluate('| & => true true false true', True), 'true')
        self.assertEqual(BooleanEvaluator().evaluate(' true false => false | true false ^ | &', False), 'false')
        self.assertEqual(BooleanEvaluator().evaluate(' ^ => true false ', True), 'true')
        self.assertEqual(BooleanEvaluator().evaluate(' => ^ true false ', True), 'true')
        self.assertEqual(BooleanEvaluator().evaluate(' true false => ^ ', False), 'true')
        self.assertEqual(BooleanEvaluator().evaluate(' true false ^ => ', False), 'true')

    def test_expressions_show(self):
        self.assertEqual(BooleanEvaluator().show('& true false', True), 'true & false')
        self.assertEqual(BooleanEvaluator().show('| & => true true false true', True), '(true => true) & false | true')
        self.assertEqual(BooleanEvaluator().show(' true false => false | true false ^ | &', False), '(true => false) | false & (true | ^ false)')
        self.assertEqual(BooleanEvaluator().show(' ^ => true false ', True), '^ (true => false)')
        self.assertEqual(BooleanEvaluator().show(' => ^ true false ', True), '^ true => false')
        self.assertEqual(BooleanEvaluator().show(' => ^ true false ', True), '^ true => false')
        self.assertEqual(BooleanEvaluator().show(' true false => ^ ', False), '^ (true => false)')
        self.assertEqual(BooleanEvaluator().show(' true false ^ => ', False), 'true => ^ false')

    def test_expressions_to_posfix(self):
        self.assertEqual(BooleanEvaluator().to_posfix('& true false'), 'true false &')
        self.assertEqual(BooleanEvaluator().to_posfix('& | => true false false | true ^ false'), 'true false => false | true false ^ | &')

class TestErrors(unittest.TestCase):
    def test_err1(self):
        self.bev = BooleanEvaluator()
        self.assertRaises(Exception, self.bev.parse, '=> hola false', True)
        self.assertRaises(Exception, self.bev.parse, 'false true =>', True)
        self.assertRaises(Exception, self.bev.parse, '^ false', False)

if __name__ == '__main__':
    unittest.main()