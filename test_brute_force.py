import pytest

import brute_force

test_data = [
    ("14:00:01","1.1.1.1"),
    ("14:00:20","1.1.1.1"),
    ("14:00:50","1.1.1.1"),
    ("14:05:00","2.2.2.2"),
    ("14:05:30","2.2.2.2"),
    ("14:09:00","2.2.2.2"),
    ("14:00:10","3.3.3.3"),
    ("14:00:17","3.3.3.3")
]

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (60, 3, ["1.1.1.1"]),
        (6, 2, []),
        (7, 2, ['3.3.3.3']),
        (20, 2, ['1.1.1.1', '3.3.3.3']),
    ],
)
def test_find_brute_force(a, b, expected):
    # Given - Arrange
    brute_force.time_threshold = a
    brute_force.tries_threshold = b
    
    # When - Act
    result = brute_force.find_brute_force(test_data)
    
    # Then, Assert
    assert result == expected
def test_zero_tries_raises_index_error():
            brute_force.time_threshold = 60
            brute_force.tries_threshold = 0
            with pytest.raises(IndexError):
                    brute_force.find_brute_force(test_data)
