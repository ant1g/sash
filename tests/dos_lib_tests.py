import os
import unittest

import utils

def dos_lib(*args):
    dos_lib_path = os.path.join(utils.path_to_tests(), "dos_lib")
    cmd = (dos_lib_path,) + args

    return utils.run(cmd).decode("utf-8")

class DosLibTests(unittest.TestCase):
    def test_rand_str(self):
        str1 = dos_lib("rand_str")
        str2 = dos_lib("rand_str")
        self.assertEqual(33, len(str1))
        self.assertEqual(16, len(bytes.fromhex(str1)))
        self.assertNotEqual(str1, str2)
