import src.object_detector


class TestObjectDetector:
    def test_negative_export(self) -> None:
        """Tests negative package structure."""
        assert "random" not in src.object_detector.__all__

    def test_export_scan_buffer(self) -> None:
        """Tests the package structure contains scan_buffer."""
        assert "scan_buffer" in src.object_detector.__all__

    def test_export_scan_file(self) -> None:
        """Tests the package structure contains scan_file."""
        assert "scan_file" in src.object_detector.__all__
