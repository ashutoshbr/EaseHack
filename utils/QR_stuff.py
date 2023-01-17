import segno
import csv, os, shutil
from utils.transcoder import sign_data, f_pv, f_pb


def gen_qr():
    with open("./data.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Make QRs folder
        try:
            os.makedirs("QRs")
        except OSError:
            print("Old QRs directory was removed for the new one")
            shutil.rmtree("./QRs/")
            os.makedirs("QRs")

        # Save the keys
        with open(".env", "w+") as env_file:
            env_file.write(f"PV_KEY={f_pv}\nPB_KEY={f_pb}")

        # Iterate over each row and make QR
        for row in csv_reader:
            encoded_data = sign_data(row[0].encode("utf-8"))
            qrcode = segno.make_qr(encoded_data, error="H")

            # Save generated QR in the QRs folder
            qrcode.save(f"./QRs/{row[0]}" + ".png", scale=3)
