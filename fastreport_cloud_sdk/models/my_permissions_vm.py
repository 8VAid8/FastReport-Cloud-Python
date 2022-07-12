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


class MyPermissionsVM(object):
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
        'subscription': 'SubscriptionPermission',
        'files': 'FilePermission',
        'datasources': 'DataSourcePermission',
        'groups': 'GroupPermission',
        'tasks': 'TaskPermission'
    }

    attribute_map = {
        'subscription': 'subscription',
        'files': 'files',
        'datasources': 'datasources',
        'groups': 'groups',
        'tasks': 'tasks'
    }

    def __init__(self, subscription=None, files=None, datasources=None, groups=None, tasks=None, local_vars_configuration=None):  # noqa: E501
        """MyPermissionsVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._subscription = None
        self._files = None
        self._datasources = None
        self._groups = None
        self._tasks = None
        self.discriminator = None

        if subscription is not None:
            self.subscription = subscription
        if files is not None:
            self.files = files
        if datasources is not None:
            self.datasources = datasources
        if groups is not None:
            self.groups = groups
        if tasks is not None:
            self.tasks = tasks

    @property
    def subscription(self):
        """Gets the subscription of this MyPermissionsVM.  # noqa: E501


        :return: The subscription of this MyPermissionsVM.  # noqa: E501
        :rtype: SubscriptionPermission
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this MyPermissionsVM.


        :param subscription: The subscription of this MyPermissionsVM.  # noqa: E501
        :type subscription: SubscriptionPermission
        """

        self._subscription = subscription

    @property
    def files(self):
        """Gets the files of this MyPermissionsVM.  # noqa: E501


        :return: The files of this MyPermissionsVM.  # noqa: E501
        :rtype: FilePermission
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this MyPermissionsVM.


        :param files: The files of this MyPermissionsVM.  # noqa: E501
        :type files: FilePermission
        """

        self._files = files

    @property
    def datasources(self):
        """Gets the datasources of this MyPermissionsVM.  # noqa: E501


        :return: The datasources of this MyPermissionsVM.  # noqa: E501
        :rtype: DataSourcePermission
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """Sets the datasources of this MyPermissionsVM.


        :param datasources: The datasources of this MyPermissionsVM.  # noqa: E501
        :type datasources: DataSourcePermission
        """

        self._datasources = datasources

    @property
    def groups(self):
        """Gets the groups of this MyPermissionsVM.  # noqa: E501


        :return: The groups of this MyPermissionsVM.  # noqa: E501
        :rtype: GroupPermission
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this MyPermissionsVM.


        :param groups: The groups of this MyPermissionsVM.  # noqa: E501
        :type groups: GroupPermission
        """

        self._groups = groups

    @property
    def tasks(self):
        """Gets the tasks of this MyPermissionsVM.  # noqa: E501


        :return: The tasks of this MyPermissionsVM.  # noqa: E501
        :rtype: TaskPermission
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this MyPermissionsVM.


        :param tasks: The tasks of this MyPermissionsVM.  # noqa: E501
        :type tasks: TaskPermission
        """

        self._tasks = tasks

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
        if not isinstance(other, MyPermissionsVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MyPermissionsVM):
            return True

        return self.to_dict() != other.to_dict()
