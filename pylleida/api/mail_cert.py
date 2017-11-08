# -*- coding: utf-8 -*-
from pylleida.api import BaseApi, BaseResponse


class MailCertApiResponse(BaseResponse):
    pass


class MailCertApi(BaseApi):
    def __init__(self, config):
        self.endpoint = 'https://tsa.lleida.net/cgi-bin/mailcertapi.cgi'
        super(MailCertApi, self).__init__(**config)

    def get_default_settings(self):
        template_name = 'get_default_settings.xml'
        params = {}
        return self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)

    def list_pdf(self,
                 mail_from=None, mail_to=None,
                 date_min=None, date_max=None,
                 file_id_min=None, file_id_max=None,
                 file_type=None, subjrw=None,
                 mail_message_id=None, row_order=None,
                 only_last_file_id=False):
        """
        Returns a list of items, each item referencing a Lleida.net email certificante.
        The input parameters act as search criteria to narrow the returned results.

        :param mail_from: results by a given sender's email address.
        :param mail_to: filter results by a given recipient's email address.
        :param date_min: filter results starting from an initial date.
        :param date_max: filter results starting from a final date.
        :param file_id_min: filter results starting from a minimum file_id.
        :param file_id_max: filter results up to a maximum file_id.
        :param file_type: filter results by the file/document type.
        :param subjrw: filter results based on a substring that appears in the emails' subjects. It is advised to
        use ASCII alphanumeric values that may appear in the first 200 character positions of the subject.
        :param mail_message_id: filter results by the message id of an email certificate.
        :param row_order: filter results by ascending or descending order based on the email certificate id.
        Valid values are 'asc' for ascending order, 'desc' for descending order.
        :param only_last_file_id: return a single element, (the latest email certificate file identifier)
        in the response.
        :return: a JSON response containing the results.
        """
        template_name = 'list_pdf.xml'
        params = {
            'mail_from': mail_from, 'mail_to': mail_to,
            'date_min': date_min, 'date_max': date_max,
            'file_id_min': file_id_min, 'file_id_max': file_id_max,
            'file_type': file_type, 'subjrw': subjrw,
            'mail_message_id': mail_message_id, 'row_order': row_order,
            'only_last_file_id': only_last_file_id
        }
        response = self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)
        return MailCertApiResponse(response)

    def download_pdf(self, file_id):
        """
        Returns the contents of an email certificate PDF file, whose file identifier matches
        the provided input parameter.

        :param file_id: the Lleida.net identifier of the requested PDF file.
        :return: a MailCertResponse object whose 'content' attribute stores the binary contents of the PDF file.
        """
        template_name = 'download_pdf.xml'
        params = {'file_id': file_id}

        response = self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)
        return MailCertApiResponse(response)
