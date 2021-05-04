import os
import unittest

import utils

def sash_lib(*args):
    sash_lib_path = os.path.join(utils.path_to_tests(), "sash_lib")
    cmd = (sash_lib_path,) + args

    return utils.run(cmd).decode("utf-8")

class SashLibTests(unittest.TestCase):
    def test_rand_str(self):
        str1 = sash_lib("rand_str")
        str2 = sash_lib("rand_str")

        self.assertEqual(17, len(str1))
        self.assertEqual(8, len(bytes.fromhex(str1)))
        self.assertNotEqual(str1, str2)
