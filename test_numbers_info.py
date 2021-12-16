import numbers_info
import math
import unittest
import random
import os

class CorrectionOfFunctions(unittest.TestCase):

    # Тесты корректности определения минимума, максимума, суммы и произведения функций

    def testMin(self):
        tst_arr = [float(i) * random.random() for i in range(-1000, 1000)]
        self.assertEqual(min(tst_arr), numbers_info.minimum(tst_arr))

    def testMax(self):
        tst_arr = [float(i) * random.random() for i in range(-1000, 1000)]
        self.assertEqual(max(tst_arr), numbers_info.maximum(tst_arr))

    def testSum(self):
        tst_arr = [float(i) * random.random() for i in range(1, 1000)]
        self.assertEqual(sum(tst_arr), numbers_info.addition(tst_arr))

    def testMult(self):
        tst_arr = [float(i) * random.random() for i in range(1, 1000)]
        self.assertEqual(math.prod(tst_arr), numbers_info.multiplication(tst_arr))


class testFailures(unittest.TestCase):

    # Тест на случай присутсвия в файле чего-то кроме чисел

    def testIfNotDigits(self):
        filename = 'temp_file.txt'
        with open(filename, 'w') as f:
            for i in ['a', 'b', 'c', '1']:
                f.write('i' + '\n')
        self.assertEqual(None, numbers_info.body(filename))

        os.remove(filename)
