import unittest
import q1

class HW7Test(unittest.TestCase):
    def test_Count100(self):
        # test to ensure 100 lines are printed
        result = q1.run(100)
        self.assertEqual(result.count("\n"), 100)



if __name__ == "__main__":
    unittest.main()
