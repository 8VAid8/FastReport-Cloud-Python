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


class SubscriptionVM(object):
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
        'id': 'str',
        'name': 'str',
        'locale': 'str',
        'current': 'SubscriptionPeriodVM',
        'old': 'list[SubscriptionPeriodVM]',
        'templates_folder': 'SubscriptionFolder',
        'reports_folder': 'SubscriptionFolder',
        'exports_folder': 'SubscriptionFolder'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'locale': 'locale',
        'current': 'current',
        'old': 'old',
        'templates_folder': 'templatesFolder',
        'reports_folder': 'reportsFolder',
        'exports_folder': 'exportsFolder'
    }

    def __init__(self, id=None, name=None, locale=None, current=None, old=None, templates_folder=None, reports_folder=None, exports_folder=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._locale = None
        self._current = None
        self._old = None
        self._templates_folder = None
        self._reports_folder = None
        self._exports_folder = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if locale is not None:
            self.locale = locale
        if current is not None:
            self.current = current
        if old is not None:
            self.old = old
        if templates_folder is not None:
            self.templates_folder = templates_folder
        if reports_folder is not None:
            self.reports_folder = reports_folder
        if exports_folder is not None:
            self.exports_folder = exports_folder

    @property
    def id(self):
        """Gets the id of this SubscriptionVM.  # noqa: E501


        :return: The id of this SubscriptionVM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionVM.


        :param id: The id of this SubscriptionVM.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionVM.  # noqa: E501


        :return: The name of this SubscriptionVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionVM.


        :param name: The name of this SubscriptionVM.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def locale(self):
        """Gets the locale of this SubscriptionVM.  # noqa: E501


        :return: The locale of this SubscriptionVM.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this SubscriptionVM.


        :param locale: The locale of this SubscriptionVM.  # noqa: E501
        :type locale: str
        """

        self._locale = locale

    @property
    def current(self):
        """Gets the current of this SubscriptionVM.  # noqa: E501


        :return: The current of this SubscriptionVM.  # noqa: E501
        :rtype: SubscriptionPeriodVM
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this SubscriptionVM.


        :param current: The current of this SubscriptionVM.  # noqa: E501
        :type current: SubscriptionPeriodVM
        """

        self._current = current

    @property
    def old(self):
        """Gets the old of this SubscriptionVM.  # noqa: E501


        :return: The old of this SubscriptionVM.  # noqa: E501
        :rtype: list[SubscriptionPeriodVM]
        """
        return self._old

    @old.setter
    def old(self, old):
        """Sets the old of this SubscriptionVM.


        :param old: The old of this SubscriptionVM.  # noqa: E501
        :type old: list[SubscriptionPeriodVM]
        """

        self._old = old

    @property
    def templates_folder(self):
        """Gets the templates_folder of this SubscriptionVM.  # noqa: E501


        :return: The templates_folder of this SubscriptionVM.  # noqa: E501
        :rtype: SubscriptionFolder
        """
        return self._templates_folder

    @templates_folder.setter
    def templates_folder(self, templates_folder):
        """Sets the templates_folder of this SubscriptionVM.


        :param templates_folder: The templates_folder of this SubscriptionVM.  # noqa: E501
        :type templates_folder: SubscriptionFolder
        """

        self._templates_folder = templates_folder

    @property
    def reports_folder(self):
        """Gets the reports_folder of this SubscriptionVM.  # noqa: E501


        :return: The reports_folder of this SubscriptionVM.  # noqa: E501
        :rtype: SubscriptionFolder
        """
        return self._reports_folder

    @reports_folder.setter
    def reports_folder(self, reports_folder):
        """Sets the reports_folder of this SubscriptionVM.


        :param reports_folder: The reports_folder of this SubscriptionVM.  # noqa: E501
        :type reports_folder: SubscriptionFolder
        """

        self._reports_folder = reports_folder

    @property
    def exports_folder(self):
        """Gets the exports_folder of this SubscriptionVM.  # noqa: E501


        :return: The exports_folder of this SubscriptionVM.  # noqa: E501
        :rtype: SubscriptionFolder
        """
        return self._exports_folder

    @exports_folder.setter
    def exports_folder(self, exports_folder):
        """Sets the exports_folder of this SubscriptionVM.


        :param exports_folder: The exports_folder of this SubscriptionVM.  # noqa: E501
        :type exports_folder: SubscriptionFolder
        """

        self._exports_folder = exports_folder

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
        if not isinstance(other, SubscriptionVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionVM):
            return True

        return self.to_dict() != other.to_dict()
