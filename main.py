from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder

signing_key = SigningKey.generate()

priv_key_b64 = signing_key.encode(encoder=Base64Encoder)
pub_key_b64 = signing_key.verify_key.encode(encoder=Base64Encoder)

data = b"Data to be encoded"


def sign_data(data: bytes):
    signed_b64 = signing_key.sign(data, encoder=Base64Encoder)
    return signed_b64


if __name__ == "__main__":
    signed_b64 = sign_data(data)

    print("pv: ", priv_key_b64)  # private key in alpha-numeric encoding
    print("pb: ", pub_key_b64)  # public key in alpha-numeric encoding
    print(signed_b64)

    verified = signing_key.verify_key.verify(signed_b64, encoder=Base64Encoder)

    print(verified)  # origin 'data'

    print("signed data: ", signed_b64)


""""
# To be used with saved keys

from dotenv import load_dotenv
import os

load_dotenv()

priv_key_b64 = os.environ["SIGNING_KEY"]
pub_key_b64 = os.environ["VERIFY_KEY"]
"""
