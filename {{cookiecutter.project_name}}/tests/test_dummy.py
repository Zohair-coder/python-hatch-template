# install the package in editable mode
# pip install -e .
# before running the tests

import {{cookiecutter.project_name}}

def test_dummy():
    assert True

def test_import():
    assert {{cookiecutter.project_name}}.just_return_true()

