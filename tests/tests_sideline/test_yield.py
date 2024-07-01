import pytest


@pytest.fixture
def example_ficture():
    print("\n--- Setup part of the fixture ---")
    yield
    print("\n--- Teardown part of the fixture ---")


@pytest.fixture
def sample_data():
    #print("\n--- Create data ---")
    data = {"key": "value"}
    yield data  # Passing data to the test function
    print("\n--- Teardown part of the fixture ---")


def test_example(example_ficture):
    assert 1 == 1


def test_sample_data(sample_data):
    assert sample_data["key"] == "value"



# pytest -s -v test_yield.py - pass
