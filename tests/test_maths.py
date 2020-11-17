import pytest
import unittest

from .context import src


"""
add tests

"""

# test add
def test_add_success():
    assert src.add(2,2) == 4


# test add fail
def test_add_fail():
    assert not src.add(2,3) == 4