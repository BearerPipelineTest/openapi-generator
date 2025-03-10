# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from petstore_api.model.api_response import ApiResponse

# path params
PetIdSchema = schemas.Int64Schema
# body param


class SchemaForRequestBodyMultipartFormData(
    schemas.DictSchema
):


    class MetaOapg:
        class properties:
            additionalMetadata = schemas.StrSchema
            file = schemas.BinarySchema
            __annotations__ = {
                "additionalMetadata": additionalMetadata,
                "file": file,
            }
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["additionalMetadata"]) -> MetaOapg.properties.additionalMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[schemas.AnyTypeSchema]: ...
    
    def __getitem__(self, name: typing.Union[typing.Literal["additionalMetadata", "file", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["additionalMetadata"]) -> typing.Union[MetaOapg.properties.additionalMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["file"]) -> typing.Union[MetaOapg.properties.file, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.AnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing.Literal["additionalMetadata", "file", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        additionalMetadata: typing.Union[MetaOapg.properties.additionalMetadata, str, schemas.Unset] = schemas.unset,
        file: typing.Union[MetaOapg.properties.file, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyMultipartFormData':
        return super().__new__(
            cls,
            *args,
            additionalMetadata=additionalMetadata,
            file=file,
            _configuration=_configuration,
            **kwargs,
        )
SchemaFor200ResponseBodyApplicationJson = ApiResponse
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _upload_image_oapg(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        content_type: str = 'multipart/form-data',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        uploads an image
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_pet_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class UploadImage(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def upload_image(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        content_type: str = 'multipart/form-data',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._upload_image_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        content_type: str = 'multipart/form-data',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._upload_image_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


