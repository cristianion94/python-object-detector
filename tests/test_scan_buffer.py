from src.object_detector import scan_buffer
from io import StringIO
import json
from src.object_detector.scan_buffer import SupportedTypes


class TestScanBuffer:
    """Test suite for scanning an image buffer."""
    def test_scan_buffer(self, image_buffer: bytes) -> None:
        """Tests something"""
        out = scan_buffer(image_buffer)
        result = json.loads(out)

        assert SupportedTypes.jpg.value == result["mime_type"]
