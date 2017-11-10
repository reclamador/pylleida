========
pylleida
========


.. image:: https://img.shields.io/pypi/v/pylleida.svg
        :target: https://pypi.python.org/pypi/pylleida

.. image:: https://img.shields.io/travis/nick13jaremek/pylleida.svg
        :target: https://travis-ci.org/nick13jaremek/pylleida

.. image:: https://readthedocs.org/projects/pylleida/badge/?version=latest
        :target: https://pylleida.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/nick13jaremek/pylleida/shield.svg
     :target: https://pyup.io/repos/github/nick13jaremek/pylleida/
     :alt: Updates


A HTTP Python client to use the Lleida.net API. This API consists of several modules,
each one related to a different set of services. More information can be found at the
official `API listing website`_.

.. _`API listing website`: https://api.lleida.net/devel/es/index.html#api


* Free software: MIT license
* Documentation: https://pylleida.readthedocs.io.


Disclosure
----------

This Python library has been developed by the **reclamador.es** team without any previous collaboration agreement with Lleida.net. The code in this repository will be updated according to the updates on the Lleida.net APIs, initially based on the internal requirements of the **reclamador.es** team.

Features
--------

* MailCert API: lets the client check the status of the PDF email certificate documents emitted by the Lleida.net MailCert service. Currently implemented methods:

    * **get_default_settings**: retrieves a list of the MailCert service's configuration parameters associated to the account used by the PyLleida client.
    * **list_pdf**: fetches a listing of PDF documents (email certificates), indicating their metadat, status and other identification data.
    * **download_pdf**: fetches the binary data of a given PDF document (email certificate) if possible, otherwise returns an error response.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

