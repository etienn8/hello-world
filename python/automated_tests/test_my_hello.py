import unittest
import sys
sys.path.append('../')              #Add the path to the code to test

from my_hello import my_hello_class

class TestMyHello(unittest.TestCase):

    def test_adding_header_to_msg(self):
        self.assertEqual(my_hello_class().adding_header_to_msg('alloa'),"address: 0x0101;alloa")



if __name__ == '__main__':
    unittest.main()