# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import fastreport_cloud_sdk
from fastreport_cloud_sdk.api.user_settings_api import UserSettingsApi  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException


class TestUserSettingsApi(unittest.TestCase):
    """UserSettingsApi unit test stubs"""

    def setUp(self):
        self.api = fastreport_cloud_sdk.api.user_settings_api.UserSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_settings_get_current_user_settings(self):
        """Test case for user_settings_get_current_user_settings

        Return current user settings.  # noqa: E501
        """
        pass

    def test_user_settings_update_my_settings(self):
        """Test case for user_settings_update_my_settings

        Update settings of the current user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
