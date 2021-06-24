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


class ReportCreateVM(object):
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
        'template_id': 'str',
        'report_info': 'ReportInfo',
        'name': 'str',
        'tags': 'list[str]',
        'icon': 'str',
        'content': 'str'
    }

    attribute_map = {
        'template_id': 'templateId',
        'report_info': 'reportInfo',
        'name': 'name',
        'tags': 'tags',
        'icon': 'icon',
        'content': 'content'
    }

    def __init__(self, template_id=None, report_info=None, name=None, tags=None, icon=None, content=None, local_vars_configuration=None):  # noqa: E501
        """ReportCreateVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._template_id = None
        self._report_info = None
        self._name = None
        self._tags = None
        self._icon = None
        self._content = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if report_info is not None:
            self.report_info = report_info
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if icon is not None:
            self.icon = icon
        if content is not None:
            self.content = content

    @property
    def template_id(self):
        """Gets the template_id of this ReportCreateVM.  # noqa: E501


        :return: The template_id of this ReportCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ReportCreateVM.


        :param template_id: The template_id of this ReportCreateVM.  # noqa: E501
        :type template_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                template_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', template_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `template_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._template_id = template_id

    @property
    def report_info(self):
        """Gets the report_info of this ReportCreateVM.  # noqa: E501


        :return: The report_info of this ReportCreateVM.  # noqa: E501
        :rtype: ReportInfo
        """
        return self._report_info

    @report_info.setter
    def report_info(self, report_info):
        """Sets the report_info of this ReportCreateVM.


        :param report_info: The report_info of this ReportCreateVM.  # noqa: E501
        :type report_info: ReportInfo
        """

        self._report_info = report_info

    @property
    def name(self):
        """Gets the name of this ReportCreateVM.  # noqa: E501


        :return: The name of this ReportCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportCreateVM.


        :param name: The name of this ReportCreateVM.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 250):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this ReportCreateVM.  # noqa: E501


        :return: The tags of this ReportCreateVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReportCreateVM.


        :param tags: The tags of this ReportCreateVM.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def icon(self):
        """Gets the icon of this ReportCreateVM.  # noqa: E501


        :return: The icon of this ReportCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ReportCreateVM.


        :param icon: The icon of this ReportCreateVM.  # noqa: E501
        :type icon: str
        """
        if (self.local_vars_configuration.client_side_validation and
                icon is not None and len(icon) > 65536):
            raise ValueError("Invalid value for `icon`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                icon is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', icon)):  # noqa: E501
            raise ValueError(r"Invalid value for `icon`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._icon = icon

    @property
    def content(self):
        """Gets the content of this ReportCreateVM.  # noqa: E501


        :return: The content of this ReportCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ReportCreateVM.


        :param content: The content of this ReportCreateVM.  # noqa: E501
        :type content: str
        """
        if (self.local_vars_configuration.client_side_validation and
                content is not None and len(content) > 1073741824):
            raise ValueError("Invalid value for `content`, length must be less than or equal to `1073741824`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                content is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', content)):  # noqa: E501
            raise ValueError(r"Invalid value for `content`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, ReportCreateVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportCreateVM):
            return True

        return self.to_dict() != other.to_dict()
