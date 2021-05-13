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


class UserProfileUpdateVM(object):
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
        'name': 'str',
        'username': 'str',
        'email': 'str',
        'password_new': 'str',
        'password_new2': 'str'
    }

    attribute_map = {
        'name': 'name',
        'username': 'username',
        'email': 'email',
        'password_new': 'passwordNew',
        'password_new2': 'passwordNew2'
    }

    def __init__(self, name=None, username=None, email=None, password_new=None, password_new2=None, local_vars_configuration=None):  # noqa: E501
        """UserProfileUpdateVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._username = None
        self._email = None
        self._password_new = None
        self._password_new2 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if password_new is not None:
            self.password_new = password_new
        if password_new2 is not None:
            self.password_new2 = password_new2

    @property
    def name(self):
        """Gets the name of this UserProfileUpdateVM.  # noqa: E501


        :return: The name of this UserProfileUpdateVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserProfileUpdateVM.


        :param name: The name of this UserProfileUpdateVM.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def username(self):
        """Gets the username of this UserProfileUpdateVM.  # noqa: E501


        :return: The username of this UserProfileUpdateVM.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserProfileUpdateVM.


        :param username: The username of this UserProfileUpdateVM.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this UserProfileUpdateVM.  # noqa: E501


        :return: The email of this UserProfileUpdateVM.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfileUpdateVM.


        :param email: The email of this UserProfileUpdateVM.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def password_new(self):
        """Gets the password_new of this UserProfileUpdateVM.  # noqa: E501


        :return: The password_new of this UserProfileUpdateVM.  # noqa: E501
        :rtype: str
        """
        return self._password_new

    @password_new.setter
    def password_new(self, password_new):
        """Sets the password_new of this UserProfileUpdateVM.


        :param password_new: The password_new of this UserProfileUpdateVM.  # noqa: E501
        :type password_new: str
        """

        self._password_new = password_new

    @property
    def password_new2(self):
        """Gets the password_new2 of this UserProfileUpdateVM.  # noqa: E501


        :return: The password_new2 of this UserProfileUpdateVM.  # noqa: E501
        :rtype: str
        """
        return self._password_new2

    @password_new2.setter
    def password_new2(self, password_new2):
        """Sets the password_new2 of this UserProfileUpdateVM.


        :param password_new2: The password_new2 of this UserProfileUpdateVM.  # noqa: E501
        :type password_new2: str
        """

        self._password_new2 = password_new2

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
        if not isinstance(other, UserProfileUpdateVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProfileUpdateVM):
            return True

        return self.to_dict() != other.to_dict()
