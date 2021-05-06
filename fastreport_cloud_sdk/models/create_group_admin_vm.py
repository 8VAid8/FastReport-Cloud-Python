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


class CreateGroupAdminVM(object):
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
        'name': 'str',
        'subscription_id': 'str'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'name': 'name',
        'subscription_id': 'subscriptionId'
    }

    def __init__(self, owner_id=None, name=None, subscription_id=None, local_vars_configuration=None):  # noqa: E501
        """CreateGroupAdminVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._owner_id = None
        self._name = None
        self._subscription_id = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        self.name = name
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def owner_id(self):
        """Gets the owner_id of this CreateGroupAdminVM.  # noqa: E501


        :return: The owner_id of this CreateGroupAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CreateGroupAdminVM.


        :param owner_id: The owner_id of this CreateGroupAdminVM.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this CreateGroupAdminVM.  # noqa: E501


        :return: The name of this CreateGroupAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGroupAdminVM.


        :param name: The name of this CreateGroupAdminVM.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this CreateGroupAdminVM.  # noqa: E501


        :return: The subscription_id of this CreateGroupAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this CreateGroupAdminVM.


        :param subscription_id: The subscription_id of this CreateGroupAdminVM.  # noqa: E501
        :type subscription_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_id is not None and not re.search(r'^[A-Fa-f0-9]{24}$', subscription_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `subscription_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501

        self._subscription_id = subscription_id

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
        if not isinstance(other, CreateGroupAdminVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGroupAdminVM):
            return True

        return self.to_dict() != other.to_dict()
