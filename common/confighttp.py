import json
import logging
import requests
import simplejson

logger = logging.getLogger(__name__)

def post(header, address, requests_parameter_type, timeout=8, data=None, files=None):
    """
    Post 请求
    :param header:
    :param address:
    :param requests_parameter_type:
    :param timeout:
    :param data:
    :param file:
    :return:
    """

    if requests_parameter_type == 'raw':
        data = json.dumps(data)
    responses = requests.post(url=address, data=data, headers =header, timeout=timeout, files=files)
    try:
        return responses.status_code, responses.json()
    except json.decoder.JSONDecodeError:
        return  responses.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return responses.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise

def get(header, address, data, timeout=8):
    """
    Get 请求
    :param header: 
    :param address: 
    :param data: 
    :param timeout: 
    :return: 
    """
    responses = requests.get(url=address, params=data, headers=header,timeout=timeout)
    if responses.status_code == '301':
        responses = requests.get(url=responses.headers["location"])
    try:
        return responses.status_code, responses.json()
    except json.decoder.JSONDecodeError:
        return responses.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return responses.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise