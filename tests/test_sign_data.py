import unittest
from utils.transcoder import sign_data


class TestSignData(unittest.TestCase):
    def test_not_none(self):
        r = sign_data(b"Foo Bar")
        return self.assertIsNotNone(r)
