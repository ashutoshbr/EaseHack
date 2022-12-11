import segno
import csv, os

with open("./data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # Make QRs folder
    try:
        os.makedirs("QRs")
    except OSError:
        print("Directory named QRs already exists")

    # Iterate over each row and make QR
    for row in csv_reader:
        qrcode = segno.make_qr(row[0], error="H")

        # Save generated QR in the QRs folder
        qrcode.save(f"./QRs/{row[0]}" + ".png", scale=3)
