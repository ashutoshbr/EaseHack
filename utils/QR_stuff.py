import segno
import csv, os
from utils.transcoder import sign_data

with open("./data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # Make QRs folder
    try:
        os.makedirs("QRs")
    except OSError:
        print("Directory named QRs already exists")

    # Iterate over each row and make QR
    for row in csv_reader:
        encoded_data = sign_data(row[0].encode("ascii"))
        qrcode = segno.make_qr(encoded_data, error="H")

        # Save generated QR in the QRs folder
        qrcode.save(f"./QRs/{row[0]}" + ".png", scale=3)
