from src.object_detector import scan_buffer
from io import StringIO
import json
from src.object_detector.scan_buffer import SupportedTypes


class TestScanBuffer:
    """Test suite for scanning an image buffer."""
    def test_scan_buffer(self, image_buffer: bytes, object_name: str) -> None:
        """Tests something

        Args:
            image_buffer (bytes): Filled by fixture
            object_name (str): Filled by fixture
        """
        out = scan_buffer(image_buffer)
        result = json.loads(out)

        assert SupportedTypes.jpg.value == result["mime_type"]
        assert 1 == len(result["objects"])
        assert object_name == result["objects"][0]["name"]
        assert 502 == result["objects"][0]["xmin"]
        assert 482 == result["objects"][0]["ymin"]
        assert 640 == result["objects"][0]["xmax"]
        assert 604 == result["objects"][0]["ymax"]
        assert result["objects"][0]["confidence"]
