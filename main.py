from rich.console import Console
from rich.table import Table
from utils.transcoder import f_pv, f_pb
from utils.qr_stuff import gen_qr
from utils.transcoder import verify_data
from utils.patcher import gen_certificate

console = Console()
table = Table(expand=True, style="green", highlight=True, show_edge=False)

table.add_column("Welcome to EaseHack", justify="center", no_wrap=True)

console.print(table)
console.print("Press 1 to generate keys", style="green")
console.print("Press 2 to save keys in .env file", style="green")
console.print("Press 3 to use data.csv to generate QRs", style="green")
console.print("Press 4 to verify", style="green")
console.print("Press 5 to generate Certificates with QR", style="green")
console.print("Press 0 to exit.", style="green")


while True:
    user_input = int(input("Enter your choice: "))
    match user_input:
        case 1:
            print(f"PV_KEY={f_pv}")
            print(f"PB_KEY={f_pb}")
        case 2:
            with open(".env", "w+") as env_file:
                env_file.write(f"PV_KEY={f_pv}\nPB_KEY={f_pb}")
        case 3:
            console.print(
                "Warning!!! Your previous keys have been overwritten", style="red"
            )
            gen_qr()
        case 4:
            encoded_data = input("Encoded data = ")
            verified = verify_data(bytes(encoded_data, encoding="utf-8"))
            console.print(verified, style="green bold")
        case 5:
            gen_certificate()
            console.print(
                "Please find the generated certificates in Cert folder", style="italic"
            )
        case 0:
            exit()
