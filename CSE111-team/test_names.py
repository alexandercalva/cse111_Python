from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Alexander", "Calva") == "Calva;Alexander"
    # assert make_full_name("", "correct") == ""
    # assert make_full_name("clear", "") == ""
    # assert make_full_name("happy", "funny") == ""
    # assert make_full_name("cat", "catalog") == "cat"
    # assert make_full_name("dogmatic", "dog") == "dog"
    # assert make_full_name("jump", "joyous") == "j"
    # assert make_full_name("unwise", "ungrateful") == "un"
    # assert make_full_name("Disable", "dIstasteful") == "dis"

def test_extract_family_name():
    assert extract_family_name("Calva;Alexander") == "Calva"
    # assert extract_family_name("", "correct") == ""
    # assert extract_family_name("clear", "") == ""
    # assert extract_family_name("happy", "funny") == ""
    # assert extract_family_name("cat", "catalog") == "cat"
    # assert extract_family_name("dogmatic", "dog") == "dog"
    # assert extract_family_name("jump", "joyous") == "j"
    # assert extract_family_name("unwise", "ungrateful") == "un"
    # assert extract_family_name("Disable", "dIstasteful") == "dis"

def test_extract_given_name():
    assert extract_given_name("Calva;Alexander") == "Alexander"
    # assert extract_given_name("", "correct") == ""
    # assert extract_given_name("clear", "") == ""
    # assert extract_given_name("happy", "funny") == ""
    # assert extract_given_name("cat", "catalog") == "cat"
    # assert extract_given_name("dogmatic", "dog") == "dog"
    # assert extract_given_name("jump", "joyous") == "j"
    # assert extract_given_name("unwise", "ungrateful") == "un"
    # assert extract_given_name("Disable", "dIstasteful") == "dis"

# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])