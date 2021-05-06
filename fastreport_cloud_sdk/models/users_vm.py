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


class UsersVM(object):
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
        'users': 'list[UserVM]',
        'count': 'int',
        'skip': 'int',
        'take': 'int'
    }

    attribute_map = {
        'users': 'users',
        'count': 'count',
        'skip': 'skip',
        'take': 'take'
    }

    def __init__(self, users=None, count=None, skip=None, take=None, local_vars_configuration=None):  # noqa: E501
        """UsersVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._users = None
        self._count = None
        self._skip = None
        self._take = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if count is not None:
            self.count = count
        if skip is not None:
            self.skip = skip
        if take is not None:
            self.take = take

    @property
    def users(self):
        """Gets the users of this UsersVM.  # noqa: E501


        :return: The users of this UsersVM.  # noqa: E501
        :rtype: list[UserVM]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UsersVM.


        :param users: The users of this UsersVM.  # noqa: E501
        :type users: list[UserVM]
        """

        self._users = users

    @property
    def count(self):
        """Gets the count of this UsersVM.  # noqa: E501


        :return: The count of this UsersVM.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this UsersVM.


        :param count: The count of this UsersVM.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def skip(self):
        """Gets the skip of this UsersVM.  # noqa: E501


        :return: The skip of this UsersVM.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this UsersVM.


        :param skip: The skip of this UsersVM.  # noqa: E501
        :type skip: int
        """

        self._skip = skip

    @property
    def take(self):
        """Gets the take of this UsersVM.  # noqa: E501


        :return: The take of this UsersVM.  # noqa: E501
        :rtype: int
        """
        return self._take

    @take.setter
    def take(self, take):
        """Sets the take of this UsersVM.


        :param take: The take of this UsersVM.  # noqa: E501
        :type take: int
        """

        self._take = take

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
        if not isinstance(other, UsersVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersVM):
            return True

        return self.to_dict() != other.to_dict()
