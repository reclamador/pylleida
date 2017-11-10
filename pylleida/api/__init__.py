# -*- coding: utf-8 -*-
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
        return json.loads(json.dumps(xml_content))

    def _updated_params(self, in_params):
        base_params = {'username': self.username, 'password': self.password}
        return dict(base_params, **in_params)

    def post(self, endpoint, template_name, in_params):
        params = self._updated_params(in_params)
        template = render_template(template_filename=template_name, **params)

        request_data = {'xml': template}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(endpoint, data=request_data, headers=headers, timeout=self.TIMEOUT)

        try:
            xml_response = xmltodict.parse(xml_input=response.content)
            ret_response = self._xml_to_json(xml_response)
        except xmltodict.expat.ExpatError:
            ret_response = {'content': response.content}
        return ret_response


class ResponseItem(object):
    pass


class BaseResponse(object):
    def __init__(self, json_data):
        self._update_attributes(self, json_data)

    def _format_key(self, key):
        if key.startswith('@'):
            return key.replace('@', '')
        return key

    def _update_attributes(self, obj, data):
        for key in data.keys():
            if key.startswith('_'):
                continue

            formatted_key = self._format_key(key)
            value = data[key]
            if isinstance(value, list):
                value_items = []
                for item in value:
                    new_obj = ResponseItem()
                    self._update_attributes(new_obj, item)
                    value_items.append(new_obj)
                setattr(obj, formatted_key, value_items)
            elif isinstance(value, dict):
                new_obj = ResponseItem()
                self._update_attributes(new_obj, value)
                setattr(obj, formatted_key, new_obj)
            else:
                setattr(obj, formatted_key, value)
