import unittest
import sys
import datetime
import os
from scripts.main import required


class RequiredTestCase(unittest.TestCase):
    def test_required(self):
        parser, (options, arguments), rooms, info = required()
        self.assertNotIsInstance(
            rooms, basestring) and self.asserNotIsInstance(info, basestring)


if __name__ == '__main__':
    unittest.main()
