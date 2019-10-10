#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pylleida` package."""


import unittest
import mock
from pylleida import PyLleida
import json


class TestPylleida(unittest.TestCase):
    def setUp(self):
        self.client = PyLleida(username='foo', password='bar')

    def tearDown(self):
        pass

    @mock.patch('xmltodict.parse')
    @mock.patch('requests.post')
    def test_base_api_post(self, mock_requests_post, mock_xmltodict_parse):
        mock_xmltodict_parse.return_value = '{"var": 1}'
        self.client.mailcert.post('https//endpoint', 'list_pdf.xml', {'param1': 1, 'param2': 2})
        mock_requests_post.assert_called_once_with('https//endpoint', data=mock.ANY,
                                                   headers={'content-type': 'application/x-www-form-urlencoded'},
                                                   timeout=60.0)
        mock_xmltodict_parse.assert_called_once()

    def test_has_mailcert_api(self):
        self.assertIsNotNone(self.client.mailcert)

    def test_mailcert_api_attributes(self):
        self.assertEqual(self.client.mailcert.username, 'foo')
        self.assertEqual(self.client.mailcert.password, 'bar')

    @mock.patch('pylleida.api.BaseApi.post')
    def test_mailcert_api_get_default_settings(self, mock_api_post):
        self.client.mailcert.get_default_settings()
        mock_api_post.assert_called_once_with(endpoint='https://tsa.lleida.net/cgi-bin/mailcertapi.cgi',
                                                   template_name='get_default_settings.xml', in_params={})

    @mock.patch('pylleida.api.BaseApi.post')
    def test_mailcert_list_pdf(self, mock_api_post):
        params = {'date_min': None, 'file_type': None, 'mail_to': 'to@email.com', 'row_order': None,
                  'file_id_max': None, 'subjrw': None, 'mail_message_id': None, 'mail_from': 'from@email.com',
                  'file_id_min': None,
                  'only_last_file_id': False, 'date_max': None}
        self.client.mailcert.list_pdf(mail_from='from@email.com', mail_to='to@email.com')
        mock_api_post.assert_called_once_with(endpoint='https://tsa.lleida.net/cgi-bin/mailcertapi.cgi',
                                              template_name='list_pdf.xml', in_params=params)


    @mock.patch('pylleida.api.BaseApi.post')
    def test_mailcert_download_pdf(self, mock_api_post):
        params = {'file_id': 'fileid'}
        self.client.mailcert.download_pdf(file_id='fileid')
        mock_api_post.assert_called_once_with(endpoint='https://tsa.lleida.net/cgi-bin/mailcertapi.cgi',
                                              template_name='download_pdf.xml', in_params=params)









