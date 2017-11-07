#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pylleida` package."""


import unittest
from pylleida import PyLleida


class TestPylleida(unittest.TestCase):
    def setUp(self):
        self.client = PyLleida(username='foo', password='bar')

    def tearDown(self):
        pass

    def test_has_mailcert_api(self):
        self.assertIsNotNone(self.client.mailcert)
