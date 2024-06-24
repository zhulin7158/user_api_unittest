from common.confighttp import post, get

def send_request(data):
    """
    再次封装请求方法
    :param data: 测试用例
    :return:
    """
    if data["request_type"] == 'post':
        if data["file"]:
            result = post(header=data["headers"],
                          address=data["http_type"] + "://" + data["host"] + data["address"],
                          requests_parameter_type=data["parameter_type"],files=data["parameter"],
                          timeout=data["timeout"])
        else:
            result = post(header=data["headers"],address=data["http_type"] + "://" + data["host"] + data["address"],
                          requests_parameter_type=data["parameter_type"], data=data["patameter"],
                          timeout=data["timeout"])
    elif data["request_type"] == 'get':
        result = get(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                     data=data["parameter"], timeout=data["timeout"])
    else:
        return False, False
    return result