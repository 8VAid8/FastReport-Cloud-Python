# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from fastreport_cloud_sdk.configuration import Configuration


class UpdateUserSettingsVM(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'profile_visibility': 'ProfileVisibility',
        'default_subscription': 'str',
        'show_hidden_files_and_folders': 'bool'
    }

    attribute_map = {
        'profile_visibility': 'profileVisibility',
        'default_subscription': 'defaultSubscription',
        'show_hidden_files_and_folders': 'showHiddenFilesAndFolders'
    }

    def __init__(self, profile_visibility=None, default_subscription=None, show_hidden_files_and_folders=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserSettingsVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._profile_visibility = None
        self._default_subscription = None
        self._show_hidden_files_and_folders = None
        self.discriminator = None

        self.profile_visibility = profile_visibility
        self.default_subscription = default_subscription
        self.show_hidden_files_and_folders = show_hidden_files_and_folders

    @property
    def profile_visibility(self):
        """Gets the profile_visibility of this UpdateUserSettingsVM.  # noqa: E501


        :return: The profile_visibility of this UpdateUserSettingsVM.  # noqa: E501
        :rtype: ProfileVisibility
        """
        return self._profile_visibility

    @profile_visibility.setter
    def profile_visibility(self, profile_visibility):
        """Sets the profile_visibility of this UpdateUserSettingsVM.


        :param profile_visibility: The profile_visibility of this UpdateUserSettingsVM.  # noqa: E501
        :type profile_visibility: ProfileVisibility
        """

        self._profile_visibility = profile_visibility

    @property
    def default_subscription(self):
        """Gets the default_subscription of this UpdateUserSettingsVM.  # noqa: E501


        :return: The default_subscription of this UpdateUserSettingsVM.  # noqa: E501
        :rtype: str
        """
        return self._default_subscription

    @default_subscription.setter
    def default_subscription(self, default_subscription):
        """Sets the default_subscription of this UpdateUserSettingsVM.


        :param default_subscription: The default_subscription of this UpdateUserSettingsVM.  # noqa: E501
        :type default_subscription: str
        """

        self._default_subscription = default_subscription

    @property
    def show_hidden_files_and_folders(self):
        """Gets the show_hidden_files_and_folders of this UpdateUserSettingsVM.  # noqa: E501


        :return: The show_hidden_files_and_folders of this UpdateUserSettingsVM.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_files_and_folders

    @show_hidden_files_and_folders.setter
    def show_hidden_files_and_folders(self, show_hidden_files_and_folders):
        """Sets the show_hidden_files_and_folders of this UpdateUserSettingsVM.


        :param show_hidden_files_and_folders: The show_hidden_files_and_folders of this UpdateUserSettingsVM.  # noqa: E501
        :type show_hidden_files_and_folders: bool
        """

        self._show_hidden_files_and_folders = show_hidden_files_and_folders

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateUserSettingsVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserSettingsVM):
            return True

        return self.to_dict() != other.to_dict()
