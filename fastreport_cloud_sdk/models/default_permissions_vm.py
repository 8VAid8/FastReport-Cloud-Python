# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from fastreport_cloud_sdk.configuration import Configuration


class DefaultPermissionsVM(object):
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
        'file_permissions': 'FilePermissions',
        'data_source_permissions': 'DataSourcePermissions',
        'group_permissions': 'GroupPermissions'
    }

    attribute_map = {
        'file_permissions': 'filePermissions',
        'data_source_permissions': 'dataSourcePermissions',
        'group_permissions': 'groupPermissions'
    }

    def __init__(self, file_permissions=None, data_source_permissions=None, group_permissions=None, local_vars_configuration=None):  # noqa: E501
        """DefaultPermissionsVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file_permissions = None
        self._data_source_permissions = None
        self._group_permissions = None
        self.discriminator = None

        if file_permissions is not None:
            self.file_permissions = file_permissions
        if data_source_permissions is not None:
            self.data_source_permissions = data_source_permissions
        if group_permissions is not None:
            self.group_permissions = group_permissions

    @property
    def file_permissions(self):
        """Gets the file_permissions of this DefaultPermissionsVM.  # noqa: E501


        :return: The file_permissions of this DefaultPermissionsVM.  # noqa: E501
        :rtype: FilePermissions
        """
        return self._file_permissions

    @file_permissions.setter
    def file_permissions(self, file_permissions):
        """Sets the file_permissions of this DefaultPermissionsVM.


        :param file_permissions: The file_permissions of this DefaultPermissionsVM.  # noqa: E501
        :type file_permissions: FilePermissions
        """

        self._file_permissions = file_permissions

    @property
    def data_source_permissions(self):
        """Gets the data_source_permissions of this DefaultPermissionsVM.  # noqa: E501


        :return: The data_source_permissions of this DefaultPermissionsVM.  # noqa: E501
        :rtype: DataSourcePermissions
        """
        return self._data_source_permissions

    @data_source_permissions.setter
    def data_source_permissions(self, data_source_permissions):
        """Sets the data_source_permissions of this DefaultPermissionsVM.


        :param data_source_permissions: The data_source_permissions of this DefaultPermissionsVM.  # noqa: E501
        :type data_source_permissions: DataSourcePermissions
        """

        self._data_source_permissions = data_source_permissions

    @property
    def group_permissions(self):
        """Gets the group_permissions of this DefaultPermissionsVM.  # noqa: E501


        :return: The group_permissions of this DefaultPermissionsVM.  # noqa: E501
        :rtype: GroupPermissions
        """
        return self._group_permissions

    @group_permissions.setter
    def group_permissions(self, group_permissions):
        """Sets the group_permissions of this DefaultPermissionsVM.


        :param group_permissions: The group_permissions of this DefaultPermissionsVM.  # noqa: E501
        :type group_permissions: GroupPermissions
        """

        self._group_permissions = group_permissions

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, DefaultPermissionsVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefaultPermissionsVM):
            return True

        return self.to_dict() != other.to_dict()
