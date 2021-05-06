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


class CreateDataSourceAdminVM(object):
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
        'connection_string': 'str',
        'subscription_id': 'str',
        'connection_type': 'str'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'name': 'name',
        'connection_string': 'connectionString',
        'subscription_id': 'subscriptionId',
        'connection_type': 'connectionType'
    }

    def __init__(self, owner_id=None, name=None, connection_string=None, subscription_id=None, connection_type=None, local_vars_configuration=None):  # noqa: E501
        """CreateDataSourceAdminVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._owner_id = None
        self._name = None
        self._connection_string = None
        self._subscription_id = None
        self._connection_type = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if name is not None:
            self.name = name
        if connection_string is not None:
            self.connection_string = connection_string
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if connection_type is not None:
            self.connection_type = connection_type

    @property
    def owner_id(self):
        """Gets the owner_id of this CreateDataSourceAdminVM.  # noqa: E501


        :return: The owner_id of this CreateDataSourceAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CreateDataSourceAdminVM.


        :param owner_id: The owner_id of this CreateDataSourceAdminVM.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this CreateDataSourceAdminVM.  # noqa: E501


        :return: The name of this CreateDataSourceAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDataSourceAdminVM.


        :param name: The name of this CreateDataSourceAdminVM.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def connection_string(self):
        """Gets the connection_string of this CreateDataSourceAdminVM.  # noqa: E501


        :return: The connection_string of this CreateDataSourceAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this CreateDataSourceAdminVM.


        :param connection_string: The connection_string of this CreateDataSourceAdminVM.  # noqa: E501
        :type connection_string: str
        """

        self._connection_string = connection_string

    @property
    def subscription_id(self):
        """Gets the subscription_id of this CreateDataSourceAdminVM.  # noqa: E501


        :return: The subscription_id of this CreateDataSourceAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this CreateDataSourceAdminVM.


        :param subscription_id: The subscription_id of this CreateDataSourceAdminVM.  # noqa: E501
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def connection_type(self):
        """Gets the connection_type of this CreateDataSourceAdminVM.  # noqa: E501


        :return: The connection_type of this CreateDataSourceAdminVM.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this CreateDataSourceAdminVM.


        :param connection_type: The connection_type of this CreateDataSourceAdminVM.  # noqa: E501
        :type connection_type: str
        """
        allowed_values = ["JSON", "MSSQL", "CSV", "XML", "MySQL", "Postgres"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and connection_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

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
        if not isinstance(other, CreateDataSourceAdminVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDataSourceAdminVM):
            return True

        return self.to_dict() != other.to_dict()
