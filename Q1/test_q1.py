import unittest
import q1

class HW7Test(unittest.TestCase):
    def test_Count100(self):
        # test to ensure 100 lines are printed
        result = q1.run(100)
        self.assertEqual(result, 100)
        
    def test_PrintFunc(self):
        # test PrintFunc on String input
        result = q1.PrintFunc("print")
        self.assertEqual(result, -1)

        # test PrintFunc on negative input
        result = q1.PrintFunc(-10)
        self.assertEqual(result, -1)

        # test PrintFunc on positive input
        result = q1.PrintFunc(2)
        self.assertEqual(result, 2)

        # test PrintFunc on an input multiplicable by 3
        result = q1.PrintFunc(3)
        self.assertEqual(result, "Fizz")

        # test PrintFunc on an input multiplicable by 5
        result = q1.PrintFunc(5)
        self.assertEqual(result, "Buzz")

        # test PrintFunc on an input multiplicable by 3 and 5
        result = q1.PrintFunc(3)
        self.assertEqual(result, "FizzBuzz")



if __name__ == "__main__":
    unittest.main()
