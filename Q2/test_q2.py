import unittest
import q2

class HW7Test(unittest.TestCase):
    def test_divisibleBy4(self):
        # test to see if integer input it divisible by 4
        results = q2.by4(8)
        self.assertEqual(results, true)

        results = q2.by4(5)
        self.assertEqual(results, false)
        
        

if __name__ == "__main__":
    unittest.main()