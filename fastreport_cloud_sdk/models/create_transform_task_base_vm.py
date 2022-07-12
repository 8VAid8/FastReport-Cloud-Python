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


class CreateTransformTaskBaseVM(object):
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
        'locale': 'str',
        'input_file': 'InputFileVM',
        'output_file': 'OutputFileVM',
        'transports': 'list[CreateTransportTaskBaseVM]',
        'name': 'str',
        'subscription_id': 'str',
        'type': 'TaskType',
        'delayed_run_time': 'datetime',
        'cron_expression': 'str'
    }

    attribute_map = {
        'locale': 'locale',
        'input_file': 'inputFile',
        'output_file': 'outputFile',
        'transports': 'transports',
        'name': 'name',
        'subscription_id': 'subscriptionId',
        'type': 'type',
        'delayed_run_time': 'delayedRunTime',
        'cron_expression': 'cronExpression'
    }

    def __init__(self, locale=None, input_file=None, output_file=None, transports=None, name=None, subscription_id=None, type=None, delayed_run_time=None, cron_expression=None, local_vars_configuration=None):  # noqa: E501
        """CreateTransformTaskBaseVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._locale = None
        self._input_file = None
        self._output_file = None
        self._transports = None
        self._name = None
        self._subscription_id = None
        self._type = None
        self._delayed_run_time = None
        self._cron_expression = None
        self.discriminator = None

        self.locale = locale
        if input_file is not None:
            self.input_file = input_file
        if output_file is not None:
            self.output_file = output_file
        self.transports = transports
        self.name = name
        self.subscription_id = subscription_id
        if type is not None:
            self.type = type
        self.delayed_run_time = delayed_run_time
        self.cron_expression = cron_expression

    @property
    def locale(self):
        """Gets the locale of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The locale of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateTransformTaskBaseVM.


        :param locale: The locale of this CreateTransformTaskBaseVM.  # noqa: E501
        :type locale: str
        """
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and not re.search(r'^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$', locale)):  # noqa: E501
            raise ValueError(r"Invalid value for `locale`, must be a follow pattern or equal to `/^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$/`")  # noqa: E501

        self._locale = locale

    @property
    def input_file(self):
        """Gets the input_file of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The input_file of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: InputFileVM
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        """Sets the input_file of this CreateTransformTaskBaseVM.


        :param input_file: The input_file of this CreateTransformTaskBaseVM.  # noqa: E501
        :type input_file: InputFileVM
        """

        self._input_file = input_file

    @property
    def output_file(self):
        """Gets the output_file of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The output_file of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: OutputFileVM
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        """Sets the output_file of this CreateTransformTaskBaseVM.


        :param output_file: The output_file of this CreateTransformTaskBaseVM.  # noqa: E501
        :type output_file: OutputFileVM
        """

        self._output_file = output_file

    @property
    def transports(self):
        """Gets the transports of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The transports of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: list[CreateTransportTaskBaseVM]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this CreateTransformTaskBaseVM.


        :param transports: The transports of this CreateTransformTaskBaseVM.  # noqa: E501
        :type transports: list[CreateTransportTaskBaseVM]
        """
        if (self.local_vars_configuration.client_side_validation and
                transports is not None and len(transports) > 10):
            raise ValueError("Invalid value for `transports`, number of items must be less than or equal to `10`")  # noqa: E501

        self._transports = transports

    @property
    def name(self):
        """Gets the name of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The name of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTransformTaskBaseVM.


        :param name: The name of this CreateTransformTaskBaseVM.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The subscription_id of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this CreateTransformTaskBaseVM.


        :param subscription_id: The subscription_id of this CreateTransformTaskBaseVM.  # noqa: E501
        :type subscription_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', subscription_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `subscription_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def type(self):
        """Gets the type of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The type of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateTransformTaskBaseVM.


        :param type: The type of this CreateTransformTaskBaseVM.  # noqa: E501
        :type type: TaskType
        """

        self._type = type

    @property
    def delayed_run_time(self):
        """Gets the delayed_run_time of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The delayed_run_time of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: datetime
        """
        return self._delayed_run_time

    @delayed_run_time.setter
    def delayed_run_time(self, delayed_run_time):
        """Sets the delayed_run_time of this CreateTransformTaskBaseVM.


        :param delayed_run_time: The delayed_run_time of this CreateTransformTaskBaseVM.  # noqa: E501
        :type delayed_run_time: datetime
        """

        self._delayed_run_time = delayed_run_time

    @property
    def cron_expression(self):
        """Gets the cron_expression of this CreateTransformTaskBaseVM.  # noqa: E501


        :return: The cron_expression of this CreateTransformTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this CreateTransformTaskBaseVM.


        :param cron_expression: The cron_expression of this CreateTransformTaskBaseVM.  # noqa: E501
        :type cron_expression: str
        """

        self._cron_expression = cron_expression

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
        if not isinstance(other, CreateTransformTaskBaseVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTransformTaskBaseVM):
            return True

        return self.to_dict() != other.to_dict()
