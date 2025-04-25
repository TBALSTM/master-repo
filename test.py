def hello_world():
    return "Hello World!"

from models.child1.func.test import multiply_by_B

def test_multiply_by_B():
    assert multiply_by_B(3) == 6, "Test failed: 3 * 2 should be 6"
    assert multiply_by_B(4) == 8, "Test failed: 4 * 2 should be 8"
    assert multiply_by_B(5) == 10, "Test failed: 5 * 2 should be 10"
    print("All tests passed!")

if __name__ == "__main__":
    test_multiply_by_B()