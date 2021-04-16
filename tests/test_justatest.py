#!/usr/bin/env python

"""Tests for the justatest module.
"""
import pytest

from justatest import justatest


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_justatest(an_object):
    assert an_object == {}
