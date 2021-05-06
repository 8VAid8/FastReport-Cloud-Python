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


class SubscriptionFolder(object):
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
        'folder_id': 'str',
        'bytes_used': 'int'
    }

    attribute_map = {
        'folder_id': 'folderId',
        'bytes_used': 'bytesUsed'
    }

    def __init__(self, folder_id=None, bytes_used=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionFolder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._folder_id = None
        self._bytes_used = None
        self.discriminator = None

        if folder_id is not None:
            self.folder_id = folder_id
        if bytes_used is not None:
            self.bytes_used = bytes_used

    @property
    def folder_id(self):
        """Gets the folder_id of this SubscriptionFolder.  # noqa: E501


        :return: The folder_id of this SubscriptionFolder.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this SubscriptionFolder.


        :param folder_id: The folder_id of this SubscriptionFolder.  # noqa: E501
        :type folder_id: str
        """

        self._folder_id = folder_id

    @property
    def bytes_used(self):
        """Gets the bytes_used of this SubscriptionFolder.  # noqa: E501


        :return: The bytes_used of this SubscriptionFolder.  # noqa: E501
        :rtype: int
        """
        return self._bytes_used

    @bytes_used.setter
    def bytes_used(self, bytes_used):
        """Sets the bytes_used of this SubscriptionFolder.


        :param bytes_used: The bytes_used of this SubscriptionFolder.  # noqa: E501
        :type bytes_used: int
        """

        self._bytes_used = bytes_used

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
        if not isinstance(other, SubscriptionFolder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionFolder):
            return True

        return self.to_dict() != other.to_dict()
