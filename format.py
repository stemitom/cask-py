import struct

HEADER_SIZE = 12


def encode_header(timestamp: int, key_size: int, value_size: int) -> bytes:
    return struct.pack("<III", timestamp, key_size, value_size)


def encode_kv(timestamp: int, key: str, value: str) -> tuple[int, bytes]:
    header: bytes = encode_header(timestamp, len(key), len(value))
    key_bytes: bytes = key.encode("utf-8")
    value_bytes: bytes = value.encode("utf-8")
    data = header + key_bytes + value_bytes
    return len(data), data


def decode_kv(data: bytes) -> tuple[int, str, str]:
    timestamp, key_size, _ = decode_header(data)
    key = data[HEADER_SIZE: HEADER_SIZE + key_size].decode("utf-8")
    value = data[HEADER_SIZE + key_size:].decode("utf-8")
    return timestamp, key, value


def decode_header(data: bytes) -> tuple[int, int, int]:
    timestamp, key_size, value_size = struct.unpack("<III", data[:HEADER_SIZE])
    print(len(data[:HEADER_SIZE]))
    return timestamp, key_size, value_size
