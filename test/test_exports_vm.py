# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.exports_vm import ExportsVM  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestExportsVM(unittest.TestCase):
    """ExportsVM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExportsVM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.exports_vm.ExportsVM()  # noqa: E501
        if include_optional :
            return ExportsVM(
                files = [
                    fastreport_cloud_sdk.models.export_vm.ExportVM(
                        format = 'Pdf', 
                        report_id = '', 
                        name = '', 
                        parent_id = '', 
                        tags = [
                            ''
                            ], 
                        icon = 'YQ==', 
                        type = 'File', 
                        size = 56, 
                        subscription_id = '', 
                        status = 'None', 
                        status_reason = 'None', 
                        id = '', 
                        created_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creator_user_id = '', 
                        edited_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        editor_user_id = '', )
                    ], 
                count = 56, 
                skip = 56, 
                take = 56
            )
        else :
            return ExportsVM(
        )

    def testExportsVM(self):
        """Test ExportsVM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
