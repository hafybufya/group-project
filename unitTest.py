# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import unittest
from  mainCode import *
import os
from unittest.mock import patch
from pathlib import Path
import csv
# ---------------------------------------------------------------------
# Class of unit tests
# ---------------------------------------------------------------------

class my_unit_tests(unittest.TestCase):

    # ---------------------------------------------------------------------
    # File handling unit tests
    # ---------------------------------------------------------------------

    # Tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile(csv_in_use))

    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67