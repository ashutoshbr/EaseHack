import unittest
from utils.transcoder import sign_data, verify_data


class TestEncodingDecoding(unittest.TestCase):
    def test_not_none(self):
        r = sign_data(b"Foo Bar")
        self.assertIsNotNone(r)

    def test_verify_data(self):
        r = verify_data(
            b"e8f11e4969f5cfaa0933d55bbda86f2c08b07bb20e343b540caeef2f1a0c27b3dc91299968dfb339226c97a8e57200f2600689c340fa4d305229163e1defd804466f6f20426172"
        )
        self.assertIsNotNone(r)


if __name__ == "__main__":
    unittest.main()
