# Author Laurel Miller
# Date 10/10/2019
# 10/4/2019 added a number_to_word file
from Challenges.Challenge_4.number_to_word import num_to_word
import unittest

class fibonacci(unittest.TestCase):
    # The n in this function is how many iterations of the fib sequence will print out.

    def fib(self, n):
        a, b = 0, 1
        for i in range(0, n):
            print(a, '-', num_to_word(a))
            a, b = b, a + b
    def test_fib(self):
        self.fib(100)

if __name__ == '__main__':
    unittest.main()



