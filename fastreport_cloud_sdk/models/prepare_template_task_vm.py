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


class PrepareTemplateTaskVM(object):
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
        'locale': 'str',
        'parent_folder_id': 'str',
        'pages_count': 'int',
        'report_parameters': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'locale': 'locale',
        'parent_folder_id': 'parentFolderId',
        'pages_count': 'pagesCount',
        'report_parameters': 'reportParameters'
    }

    def __init__(self, name=None, locale=None, parent_folder_id=None, pages_count=None, report_parameters=None, local_vars_configuration=None):  # noqa: E501
        """PrepareTemplateTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._locale = None
        self._parent_folder_id = None
        self._pages_count = None
        self._report_parameters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if locale is not None:
            self.locale = locale
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if pages_count is not None:
            self.pages_count = pages_count
        if report_parameters is not None:
            self.report_parameters = report_parameters

    @property
    def name(self):
        """Gets the name of this PrepareTemplateTaskVM.  # noqa: E501


        :return: The name of this PrepareTemplateTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrepareTemplateTaskVM.


        :param name: The name of this PrepareTemplateTaskVM.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 250):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def locale(self):
        """Gets the locale of this PrepareTemplateTaskVM.  # noqa: E501


        :return: The locale of this PrepareTemplateTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PrepareTemplateTaskVM.


        :param locale: The locale of this PrepareTemplateTaskVM.  # noqa: E501
        :type locale: str
        """
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and not re.search(r'^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$', locale)):  # noqa: E501
            raise ValueError(r"Invalid value for `locale`, must be a follow pattern or equal to `/^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$/`")  # noqa: E501

        self._locale = locale

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this PrepareTemplateTaskVM.  # noqa: E501


        :return: The parent_folder_id of this PrepareTemplateTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this PrepareTemplateTaskVM.


        :param parent_folder_id: The parent_folder_id of this PrepareTemplateTaskVM.  # noqa: E501
        :type parent_folder_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                parent_folder_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', parent_folder_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `parent_folder_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._parent_folder_id = parent_folder_id

    @property
    def pages_count(self):
        """Gets the pages_count of this PrepareTemplateTaskVM.  # noqa: E501


        :return: The pages_count of this PrepareTemplateTaskVM.  # noqa: E501
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """Sets the pages_count of this PrepareTemplateTaskVM.


        :param pages_count: The pages_count of this PrepareTemplateTaskVM.  # noqa: E501
        :type pages_count: int
        """
        if (self.local_vars_configuration.client_side_validation and
                pages_count is not None and pages_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `pages_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pages_count is not None and pages_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `pages_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._pages_count = pages_count

    @property
    def report_parameters(self):
        """Gets the report_parameters of this PrepareTemplateTaskVM.  # noqa: E501


        :return: The report_parameters of this PrepareTemplateTaskVM.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._report_parameters

    @report_parameters.setter
    def report_parameters(self, report_parameters):
        """Sets the report_parameters of this PrepareTemplateTaskVM.


        :param report_parameters: The report_parameters of this PrepareTemplateTaskVM.  # noqa: E501
        :type report_parameters: dict(str, str)
        """

        self._report_parameters = report_parameters

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
        if not isinstance(other, PrepareTemplateTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrepareTemplateTaskVM):
            return True

        return self.to_dict() != other.to_dict()
