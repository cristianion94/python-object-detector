from src.object_detector import scan_buffer
from io import StringIO
import json
from src.object_detector.scan_buffer import SupportedTypes


class TestScanBuffer:

    def test_scan_buffer(self, image_buffer) -> None:
        """Tests something"""
        out = StringIO()
        scan_buffer(image_buffer, out)
        result = json.loads(out.getvalue())

        assert SupportedTypes.jpg.value == result["mime_type"]
