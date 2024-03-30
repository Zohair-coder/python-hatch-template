import pytest

# install the package in editable mode
# pip install -e .
# before running the tests

import gflights

def test_dummy():
    assert True

def test_import():
    assert gflights.just_return_true()

