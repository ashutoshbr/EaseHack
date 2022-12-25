from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from dotenv import load_dotenv
import os

load_dotenv()

signing_key = SigningKey.generate()

priv_key_b64 = signing_key.encode(encoder=HexEncoder)
pub_key_b64 = signing_key.verify_key.encode(encoder=HexEncoder)

data = b"Asta Raven"


def sign_data(data: bytes):
    signed_b64 = signing_key.sign(data, encoder=HexEncoder)
    print("pv: ", priv_key_b64)  # private key
    print("pb: ", pub_key_b64)  # public key
    return signed_b64


def verify_data(data: bytes):
    pb_key = bytes(os.environ["PB_KEY"], encoding="utf-8")
    print("data", data)
    print("pb_key", pb_key)
    r = VerifyKey(pb_key, encoder=HexEncoder)
    print("r", r)
    try:
        belongs_to = r.verify(data, encoder=HexEncoder)
        print(belongs_to)
    except BadSignatureError:
        return "Forged!"
    return f"Certificate belongs to {belongs_to.decode('utf-8')}"
