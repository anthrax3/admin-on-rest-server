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


class DatacontrollerApi(object):
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

    def data_mutation_using_delete(self, entity, id, **kwargs):
        """
        dataMutation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_mutation_using_delete(entity, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param str id: id (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.data_mutation_using_delete_with_http_info(entity, id, **kwargs)
        else:
            (data) = self.data_mutation_using_delete_with_http_info(entity, id, **kwargs)
            return data

    def data_mutation_using_delete_with_http_info(self, entity, id, **kwargs):
        """
        dataMutation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_mutation_using_delete_with_http_info(entity, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param str id: id (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_mutation_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params) or (params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `data_mutation_using_delete`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `data_mutation_using_delete`")


        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/api/{entity}/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='dict(str, object)',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def data_mutation_using_post(self, entity, all_request_params, **kwargs):
        """
        dataMutation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_mutation_using_post(entity, all_request_params, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param object all_request_params: allRequestParams (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.data_mutation_using_post_with_http_info(entity, all_request_params, **kwargs)
        else:
            (data) = self.data_mutation_using_post_with_http_info(entity, all_request_params, **kwargs)
            return data

    def data_mutation_using_post_with_http_info(self, entity, all_request_params, **kwargs):
        """
        dataMutation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_mutation_using_post_with_http_info(entity, all_request_params, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param object all_request_params: allRequestParams (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'all_request_params']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_mutation_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params) or (params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `data_mutation_using_post`")
        # verify the required parameter 'all_request_params' is set
        if ('all_request_params' not in params) or (params['all_request_params'] is None):
            raise ValueError("Missing the required parameter `all_request_params` when calling `data_mutation_using_post`")


        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'all_request_params' in params:
            body_params = params['all_request_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/{entity}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='dict(str, object)',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def data_mutation_using_put(self, entity, id, all_request_params, **kwargs):
        """
        dataMutation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_mutation_using_put(entity, id, all_request_params, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param str id: id (required)
        :param object all_request_params: allRequestParams (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.data_mutation_using_put_with_http_info(entity, id, all_request_params, **kwargs)
        else:
            (data) = self.data_mutation_using_put_with_http_info(entity, id, all_request_params, **kwargs)
            return data

    def data_mutation_using_put_with_http_info(self, entity, id, all_request_params, **kwargs):
        """
        dataMutation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_mutation_using_put_with_http_info(entity, id, all_request_params, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param str id: id (required)
        :param object all_request_params: allRequestParams (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'id', 'all_request_params']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_mutation_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params) or (params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `data_mutation_using_put`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `data_mutation_using_put`")
        # verify the required parameter 'all_request_params' is set
        if ('all_request_params' not in params) or (params['all_request_params'] is None):
            raise ValueError("Missing the required parameter `all_request_params` when calling `data_mutation_using_put`")


        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'all_request_params' in params:
            body_params = params['all_request_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/{entity}/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='dict(str, object)',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def data_query_using_get(self, entity, **kwargs):
        """
        dataQuery
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_query_using_get(entity, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.data_query_using_get_with_http_info(entity, **kwargs)
        else:
            (data) = self.data_query_using_get_with_http_info(entity, **kwargs)
            return data

    def data_query_using_get_with_http_info(self, entity, **kwargs):
        """
        dataQuery
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.data_query_using_get_with_http_info(entity, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_query_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params) or (params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `data_query_using_get`")


        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']

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

        return self.api_client.call_api('/api/{entity}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='dict(str, object)',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_one_using_get(self, entity, id, **kwargs):
        """
        findOne
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_one_using_get(entity, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param str id: id (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_one_using_get_with_http_info(entity, id, **kwargs)
        else:
            (data) = self.find_one_using_get_with_http_info(entity, id, **kwargs)
            return data

    def find_one_using_get_with_http_info(self, entity, id, **kwargs):
        """
        findOne
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_one_using_get_with_http_info(entity, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity: entity (required)
        :param str id: id (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_one_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params) or (params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `find_one_using_get`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `find_one_using_get`")


        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/api/{entity}/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='dict(str, object)',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)