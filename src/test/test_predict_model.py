from src.models.predict_model import SampleClass


def test_factorial():

    assert SampleClass.factorial(5) == 120
    assert SampleClass.factorial(1) == 1
    assert SampleClass.summation() == 15
