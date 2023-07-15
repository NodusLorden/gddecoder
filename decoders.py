import base64
import gzip


# bytes string -> bytes
def xor(by: bytes, mask: bytes = 11) -> bytes:
    return bytes(map(lambda x: x ^ mask, by))


# bytes -> base64 bytes
def from_base64(by: bytes) -> bytes:
    return base64.b64decode(by.decode("ASCII").replace("_", "/").replace("-", "+"))


# bytes base64 -> bytes
def to_base64(by: bytes) -> bytes:
    return base64.b64encode(by).decode("ASCII").replace("/", "_").replace("+", "-").encode("ASCII")


# bytes -> string
def from_gzip(by: bytes) -> str:
    return gzip.decompress(by).decode()


# string -> bytes
def to_gzip(st: str, compresslevel=0) -> bytes:
    return gzip.compress(st.encode(), compresslevel=compresslevel)


# bytes from file -> plist
def save_file_decoder(by: bytes):
    return from_gzip(from_base64(xor(by)))


# plist -> bytes from file
def save_file_encoder(st: str):
    return xor(to_base64(to_gzip(st)))


# k4 string -> blocks
def editor_decoder(st: str) -> str:
    return from_gzip(from_base64(st.encode()))


# blocks -> k4 string
def editor_encoder(st: str) -> str:
    return to_base64(to_gzip(st)).decode()


# k34 string -> string
def k34_decoder(st: str) -> str:
    return from_gzip(from_base64(st.encode()))


# k3 string -> text string
def description_decoder(st: str) -> str:
    return from_base64(st.encode()).decode()


def encode_gjp(psw: str):
    return to_base64(gjp_xor(psw, 37526))


def decode_gjp(gjp: str):
    return gjp_xor(from_base64(gjp), 37526)


#  base64 str -> text
def decode_text(st: str):
    return from_base64(st.encode()).decode()


#  text -> base64 str
def encode_text(text: str):
    return to_base64(text.encode()).decode()


def gjp_xor(psw: str, key: int):
    key = str(key)
    xst = ""
    for i in range(len(psw)):
        xst += chr(ord(psw[i]) ^ ord(key[i % len(key)]))
    return xst
