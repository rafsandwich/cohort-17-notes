import pytest
from triangle import is_valid_triangle

def test_is_valid_triangle_negative_case_should_be_right_triangle():
    assert not is_valid_triangle(5, 10, 25)

def test_is_valid_triangle_postitve_case_right_triangle():
    assert is_valid_triangle(3,4,5)

def test_is_valid_triangle_wrong_number_sides():
    with pytest.raises(TypeError):
        is_valid_triangle(1, 2, 3, 4)

def test_is_valid_triangle_string_params():
    with pytest.raises(TypeError):
        
        is_valid_triangle("2", 2, 5)