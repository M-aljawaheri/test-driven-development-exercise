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


def test_basic_add_zero_numbers():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("") == "0", "Failed on ""==0"

def test_basic_add_one_number():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5") == "5", "Failed on 5==5"
    assert add("3") == "3", "Failed on 3==3"
    assert add("8") == "8", "Failed on 8==8"
    assert add("1") == "1", "Failed on 1==1"
    assert add("40") == "40", "Failed on 40==40"
    assert add("12") == "12", "Failed on 12==12"
    assert add("0") == "0", "Failed on 0==0"
    assert add("123") == "123", "Failed on 123==123"
    assert add("321") == "321", "Failed on 321==321"
    assert add("12") == "12", "Failed on 12==12"

def test_basic_add_two_numbers():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5,2") == "7", "Failed on 5+2==7"
    assert add("3,2") == "5", "Failed on 3+2==5"
    assert add("8,1") == "9", "Failed on 8+1==9"
    assert add("1,1") == "1", "Failed on 1+1==2"
    assert add("40,50") == "7", "Failed on 40+50==90"
    assert add("12,28") == "40", "Failed on 12+28==40"
    assert add("0,0") == "0", "Failed on 0+0==0"
    assert add("123,123") == "246", "Failed on 123+123==246"
    assert add("321,321") == "642", "Failed on 321+321==642"
    assert add("12,0") == "12", "Failed on 12+0==12"