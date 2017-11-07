
from pylleida.api import BaseApi


class MailCertApi(BaseApi):
    def __init__(self, config):
        self.endpoint = 'https://tsa.lleida.net/cgi-bin/mailcertapi.cgi'
        super(MailCertApi, self).__init__(**config)

    def get_default_settings(self):
        pass

    def list_pdf(self):
        pass

    def download_pdf(self):
        pass
