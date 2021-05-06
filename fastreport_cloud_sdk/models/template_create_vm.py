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


class TemplateCreateVM(object):
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
        'tags': 'list[str]',
        'icon': 'str',
        'content': 'str'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'icon': 'icon',
        'content': 'content'
    }

    def __init__(self, name=None, tags=None, icon=None, content=None, local_vars_configuration=None):  # noqa: E501
        """TemplateCreateVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._tags = None
        self._icon = None
        self._content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if icon is not None:
            self.icon = icon
        if content is not None:
            self.content = content

    @property
    def name(self):
        """Gets the name of this TemplateCreateVM.  # noqa: E501


        :return: The name of this TemplateCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateCreateVM.


        :param name: The name of this TemplateCreateVM.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this TemplateCreateVM.  # noqa: E501


        :return: The tags of this TemplateCreateVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TemplateCreateVM.


        :param tags: The tags of this TemplateCreateVM.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def icon(self):
        """Gets the icon of this TemplateCreateVM.  # noqa: E501


        :return: The icon of this TemplateCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this TemplateCreateVM.


        :param icon: The icon of this TemplateCreateVM.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def content(self):
        """Gets the content of this TemplateCreateVM.  # noqa: E501


        :return: The content of this TemplateCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TemplateCreateVM.


        :param content: The content of this TemplateCreateVM.  # noqa: E501
        :type content: str
        """

        self._content = content

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
        if not isinstance(other, TemplateCreateVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateCreateVM):
            return True

        return self.to_dict() != other.to_dict()
