import unittest
import os

# Checks if count of name and QR is equal
class TestQRGeneration(unittest.TestCase):
    def test_gen_qr(self):
        lst = os.listdir("./QRs/")
        qr_count = len(lst)

        with open("./data.csv") as csv_file:
            name_count = sum(1 for row in csv_file)

        self.assertEqual(qr_count, name_count)
