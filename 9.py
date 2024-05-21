import pytest
from count_chars import count_chars

def test_count_chars_with_string_input():
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_count_chars_with_empty_string_input():
    assert count_chars("") == {}

def test_count_chars_with_non_string_input():
    with pytest.raises(TypeError):
        count_chars(123)

def test_count_chars_with_non_string_iterable_input():
    with pytest.raises(TypeError):
        count_chars([1, 2, 3])
