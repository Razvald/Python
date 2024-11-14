import pytest
from main import multiply, divide, distance, solve_quadratic, geometric_sum

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 4, 5) == 5

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2, 1)
    assert solve_quadratic(1, 2, 1) == -1
    assert solve_quadratic(1, 0, 1) == None

def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
    assert geometric_sum(3, 1, 5) == 15
