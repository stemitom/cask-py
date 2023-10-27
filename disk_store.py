import os.path
import time

from serializer import encode_kv, decode_kv
from typing import Dict

class KeyDir:
    def __init__(self) -> None:
        self.map: Dict[str, int] = {}
    
    def set_key_offset(self, key: str, offset: int) -> None:
        self.map[key] = offset
        
    def get_offset(self, key: str) -> int:
        return self.map.get(key, -1)


class DiskStorage:
    def __init__(self, file_name: str = "data.db"):
        self.filename = file_name
        self.file = open(os.path.abspath(self.filename), "ab+")
        self._key_dir = KeyDir()
    
    def _write(self, data: bytes) -> int:
        offset = self.file.tell()
        self.file.write(data)
        self.file.flush()
        os.fsync(self.file.fileno())
        return offset

    def set(self, key: str, value: str) -> None:
        timestamp = int(time.time())
        _, data = encode_kv(timestamp, key, value)
        offset = self._write(data)
        self._key_dir.set_key_offset(key, offset)
            
    def get(self, key: str) -> str:
        offset = self._key_dir.get_offset(key)
        if offset != -1:
            self.file.seek(offset)
            encoded_data = self.file.read()
            _, _, value = decode_kv(encoded_data)
            return value
        return ""

    def close(self) -> None:
        self.file.flush()
        os.fsync(self.file.fileno())
        self.file.close()

    def __setitem__(self, key: str, value: str) -> None:
        return self.set(key, value)

    def __getitem__(self, item: str) -> str:
        return self.get(item)
