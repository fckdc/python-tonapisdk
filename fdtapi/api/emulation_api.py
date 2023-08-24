# coding: utf-8

"""
    REST api to TON blockchain explorer

    Provide access to indexed TON blockchain  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@tonkeeper.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from fdtapi.models.account_event import AccountEvent
from fdtapi.models.emulate_message_to_event_request import EmulateMessageToEventRequest
from fdtapi.models.event import Event
from fdtapi.models.message_consequences import MessageConsequences
from fdtapi.models.trace import Trace

from fdtapi.api_client import ApiClient
from fdtapi.api_response import ApiResponse
from fdtapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EmulationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def emulate_message_to_account_event(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], accept_language : Optional[StrictStr] = None, **kwargs) -> AccountEvent:  # noqa: E501
        """emulate_message_to_account_event  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_account_event(account_id, emulate_message_to_event_request, accept_language, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param accept_language:
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountEvent
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the emulate_message_to_account_event_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.emulate_message_to_account_event_with_http_info(account_id, emulate_message_to_event_request, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def emulate_message_to_account_event_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], accept_language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """emulate_message_to_account_event  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_account_event_with_http_info(account_id, emulate_message_to_event_request, accept_language, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param accept_language:
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccountEvent, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account_id',
            'emulate_message_to_event_request',
            'accept_language'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emulate_message_to_account_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account_id']:
            _path_params['account_id'] = _params['account_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['emulate_message_to_event_request'] is not None:
            _body_params = _params['emulate_message_to_event_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AccountEvent",
        }

        return self.api_client.call_api(
            '/v2/accounts/{account_id}/events/emulate', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def emulate_message_to_event(self, emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], accept_language : Optional[StrictStr] = None, **kwargs) -> Event:  # noqa: E501
        """emulate_message_to_event  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_event(emulate_message_to_event_request, accept_language, async_req=True)
        >>> result = thread.get()

        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param accept_language:
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Event
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the emulate_message_to_event_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.emulate_message_to_event_with_http_info(emulate_message_to_event_request, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def emulate_message_to_event_with_http_info(self, emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], accept_language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """emulate_message_to_event  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_event_with_http_info(emulate_message_to_event_request, accept_language, async_req=True)
        >>> result = thread.get()

        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param accept_language:
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Event, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'emulate_message_to_event_request',
            'accept_language'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emulate_message_to_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['emulate_message_to_event_request'] is not None:
            _body_params = _params['emulate_message_to_event_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Event",
        }

        return self.api_client.call_api(
            '/v2/events/emulate', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def emulate_message_to_trace(self, emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], **kwargs) -> Trace:  # noqa: E501
        """emulate_message_to_trace  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_trace(emulate_message_to_event_request, async_req=True)
        >>> result = thread.get()

        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Trace
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the emulate_message_to_trace_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.emulate_message_to_trace_with_http_info(emulate_message_to_event_request, **kwargs)  # noqa: E501

    @validate_arguments
    def emulate_message_to_trace_with_http_info(self, emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], **kwargs) -> ApiResponse:  # noqa: E501
        """emulate_message_to_trace  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_trace_with_http_info(emulate_message_to_event_request, async_req=True)
        >>> result = thread.get()

        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Trace, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'emulate_message_to_event_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emulate_message_to_trace" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['emulate_message_to_event_request'] is not None:
            _body_params = _params['emulate_message_to_event_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Trace",
        }

        return self.api_client.call_api(
            '/v2/traces/emulate', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def emulate_message_to_wallet(self, emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], accept_language : Optional[StrictStr] = None, **kwargs) -> MessageConsequences:  # noqa: E501
        """emulate_message_to_wallet  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_wallet(emulate_message_to_event_request, accept_language, async_req=True)
        >>> result = thread.get()

        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param accept_language:
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MessageConsequences
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the emulate_message_to_wallet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.emulate_message_to_wallet_with_http_info(emulate_message_to_event_request, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def emulate_message_to_wallet_with_http_info(self, emulate_message_to_event_request : Annotated[EmulateMessageToEventRequest, Field(..., description="bag-of-cells serialized to base64")], accept_language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """emulate_message_to_wallet  # noqa: E501

        Emulate sending message to blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.emulate_message_to_wallet_with_http_info(emulate_message_to_event_request, accept_language, async_req=True)
        >>> result = thread.get()

        :param emulate_message_to_event_request: bag-of-cells serialized to base64 (required)
        :type emulate_message_to_event_request: EmulateMessageToEventRequest
        :param accept_language:
        :type accept_language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MessageConsequences, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'emulate_message_to_event_request',
            'accept_language'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emulate_message_to_wallet" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['emulate_message_to_event_request'] is not None:
            _body_params = _params['emulate_message_to_event_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "MessageConsequences",
        }

        return self.api_client.call_api(
            '/v2/wallet/emulate', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))