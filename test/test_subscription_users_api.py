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
from fastreport_cloud_sdk.api.subscription_users_api import SubscriptionUsersApi  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException


class TestSubscriptionUsersApi(unittest.TestCase):
    """SubscriptionUsersApi unit test stubs"""

    def setUp(self):
        self.api = fastreport_cloud_sdk.api.subscription_users_api.SubscriptionUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_subscription_users_add_user(self):
        """Test case for subscription_users_add_user

        Add a user to the subscription,  the added users will be displayed in the list of users of the subscription,  and these users will also have an active subscription.  # noqa: E501
        """
        pass

    def test_subscription_users_get_users(self):
        """Test case for subscription_users_get_users

        Returns all users of subscription  # noqa: E501
        """
        pass

    def test_subscription_users_leave_subscripiton(self):
        """Test case for subscription_users_leave_subscripiton

        Allows user to leave subscription,.  # noqa: E501
        """
        pass

    def test_subscription_users_remove_user(self):
        """Test case for subscription_users_remove_user

        Delete a user from the subscription,  the added users will be displayed in the list of users of the subscription,  and these users will also have an active subscription.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
