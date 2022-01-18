"""
This module has the method to calculate factorial of the given number
"""

from ..data.input_variables import INPUT_VALUE_1, INPUT_VALUE_2


class SampleClass:

    """Sample Class to illustrate unittesting and Jupyter notebook"""

    def __init__(self):
        pass

    def factorial(num):

        """Calculates factorial of the passed number
        num (int): Integer for which factorial is requested
        returns (int): Returns Factorial
        """
        if num in (0, 1):
            return 1
        return num * SampleClass.factorial(num - 1)

    def summation():

        """Take 2 default values defined by input_variables.py

        Returns:

        """
        return INPUT_VALUE_1 + INPUT_VALUE_2
