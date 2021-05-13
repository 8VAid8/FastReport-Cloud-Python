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


class ExportReportTaskVM(object):
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
        'file_name': 'str',
        'folder_id': 'str',
        'locale': 'str',
        'pages_count': 'int',
        'format': 'str',
        'export_parameters': 'dict(str, object)'
    }

    attribute_map = {
        'file_name': 'fileName',
        'folder_id': 'folderId',
        'locale': 'locale',
        'pages_count': 'pagesCount',
        'format': 'format',
        'export_parameters': 'exportParameters'
    }

    def __init__(self, file_name=None, folder_id=None, locale=None, pages_count=None, format=None, export_parameters=None, local_vars_configuration=None):  # noqa: E501
        """ExportReportTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file_name = None
        self._folder_id = None
        self._locale = None
        self._pages_count = None
        self._format = None
        self._export_parameters = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if folder_id is not None:
            self.folder_id = folder_id
        if locale is not None:
            self.locale = locale
        if pages_count is not None:
            self.pages_count = pages_count
        if format is not None:
            self.format = format
        if export_parameters is not None:
            self.export_parameters = export_parameters

    @property
    def file_name(self):
        """Gets the file_name of this ExportReportTaskVM.  # noqa: E501


        :return: The file_name of this ExportReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ExportReportTaskVM.


        :param file_name: The file_name of this ExportReportTaskVM.  # noqa: E501
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def folder_id(self):
        """Gets the folder_id of this ExportReportTaskVM.  # noqa: E501


        :return: The folder_id of this ExportReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this ExportReportTaskVM.


        :param folder_id: The folder_id of this ExportReportTaskVM.  # noqa: E501
        :type folder_id: str
        """

        self._folder_id = folder_id

    @property
    def locale(self):
        """Gets the locale of this ExportReportTaskVM.  # noqa: E501


        :return: The locale of this ExportReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ExportReportTaskVM.


        :param locale: The locale of this ExportReportTaskVM.  # noqa: E501
        :type locale: str
        """

        self._locale = locale

    @property
    def pages_count(self):
        """Gets the pages_count of this ExportReportTaskVM.  # noqa: E501


        :return: The pages_count of this ExportReportTaskVM.  # noqa: E501
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """Sets the pages_count of this ExportReportTaskVM.


        :param pages_count: The pages_count of this ExportReportTaskVM.  # noqa: E501
        :type pages_count: int
        """

        self._pages_count = pages_count

    @property
    def format(self):
        """Gets the format of this ExportReportTaskVM.  # noqa: E501


        :return: The format of this ExportReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ExportReportTaskVM.


        :param format: The format of this ExportReportTaskVM.  # noqa: E501
        :type format: str
        """
        allowed_values = ["Pdf", "Html", "Mht", "Image", "Biff8", "Csv", "Dbf", "Json", "LaTeX", "Odt", "Ods", "Docx", "Pptx", "Xlsx", "Xps", "Ppml", "PS", "Richtext", "Svg", "Text", "Xaml", "Xml", "Zpl"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def export_parameters(self):
        """Gets the export_parameters of this ExportReportTaskVM.  # noqa: E501


        :return: The export_parameters of this ExportReportTaskVM.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._export_parameters

    @export_parameters.setter
    def export_parameters(self, export_parameters):
        """Sets the export_parameters of this ExportReportTaskVM.


        :param export_parameters: The export_parameters of this ExportReportTaskVM.  # noqa: E501
        :type export_parameters: dict(str, object)
        """

        self._export_parameters = export_parameters

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
        if not isinstance(other, ExportReportTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportReportTaskVM):
            return True

        return self.to_dict() != other.to_dict()
