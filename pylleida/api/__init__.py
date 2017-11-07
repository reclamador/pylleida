
import json
import requests
import xmltodict
from pylleida.configuration import render_template


class BaseApi(object):
    TIMEOUT = 60.0

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _xml_to_json(self, xml_content):
        return json.dumps(xml_content)['result']  # XML response data are wrapped in 'result' tag

    def _updated_params(self, in_params):
        base_params = {'username': self.username, 'password': self.password}
        return dict(base_params, **in_params)

    def post(self, endpoint, template_name, in_params):
        params = self._updated_params(in_params)
        template = render_template(template_filename=template_name, **params)

        request_data = {'xml': template}
        headers = {'content-type': 'application/soap+xml;charset=utf-8', 'SOAPAction': 'any'}

        response = requests.post(endpoint, data=request_data, headers=headers, timeout=self.TIMEOUT)
        xml_response = xmltodict.parse(xml_input=response.content)
        return self._xml_to_json(xml_response)


