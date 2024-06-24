import os
import unittest
import json
from common.parse_excel import ParseExcel
from common.mylogger import logger
from ddt import ddt,data,file_data,unpack
from common.http_requests import HttpRequests

# def get_test_data():
#     '''
#     从外部获取参数数据
#     :return:
#     '''
#     path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_data')
#     excelPath = os.path.join(path, 'test_user_api_data.xlsx')
#     print(excelPath)
#     sheetName = '用户参数表'
#     return ParseExcel(excelPath, sheetName)

# 读取测试用例
with open("../testdata/addbusinessWarehouse.json", 'r', encoding="utf-8") as load_f:
    addWarehouse = json.load(load_f)

@ddt
class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://work-bench.znseed.top'
        cls.Http = HttpRequests(cls.url)

    @staticmethod
    def getToken():
        uri = '/SSO-SERVER/authentication/form'
        headers ={'Content-Type': 'application/json'}
        data = {'username': 'swagger', 'password': 'swagger'}
        res = demo.Http.post(uri, data=json.dumps(data), headers=headers)
        token = 'bearer' + ' ' + res.json()['data']['tokenInfo']['token']
        return token

    @data(*addWarehouse)
    def test_addbusinessWarehouse_01(self,TestData):
        """
        创建仓库
        :param TestData:
        :return:
        """
        self.headers = {
                            'Authorization': demo.getToken(),
                           'Content-Type': 'application/json'}
        uri = '/INFRASTRUCTURE/businessWarehouse/add.magpie'
        # payload = {
        #         "warehouseOwnership": "BUILD",
        #         "leaseType": "ALL",
        #         "natureOfOperation": "WAREHOUSE",
        #         "natureOfEquity": "PRIVATE",
        #         "whName": "赣州仓",
        #         "detailedAddress": "市政府",
        #         "cityCode": "360700",
        #         "provinceCode": "360000",
        #         "provinceName": "",
        #         "allowReservation": "N",
        #         "isAdmitTransfer": "N",
        #         "city": "赣州市",
        #         "province": "江西省",
        #         "areaCode": "360702",
        #         "areaName": "章贡区",
        #         "contactsList": [],
        #         "marketId": "000",
        #         "marketName": "白糖"
        #     }
        res = demo.Http.post(uri, data=json.dumps(TestData), headers=self.headers)
        self.assertEqual(res.json()["errorCode"], '')


if __name__ == '__main__':
    unittest.main()