import unittest
import q2

class HW7Test(unittest.TestCase):
    def test_divisibleBy4(self):
        # test to see if integer input it divisible by 4
        results = q2.by4(8)
        self.assertEqual(results, True)

        results = q2.by4(5)
        self.assertEqual(results, False)

    def test_divisibleBy100(self):
        # test to see if integer input it divisible by 100
        results = q2.by100(100)
        self.assertEqual(results, True)

        results = q2.by100(110)
        self.assertEqual(results, False)

    def test_divisibleBy400(self):
        # test to see if integer input it divisible by 400
        results = q2.by400(400)
        self.assertEqual(results, True)

        results = q2.by400(410)
        self.assertEqual(results, False)

    def test_leapYear(self):
        # test to see if input is a leap year
        results = q2.leapYear(8)
        self.assertEqual(results, True)

        results = q2.leapYear(100)
        self.assertEqual(results, False)

        results = q2.leapYear(400)
        self.assertEqual(results, True)

        results = q2.leapYear(2000)
        self.assertEqual(results, True)

        
        

if __name__ == "__main__":
    unittest.main()
