from typing import TextIO
import json


def scan_buffer(buffer: bytes, out: TextIO) -> None:
    scan_output = {
        "buffer_size": len(buffer)
    }

    out.write(json.dumps(scan_output, indent=4))
