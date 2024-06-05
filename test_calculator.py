"""
Test Module for String Calculator
----------------------------------
    @author: [student's name] - [student's email]
    @date: [date of creation]
    @description: This test module is designed to test the functionality of the string calculator
             defined in the calculator.py module. Using pytest for testing allows for more
             concise and powerful test capabilities, which is integrated into the GitHub
             workflow for continuous integration and testing.
"""

import pytest
from calculator import add

def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5,2") == "7", "Failed on 5+2==7"

def test_missing_last_number():
    """
        Tests missing last number. 
    """
    assert ("5\n,") == "Number expected but EOF found."
    assert add("5,") == "Number expected but EOF found."
    assert add("5,,") == "Number expected but EOF found."
    assert add("1,3,") == "Number expected but EOF found."
    assert add("1,3,") == "Number expected but EOF found."
    assert add("1,3,4,") == "Number expected but EOF found."
    assert add(",") == "Number expected but EOF found."
    assert add(",,") == "Number expected but EOF found."
    assert add("1,,3") == "Number expected but EOF found."
    assert add("1,3,4,") == "Number expected but EOF found."
    assert add("1, 3, 4, ,") == "Number expected but EOF found."