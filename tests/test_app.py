# -*- coding: utf-8 -*-

import pytest
from yaabook.app import extract_name_and_email

__author__ = "fr.Innocent"
__copyright__ = "fr.Innocent"
__license__ = "mit"


def test_extractor():
    data = 'From: "Dan at Real Python" <info@realpython.com>'
    assert extract_name_and_email(data) == ('Dan at Real Python', 'info@realpython.com')
