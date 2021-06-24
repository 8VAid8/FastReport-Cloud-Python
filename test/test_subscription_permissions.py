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
from fastreport_cloud_sdk.models.subscription_permissions import SubscriptionPermissions  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestSubscriptionPermissions(unittest.TestCase):
    """SubscriptionPermissions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionPermissions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.subscription_permissions.SubscriptionPermissions()  # noqa: E501
        if include_optional :
            return SubscriptionPermissions(
                owner_id = 'f325375e-30fc-ba00-1731-c574773100bf', 
                owner = fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission(
                    create = 0, 
                    delete = 0, 
                    execute = 0, 
                    get = 0, 
                    update = 0, 
                    administrate = 0, ), 
                groups = {
                    'key' : fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission(
                        create = 0, 
                        delete = 0, 
                        execute = 0, 
                        get = 0, 
                        update = 0, 
                        administrate = 0, )
                    }, 
                other = fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission(
                    create = 0, 
                    delete = 0, 
                    execute = 0, 
                    get = 0, 
                    update = 0, 
                    administrate = 0, ), 
                anon = fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission(
                    create = 0, 
                    delete = 0, 
                    execute = 0, 
                    get = 0, 
                    update = 0, 
                    administrate = 0, )
            )
        else :
            return SubscriptionPermissions(
        )

    def testSubscriptionPermissions(self):
        """Test SubscriptionPermissions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
