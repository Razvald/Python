import pytest
from main import multiply, divide, distance, solve_quadratic, geometric_sum
from main import word_count, find_word, to_uppercase

# Фикстура для работы с текстовым файлом
@pytest.fixture
def sample_text():
    with open("text_sample.txt", "r") as file:
        return file.read()

class TestMathFunctions:
    
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6), (0, 5, 0), (-1, 5, -5)
    ])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2), (5, 2, 2.5), (10, 5, 2)
    ])
    def test_divide(self, a, b, expected):
        assert divide(a, b) == expected

    @pytest.mark.parametrize("x1, y1, x2, y2, expected", [
        (0, 0, 3, 4, 5), (1, 1, 4, 5, 5), (2, 2, 2, 2, 0)
    ])
    def test_distance(self, x1, y1, x2, y2, expected):
        assert distance(x1, y1, x2, y2) == expected

    @pytest.mark.parametrize("a, b, c, expected", [
        (1, -3, 2, (2, 1)), (1, 2, 1, -1), (1, 0, 1, None)
    ])
    def test_solve_quadratic(self, a, b, c, expected):
        assert solve_quadratic(a, b, c) == expected

    @pytest.mark.parametrize("a, r, n, expected", [
        (1, 0.5, 3, 1.75), (2, 2, 2, 6), (3, 1, 4, 12)
    ])
    def test_geometric_sum(self, a, r, n, expected):
        assert geometric_sum(a, r, n) == pytest.approx(expected)

class TestTextFunctions:
    
    @pytest.mark.parametrize("expected", [10])
    def test_word_count(self, sample_text, expected):
        assert word_count(sample_text) == expected

    @pytest.mark.parametrize("word, expected", [
        ("Hello", True), ("apple", False)
    ])
    def test_find_word(self, sample_text, word, expected):
        assert find_word(sample_text, word) == expected

    @pytest.mark.parametrize("expected", ["HELLO WORLD! THIS IS A SAMPLE TEXT FOR TESTING PURPOSES."])
    def test_to_uppercase(self, sample_text, expected):
        assert to_uppercase(sample_text) == expected


