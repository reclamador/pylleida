# -*- coding: utf-8 -*-
from .api.mail_cert import MailCertApi


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
