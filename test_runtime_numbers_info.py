import numbers_info
import unittest
import os
from datetime import datetime


class RuntimeTest(unittest.TestCase):

    def testTimer(self):

        filename = 'temp_test.txt'

        for i in range(1, 11):
            a_list = [float(i) for i in range(1, 100000*i)]
            with open(filename, 'w') as f:
                for x in a_list:
                    f.write(str(x) + '\n')

            print(f'\n=======================================\n'
                  f'#{i}\n'
                  f'Output:\n'
                  f'----------------------------------------')

            st_time = datetime.now()
            numbers_info.body(filename)
            end_time = datetime.now() - st_time

            file_size = os.path.getsize('temp_test.txt')

            print(f'----------------------------------------\n'
                  f'\nRuntime: {end_time}'
                  f'\nFile size: {file_size} bytes')

        os.remove(filename)
        self.assertEqual(1, 1)
