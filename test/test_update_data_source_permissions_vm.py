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
from fastreport_cloud_sdk.models.update_data_source_permissions_vm import UpdateDataSourcePermissionsVM  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestUpdateDataSourcePermissionsVM(unittest.TestCase):
    """UpdateDataSourcePermissionsVM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateDataSourcePermissionsVM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.update_data_source_permissions_vm.UpdateDataSourcePermissionsVM()  # noqa: E501
        if include_optional :
            return UpdateDataSourcePermissionsVM(
                new_permissions = fastreport_cloud_sdk.models.data_source_permissions.DataSourcePermissions(
                    owner_id = '', 
                    owner = fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, ), 
                    groups = {
                        'key' : fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                            create = 0, 
                            delete = 0, 
                            execute = 0, 
                            get = 0, 
                            update = 0, 
                            administrate = 0, )
                        }, 
                    other = fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, ), 
                    anon = fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, ), ), 
                administrate = 0
            )
        else :
            return UpdateDataSourcePermissionsVM(
                new_permissions = fastreport_cloud_sdk.models.data_source_permissions.DataSourcePermissions(
                    owner_id = '', 
                    owner = fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, ), 
                    groups = {
                        'key' : fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                            create = 0, 
                            delete = 0, 
                            execute = 0, 
                            get = 0, 
                            update = 0, 
                            administrate = 0, )
                        }, 
                    other = fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, ), 
                    anon = fastreport_cloud_sdk.models.data_source_permission.DataSourcePermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, ), ),
                administrate = 0,
        )

    def testUpdateDataSourcePermissionsVM(self):
        """Test UpdateDataSourcePermissionsVM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
