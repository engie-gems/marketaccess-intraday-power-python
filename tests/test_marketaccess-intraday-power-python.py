#!/usr/bin/env python
# coding: utf-8

"""
test_marketaccess-intraday-power-python
----------------------------------
Tests for `marketaccess-intraday-power-python` module.
"""

# Third Party Libraries
import logging
import pytest

# Python API Wrapper for the Market Access Intraday Power Modules
# from marketaccess-intraday-power-python import marketaccess-intraday-power-python

# pylint: disable=redefined-outer-name, unused-argument

log = logging.getLogger(__name__)

@pytest.fixture
def setup_000(mocker):
    # mocker.patch("module.to.patchsleep")
    yield


def test_000_something(setup_000):
    pass
