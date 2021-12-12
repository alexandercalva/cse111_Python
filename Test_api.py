from apiFile import read_Scriptures
import pytest

def Test_read_scriptures(fileName):
    assert read_Scriptures(fileName) == "scriptures.csv" 

pytest.main(["-v", "--tb=line", "-rN", __file__])

