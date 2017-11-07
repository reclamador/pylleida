
from pylleida.api import BaseApi


class MailCertApi(BaseApi):
    def __init__(self, config):
        self.endpoint = 'https://tsa.lleida.net/cgi-bin/mailcertapi.cgi'
        super(MailCertApi, self).__init__(**config)

    def get_default_settings(self):
        template_name = 'get_default_settings.xml'
        params = {}
        return self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)

    def list_pdf(self):
        pass

    def download_pdf(self):
        pass
