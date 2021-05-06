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


class ReportVM(object):
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
        'parent_id': 'str',
        'tags': 'list[str]',
        'icon': 'str',
        'type': 'str',
        'size': 'int',
        'subscription_id': 'str',
        'status': 'str',
        'status_reason': 'str',
        'id': 'str',
        'created_time': 'datetime',
        'creator_user_id': 'str',
        'edited_time': 'datetime',
        'editor_user_id': 'str'
    }

    attribute_map = {
        'template_id': 'templateId',
        'report_info': 'reportInfo',
        'name': 'name',
        'parent_id': 'parentId',
        'tags': 'tags',
        'icon': 'icon',
        'type': 'type',
        'size': 'size',
        'subscription_id': 'subscriptionId',
        'status': 'status',
        'status_reason': 'statusReason',
        'id': 'id',
        'created_time': 'createdTime',
        'creator_user_id': 'creatorUserId',
        'edited_time': 'editedTime',
        'editor_user_id': 'editorUserId'
    }

    def __init__(self, template_id=None, report_info=None, name=None, parent_id=None, tags=None, icon=None, type=None, size=None, subscription_id=None, status=None, status_reason=None, id=None, created_time=None, creator_user_id=None, edited_time=None, editor_user_id=None, local_vars_configuration=None):  # noqa: E501
        """ReportVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._template_id = None
        self._report_info = None
        self._name = None
        self._parent_id = None
        self._tags = None
        self._icon = None
        self._type = None
        self._size = None
        self._subscription_id = None
        self._status = None
        self._status_reason = None
        self._id = None
        self._created_time = None
        self._creator_user_id = None
        self._edited_time = None
        self._editor_user_id = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if report_info is not None:
            self.report_info = report_info
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if tags is not None:
            self.tags = tags
        if icon is not None:
            self.icon = icon
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if creator_user_id is not None:
            self.creator_user_id = creator_user_id
        if edited_time is not None:
            self.edited_time = edited_time
        if editor_user_id is not None:
            self.editor_user_id = editor_user_id

    @property
    def template_id(self):
        """Gets the template_id of this ReportVM.  # noqa: E501


        :return: The template_id of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ReportVM.


        :param template_id: The template_id of this ReportVM.  # noqa: E501
        :type template_id: str
        """

        self._template_id = template_id

    @property
    def report_info(self):
        """Gets the report_info of this ReportVM.  # noqa: E501


        :return: The report_info of this ReportVM.  # noqa: E501
        :rtype: ReportInfo
        """
        return self._report_info

    @report_info.setter
    def report_info(self, report_info):
        """Sets the report_info of this ReportVM.


        :param report_info: The report_info of this ReportVM.  # noqa: E501
        :type report_info: ReportInfo
        """

        self._report_info = report_info

    @property
    def name(self):
        """Gets the name of this ReportVM.  # noqa: E501


        :return: The name of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportVM.


        :param name: The name of this ReportVM.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this ReportVM.  # noqa: E501


        :return: The parent_id of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ReportVM.


        :param parent_id: The parent_id of this ReportVM.  # noqa: E501
        :type parent_id: str
        """

        self._parent_id = parent_id

    @property
    def tags(self):
        """Gets the tags of this ReportVM.  # noqa: E501


        :return: The tags of this ReportVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReportVM.


        :param tags: The tags of this ReportVM.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def icon(self):
        """Gets the icon of this ReportVM.  # noqa: E501


        :return: The icon of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ReportVM.


        :param icon: The icon of this ReportVM.  # noqa: E501
        :type icon: str
        """
        if (self.local_vars_configuration.client_side_validation and
                icon is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', icon)):  # noqa: E501
            raise ValueError(r"Invalid value for `icon`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._icon = icon

    @property
    def type(self):
        """Gets the type of this ReportVM.  # noqa: E501


        :return: The type of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportVM.


        :param type: The type of this ReportVM.  # noqa: E501
        :type type: str
        """
        allowed_values = ["File", "Folder"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def size(self):
        """Gets the size of this ReportVM.  # noqa: E501


        :return: The size of this ReportVM.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ReportVM.


        :param size: The size of this ReportVM.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ReportVM.  # noqa: E501


        :return: The subscription_id of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ReportVM.


        :param subscription_id: The subscription_id of this ReportVM.  # noqa: E501
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def status(self):
        """Gets the status of this ReportVM.  # noqa: E501


        :return: The status of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReportVM.


        :param status: The status of this ReportVM.  # noqa: E501
        :type status: str
        """
        allowed_values = ["None", "InQueue", "InProcess", "Success", "Failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this ReportVM.  # noqa: E501


        :return: The status_reason of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this ReportVM.


        :param status_reason: The status_reason of this ReportVM.  # noqa: E501
        :type status_reason: str
        """
        allowed_values = ["None", "AllRight", "Hang", "Error", "NotFound", "NotEnoughSpace", "ExportStarted", "PreparationStarted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status_reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(status_reason, allowed_values)
            )

        self._status_reason = status_reason

    @property
    def id(self):
        """Gets the id of this ReportVM.  # noqa: E501


        :return: The id of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportVM.


        :param id: The id of this ReportVM.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this ReportVM.  # noqa: E501


        :return: The created_time of this ReportVM.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ReportVM.


        :param created_time: The created_time of this ReportVM.  # noqa: E501
        :type created_time: datetime
        """

        self._created_time = created_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this ReportVM.  # noqa: E501


        :return: The creator_user_id of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this ReportVM.


        :param creator_user_id: The creator_user_id of this ReportVM.  # noqa: E501
        :type creator_user_id: str
        """

        self._creator_user_id = creator_user_id

    @property
    def edited_time(self):
        """Gets the edited_time of this ReportVM.  # noqa: E501


        :return: The edited_time of this ReportVM.  # noqa: E501
        :rtype: datetime
        """
        return self._edited_time

    @edited_time.setter
    def edited_time(self, edited_time):
        """Sets the edited_time of this ReportVM.


        :param edited_time: The edited_time of this ReportVM.  # noqa: E501
        :type edited_time: datetime
        """

        self._edited_time = edited_time

    @property
    def editor_user_id(self):
        """Gets the editor_user_id of this ReportVM.  # noqa: E501


        :return: The editor_user_id of this ReportVM.  # noqa: E501
        :rtype: str
        """
        return self._editor_user_id

    @editor_user_id.setter
    def editor_user_id(self, editor_user_id):
        """Sets the editor_user_id of this ReportVM.


        :param editor_user_id: The editor_user_id of this ReportVM.  # noqa: E501
        :type editor_user_id: str
        """

        self._editor_user_id = editor_user_id

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
        if not isinstance(other, ReportVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportVM):
            return True

        return self.to_dict() != other.to_dict()
