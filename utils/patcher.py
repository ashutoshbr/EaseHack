from PIL import Image, ImageFont, ImageDraw
import csv

NAME_POS = (620, 470)
QR_POS = (745, 931)
NAME_COLOR = (77, 77, 77)


def gen_certificate():
    aspire_font = ImageFont.truetype("./assets/Aspire.ttf", 150)
    with open("./data.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            with Image.open("./assets/template.png") as template:
                on_template = ImageDraw.Draw(template)
                on_template.text(NAME_POS, row[0], NAME_COLOR, font=aspire_font)
                qr_img = Image.open(f"./QRs/{row[0]}.png")
                template.paste(qr_img, QR_POS)
                template.save(f"./Cert/{row[0]}.png")
