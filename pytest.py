from cone_volume import cone_volume
from pytest import approx
import pytest

assert cone_volume(0.6,-9) == approx(-25.09)

pytest.main(["-v", "--tb=line", "-rN", "pytest.py"])
