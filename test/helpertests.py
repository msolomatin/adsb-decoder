import sys
sys.path.append("../src")
import unittest
import helper

class HelperTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(helper.bin2int("0"), 0)
        self.assertEqual(helper.bin2int("1"), 1)
        self.assertEqual(helper.bin2int("1111"), 15)
        self.assertEqual(helper.bin2int("11110"), 30)

    def testTwo(self):
        self.assertEqual(helper.hex2bin("0"), "0000")
        self.assertEqual(helper.hex2bin("1"), "0001")
        self.assertEqual(helper.hex2bin("A"), "1010")
        self.assertEqual(helper.hex2bin("F"), "1111")

    def testThree(self):
        self.assertEqual(helper.bin2hex("0"), "0")
        self.assertEqual(helper.bin2hex("10"), "2")
        self.assertEqual(helper.bin2hex("1010"), "A")
        self.assertEqual(helper.bin2hex("1111"), "F")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
