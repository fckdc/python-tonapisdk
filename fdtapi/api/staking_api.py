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

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from fdtapi.models.account_staking import AccountStaking
from fdtapi.models.get_staking_pool_history200_response import GetStakingPoolHistory200Response
from fdtapi.models.get_staking_pool_info200_response import GetStakingPoolInfo200Response
from fdtapi.models.get_staking_pools200_response import GetStakingPools200Response

from fdtapi.api_client import ApiClient
from fdtapi.api_response import ApiResponse
from fdtapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class StakingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_account_nominators_pools(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], **kwargs) -> AccountStaking:  # noqa: E501
        """get_account_nominators_pools  # noqa: E501

        All pools where account participates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_nominators_pools(account_id, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountStaking
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_account_nominators_pools_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_account_nominators_pools_with_http_info(account_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_account_nominators_pools_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_account_nominators_pools  # noqa: E501

        All pools where account participates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_nominators_pools_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
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
        :rtype: tuple(AccountStaking, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account_id'
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
                    " to method get_account_nominators_pools" % _key
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
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AccountStaking",
        }

        return self.api_client.call_api(
            '/v2/staking/nominator/{account_id}/pools', 'GET',
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
    def get_staking_pool_history(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], **kwargs) -> GetStakingPoolHistory200Response:  # noqa: E501
        """get_staking_pool_history  # noqa: E501

        Pool history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_staking_pool_history(account_id, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetStakingPoolHistory200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_staking_pool_history_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_staking_pool_history_with_http_info(account_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_staking_pool_history_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_staking_pool_history  # noqa: E501

        Pool history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_staking_pool_history_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
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
        :rtype: tuple(GetStakingPoolHistory200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account_id'
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
                    " to method get_staking_pool_history" % _key
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
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GetStakingPoolHistory200Response",
        }

        return self.api_client.call_api(
            '/v2/staking/pool/{account_id}/history', 'GET',
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
    def get_staking_pool_info(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], accept_language : Optional[StrictStr] = None, **kwargs) -> GetStakingPoolInfo200Response:  # noqa: E501
        """get_staking_pool_info  # noqa: E501

        Stacking pool info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_staking_pool_info(account_id, accept_language, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
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
        :rtype: GetStakingPoolInfo200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_staking_pool_info_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_staking_pool_info_with_http_info(account_id, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def get_staking_pool_info_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="account ID")], accept_language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_staking_pool_info  # noqa: E501

        Stacking pool info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_staking_pool_info_with_http_info(account_id, accept_language, async_req=True)
        >>> result = thread.get()

        :param account_id: account ID (required)
        :type account_id: str
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
        :rtype: tuple(GetStakingPoolInfo200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account_id',
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
                    " to method get_staking_pool_info" % _key
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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GetStakingPoolInfo200Response",
        }

        return self.api_client.call_api(
            '/v2/staking/pool/{account_id}', 'GET',
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
    def get_staking_pools(self, available_for : Annotated[Optional[StrictStr], Field(description="account ID")] = None, include_unverified : Annotated[Optional[StrictBool], Field(description="return also pools not from white list - just compatible by interfaces (maybe dangerous!)")] = None, accept_language : Optional[StrictStr] = None, **kwargs) -> GetStakingPools200Response:  # noqa: E501
        """get_staking_pools  # noqa: E501

        All pools available in network  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_staking_pools(available_for, include_unverified, accept_language, async_req=True)
        >>> result = thread.get()

        :param available_for: account ID
        :type available_for: str
        :param include_unverified: return also pools not from white list - just compatible by interfaces (maybe dangerous!)
        :type include_unverified: bool
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
        :rtype: GetStakingPools200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_staking_pools_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_staking_pools_with_http_info(available_for, include_unverified, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def get_staking_pools_with_http_info(self, available_for : Annotated[Optional[StrictStr], Field(description="account ID")] = None, include_unverified : Annotated[Optional[StrictBool], Field(description="return also pools not from white list - just compatible by interfaces (maybe dangerous!)")] = None, accept_language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_staking_pools  # noqa: E501

        All pools available in network  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_staking_pools_with_http_info(available_for, include_unverified, accept_language, async_req=True)
        >>> result = thread.get()

        :param available_for: account ID
        :type available_for: str
        :param include_unverified: return also pools not from white list - just compatible by interfaces (maybe dangerous!)
        :type include_unverified: bool
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
        :rtype: tuple(GetStakingPools200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'available_for',
            'include_unverified',
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
                    " to method get_staking_pools" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('available_for') is not None:  # noqa: E501
            _query_params.append(('available_for', _params['available_for']))

        if _params.get('include_unverified') is not None:  # noqa: E501
            _query_params.append(('include_unverified', _params['include_unverified']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GetStakingPools200Response",
        }

        return self.api_client.call_api(
            '/v2/staking/pools', 'GET',
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
