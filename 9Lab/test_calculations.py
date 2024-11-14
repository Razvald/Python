from calculations import multiply, divide, distance, solve_quadratic, geometric_sum
import pytest

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 5) == 0
    assert multiply(2, -3) == -6
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(0, 1) == 0
    with pytest.raises(ValueError):
        divide(10, 0)

def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 4, 5) == 5
    assert distance(-1, -1, -4, -5) == 5
    assert distance(0, 0, 0, 0) == 0
    assert distance(2, 3, 2, 3) == 0

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2, 1)
    assert solve_quadratic(1, 2, 1) == -1
    assert solve_quadratic(1, 0, -4) == (2, -2)
    assert solve_quadratic(1, -2, 1) == 1
    assert solve_quadratic(1, 1, 1) == None

def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
    assert geometric_sum(2, 2, 3) == 14
    assert geometric_sum(3, 1, 5) == 15
    assert geometric_sum(1, 0.5, 4) == 1.875
    assert geometric_sum(5, 3, 2) == 20
