import pytest
from calculator import subtract


class TestSubtractBug:
    """Regression test for subtract function bug."""
    
    def test_subtract_5_minus_3(self):
        """subtract(5, 3) should return 2, not 1."""
        assert subtract(5, 3) == 2
    
    def test_subtract_10_minus_4(self):
        """subtract(10, 4) should return 6, not 5."""
        assert subtract(10, 4) == 6
    
    def test_subtract_7_minus_2(self):
        """subtract(7, 2) should return 5, not 4."""
        assert subtract(7, 2) == 5
