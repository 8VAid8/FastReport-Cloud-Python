# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fastreport_cloud_sdk.api_client import ApiClient
from fastreport_cloud_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SubscriptionUsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def subscription_users_add_user(self, subscription_id, user_id, **kwargs):  # noqa: E501
        """Add a user to the subscription,  the added users will be displayed in the list of users of the subscription,  and these users will also have an active subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_add_user(subscription_id, user_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param user_id: Idenitifier of user (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.subscription_users_add_user_with_http_info(subscription_id, user_id, **kwargs)  # noqa: E501

    def subscription_users_add_user_with_http_info(self, subscription_id, user_id, **kwargs):  # noqa: E501
        """Add a user to the subscription,  the added users will be displayed in the list of users of the subscription,  and these users will also have an active subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_add_user_with_http_info(subscription_id, user_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param user_id: Idenitifier of user (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'subscription_id',
            'user_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscription_users_add_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscription_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscription_id` when calling `subscription_users_add_user`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `subscription_users_add_user`")  # noqa: E501

        if self.api_client.client_side_validation and 'subscription_id' in local_var_params and not re.search(r'^[A-Fa-f0-9]{24}$', local_var_params['subscription_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `subscription_id` when calling `subscription_users_add_user`, must conform to the pattern `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscriptionId'] = local_var_params['subscription_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey', 'JWT']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/api/manage/v1/Subscriptions/{subscriptionId}/users/{userId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def subscription_users_get_users(self, subscription_id, **kwargs):  # noqa: E501
        """Returns all users of subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_get_users(subscription_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param skip: How many entities skip
        :type skip: int
        :param take: How many entities take
        :type take: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SubscriptionUsersVM
        """
        kwargs['_return_http_data_only'] = True
        return self.subscription_users_get_users_with_http_info(subscription_id, **kwargs)  # noqa: E501

    def subscription_users_get_users_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Returns all users of subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_get_users_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param skip: How many entities skip
        :type skip: int
        :param take: How many entities take
        :type take: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SubscriptionUsersVM, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'subscription_id',
            'skip',
            'take'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscription_users_get_users" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscription_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscription_id` when calling `subscription_users_get_users`")  # noqa: E501

        if self.api_client.client_side_validation and 'subscription_id' in local_var_params and not re.search(r'^[A-Fa-f0-9]{24}$', local_var_params['subscription_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `subscription_id` when calling `subscription_users_get_users`, must conform to the pattern `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscriptionId'] = local_var_params['subscription_id']  # noqa: E501

        query_params = []
        if 'skip' in local_var_params and local_var_params['skip'] is not None:  # noqa: E501
            query_params.append(('skip', local_var_params['skip']))  # noqa: E501
        if 'take' in local_var_params and local_var_params['take'] is not None:  # noqa: E501
            query_params.append(('take', local_var_params['take']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey', 'JWT']  # noqa: E501
        
        response_types_map = {
            200: "SubscriptionUsersVM",
            400: "ProblemDetails",
            403: "ProblemDetails",
            404: "ProblemDetails",
            500: None,
        }

        return self.api_client.call_api(
            '/api/manage/v1/Subscriptions/{subscriptionId}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def subscription_users_leave_subscripiton(self, subscription_id, **kwargs):  # noqa: E501
        """Allows user to leave subscription,.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_leave_subscripiton(subscription_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.subscription_users_leave_subscripiton_with_http_info(subscription_id, **kwargs)  # noqa: E501

    def subscription_users_leave_subscripiton_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Allows user to leave subscription,.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_leave_subscripiton_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'subscription_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscription_users_leave_subscripiton" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscription_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscription_id` when calling `subscription_users_leave_subscripiton`")  # noqa: E501

        if self.api_client.client_side_validation and 'subscription_id' in local_var_params and not re.search(r'^[A-Fa-f0-9]{24}$', local_var_params['subscription_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `subscription_id` when calling `subscription_users_leave_subscripiton`, must conform to the pattern `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscriptionId'] = local_var_params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey', 'JWT']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/api/manage/v1/Subscriptions/{subscriptionId}/leave', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def subscription_users_remove_user(self, subscription_id, user_id, **kwargs):  # noqa: E501
        """Delete a user from the subscription,  the added users will be displayed in the list of users of the subscription,  and these users will also have an active subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_remove_user(subscription_id, user_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param user_id: Idenitifier of user (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.subscription_users_remove_user_with_http_info(subscription_id, user_id, **kwargs)  # noqa: E501

    def subscription_users_remove_user_with_http_info(self, subscription_id, user_id, **kwargs):  # noqa: E501
        """Delete a user from the subscription,  the added users will be displayed in the list of users of the subscription,  and these users will also have an active subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.subscription_users_remove_user_with_http_info(subscription_id, user_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Idenitifier of subscription (required)
        :type subscription_id: str
        :param user_id: Idenitifier of user (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'subscription_id',
            'user_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscription_users_remove_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscription_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscription_id` when calling `subscription_users_remove_user`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `subscription_users_remove_user`")  # noqa: E501

        if self.api_client.client_side_validation and 'subscription_id' in local_var_params and not re.search(r'^[A-Fa-f0-9]{24}$', local_var_params['subscription_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `subscription_id` when calling `subscription_users_remove_user`, must conform to the pattern `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscriptionId'] = local_var_params['subscription_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey', 'JWT']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/api/manage/v1/Subscriptions/{subscriptionId}/users/{userId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
