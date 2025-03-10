# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class FileSchemaTestClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
        
            @classmethod
            @property
            def file(cls) -> typing.Type['File']:
                return File
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
            
                    @classmethod
                    @property
                    def items(cls) -> typing.Type['File']:
                        return File
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['File'], typing.List['File']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'File':
                    return super().__getitem__(i)
            __annotations__ = {
                "file": file,
                "files": files,
            }
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["file"]) -> 'File': ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[schemas.AnyTypeSchema]: ...
    
    def __getitem__(self, name: typing.Union[typing.Literal["file", "files", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["file"]) -> typing.Union['File', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["files"]) -> typing.Union[MetaOapg.properties.files, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.AnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing.Literal["file", "files", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file: typing.Union['File', schemas.Unset] = schemas.unset,
        files: typing.Union[MetaOapg.properties.files, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FileSchemaTestClass':
        return super().__new__(
            cls,
            *args,
            file=file,
            files=files,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.file import File
