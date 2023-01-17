from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from dotenv import load_dotenv
import os

load_dotenv()

signing_key = SigningKey.generate()

priv_key_b64 = signing_key.encode(encoder=HexEncoder)
pub_key_b64 = signing_key.verify_key.encode(encoder=HexEncoder)

# Keys in string format
f_pv = priv_key_b64.decode("utf-8")
f_pb = pub_key_b64.decode("utf-8")


def sign_data(data: bytes):
    signed_b64 = signing_key.sign(data, encoder=HexEncoder)
    return signed_b64


def verify_data(data: bytes):
    pb_key = bytes(os.environ["PB_KEY"], encoding="utf-8")
    r = VerifyKey(pb_key, encoder=HexEncoder)
    try:
        belongs_to = r.verify(data, encoder=HexEncoder)
    except BadSignatureError:
        return "Forged!"
    return f"Certificate belongs to {belongs_to.decode('utf-8')}"
