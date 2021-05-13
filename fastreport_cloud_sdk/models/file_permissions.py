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


class FilePermissions(object):
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
        'owner_id': 'str',
        'owner': 'FilePermission',
        'groups': 'dict(str, FilePermission)',
        'other': 'FilePermission',
        'anon': 'FilePermission'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'owner': 'owner',
        'groups': 'groups',
        'other': 'other',
        'anon': 'anon'
    }

    def __init__(self, owner_id=None, owner=None, groups=None, other=None, anon=None, local_vars_configuration=None):  # noqa: E501
        """FilePermissions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._owner_id = None
        self._owner = None
        self._groups = None
        self._other = None
        self._anon = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if owner is not None:
            self.owner = owner
        if groups is not None:
            self.groups = groups
        if other is not None:
            self.other = other
        if anon is not None:
            self.anon = anon

    @property
    def owner_id(self):
        """Gets the owner_id of this FilePermissions.  # noqa: E501


        :return: The owner_id of this FilePermissions.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this FilePermissions.


        :param owner_id: The owner_id of this FilePermissions.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def owner(self):
        """Gets the owner of this FilePermissions.  # noqa: E501


        :return: The owner of this FilePermissions.  # noqa: E501
        :rtype: FilePermission
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FilePermissions.


        :param owner: The owner of this FilePermissions.  # noqa: E501
        :type owner: FilePermission
        """

        self._owner = owner

    @property
    def groups(self):
        """Gets the groups of this FilePermissions.  # noqa: E501


        :return: The groups of this FilePermissions.  # noqa: E501
        :rtype: dict(str, FilePermission)
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this FilePermissions.


        :param groups: The groups of this FilePermissions.  # noqa: E501
        :type groups: dict(str, FilePermission)
        """

        self._groups = groups

    @property
    def other(self):
        """Gets the other of this FilePermissions.  # noqa: E501


        :return: The other of this FilePermissions.  # noqa: E501
        :rtype: FilePermission
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this FilePermissions.


        :param other: The other of this FilePermissions.  # noqa: E501
        :type other: FilePermission
        """

        self._other = other

    @property
    def anon(self):
        """Gets the anon of this FilePermissions.  # noqa: E501


        :return: The anon of this FilePermissions.  # noqa: E501
        :rtype: FilePermission
        """
        return self._anon

    @anon.setter
    def anon(self, anon):
        """Sets the anon of this FilePermissions.


        :param anon: The anon of this FilePermissions.  # noqa: E501
        :type anon: FilePermission
        """

        self._anon = anon

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
        if not isinstance(other, FilePermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilePermissions):
            return True

        return self.to_dict() != other.to_dict()
