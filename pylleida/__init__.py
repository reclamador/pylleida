# -*- coding: utf-8 -*-

"""Top-level package for pylleida."""

__author__ = """NickM. Jaremek"""
__email__ = 'nick13jaremek@gmail.com'
__version__ = '0.2.0'

from pylleida.api.mail_cert import MailCertApi


class PyLleida(object):
    def __init__(self, username, password):
        """
        Python wrapper for the Lleida.net API.

        There exists only one way to authenticate with the Lleida.net API, which consists on providing a
        username/password combination.

        :param username: Lleida.net username
        :param password: Lleida.net password
        """

        config = dict(
            username=username,
            password=password
        )

        self.mailcert = MailCertApi(config)
