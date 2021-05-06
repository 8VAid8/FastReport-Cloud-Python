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
from fastreport_cloud_sdk.models.create_subscription_plan_vm import CreateSubscriptionPlanVM  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestCreateSubscriptionPlanVM(unittest.TestCase):
    """CreateSubscriptionPlanVM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSubscriptionPlanVM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.create_subscription_plan_vm.CreateSubscriptionPlanVM()  # noqa: E501
        if include_optional :
            return CreateSubscriptionPlanVM(
                is_active = True, 
                display_name = '', 
                time_period_type = 'Second', 
                time_period = 56, 
                templates_space_limit = 56, 
                reports_space_limit = 56, 
                exports_space_limit = 56, 
                file_upload_size_limit = 56, 
                data_source_limit = 56, 
                max_users_count = 56, 
                has_space_overdraft = True, 
                group_limit = 56, 
                online_designer = True, 
                is_demo = True, 
                url_to_buy = '', 
                unlimited_page = True, 
                page_limit = 56
            )
        else :
            return CreateSubscriptionPlanVM(
        )

    def testCreateSubscriptionPlanVM(self):
        """Test CreateSubscriptionPlanVM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
