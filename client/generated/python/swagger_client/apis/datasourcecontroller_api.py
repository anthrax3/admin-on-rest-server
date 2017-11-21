# coding: utf-8

"""
    DataHive RESTful APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DatasourcecontrollerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_data_source_using_post(self, data_source, **kwargs):
        """
        addDataSource
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_data_source_using_post(data_source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DataSource data_source: dataSource (required)
        :return: DataSource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_data_source_using_post_with_http_info(data_source, **kwargs)
        else:
            (data) = self.add_data_source_using_post_with_http_info(data_source, **kwargs)
            return data

    def add_data_source_using_post_with_http_info(self, data_source, **kwargs):
        """
        addDataSource
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_data_source_using_post_with_http_info(data_source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DataSource data_source: dataSource (required)
        :return: DataSource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_source']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_data_source_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_source' is set
        if ('data_source' not in params) or (params['data_source'] is None):
            raise ValueError("Missing the required parameter `data_source` when calling `add_data_source_using_post`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data_source' in params:
            body_params = params['data_source']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/datasource/_datasource', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DataSource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def edit_data_source_using_put(self, id, data_source, **kwargs):
        """
        editDataSource
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.edit_data_source_using_put(id, data_source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: id (required)
        :param DataSource data_source: dataSource (required)
        :return: DataSource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.edit_data_source_using_put_with_http_info(id, data_source, **kwargs)
        else:
            (data) = self.edit_data_source_using_put_with_http_info(id, data_source, **kwargs)
            return data

    def edit_data_source_using_put_with_http_info(self, id, data_source, **kwargs):
        """
        editDataSource
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.edit_data_source_using_put_with_http_info(id, data_source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: id (required)
        :param DataSource data_source: dataSource (required)
        :return: DataSource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data_source']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_data_source_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `edit_data_source_using_put`")
        # verify the required parameter 'data_source' is set
        if ('data_source' not in params) or (params['data_source'] is None):
            raise ValueError("Missing the required parameter `data_source` when calling `edit_data_source_using_put`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data_source' in params:
            body_params = params['data_source']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/datasource/_datasource/put/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DataSource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_role_using_get(self, datasource_id, **kwargs):
        """
        findRole
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_role_using_get(datasource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str datasource_id: datasourceId (required)
        :return: DataSource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_role_using_get_with_http_info(datasource_id, **kwargs)
        else:
            (data) = self.find_role_using_get_with_http_info(datasource_id, **kwargs)
            return data

    def find_role_using_get_with_http_info(self, datasource_id, **kwargs):
        """
        findRole
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_role_using_get_with_http_info(datasource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str datasource_id: datasourceId (required)
        :return: DataSource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_role_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datasource_id' is set
        if ('datasource_id' not in params) or (params['datasource_id'] is None):
            raise ValueError("Missing the required parameter `datasource_id` when calling `find_role_using_get`")


        collection_formats = {}

        path_params = {}
        if 'datasource_id' in params:
            path_params['datasourceId'] = params['datasource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/datasource/_datasource/{datasourceId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DataSource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_using_get(self, **kwargs):
        """
        list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[DataSource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_using_get_with_http_info(**kwargs)
        else:
            (data) = self.list_using_get_with_http_info(**kwargs)
            return data

    def list_using_get_with_http_info(self, **kwargs):
        """
        list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_using_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[DataSource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/datasource/_datasource', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[DataSource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)