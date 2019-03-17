import pytest
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from argparseGraph import argparseGraph as agg

def test_hello_worls():
    print("hello world")
    # assert True == False
