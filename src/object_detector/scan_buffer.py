from typing import TextIO
import json
import numpy as np
import cv2
from filetype import guess_mime
from enum import Enum, unique


@unique
class SupportedTypes(Enum):
    """Supported file types"""
    jpg = "image/jpeg"
    png = "image/png"


def validate_file_type(buffer: bytes):
    mime = guess_mime(buffer)
    if mime is None:
        raise TypeError("File type not supported.")
    return SupportedTypes(mime)


def decode_image(buffer: bytes):
    return cv2.imdecode(np.frombuffer(buffer, dtype=np.uint8), flags=1)


def scan_buffer(buffer: bytes, out: TextIO) -> None:
    mime_type = validate_file_type(buffer)
    image = decode_image(buffer)

    scan_output = {
        "buffer_size": len(buffer),
        "mime_type": mime_type,
    }

    out.write(json.dumps(scan_output, indent=4))
