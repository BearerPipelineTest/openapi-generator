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


class TriangleInterface(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "shapeType",
            "triangleType",
        }
        class properties:
            
            
            class shapeType(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "Triangle": "TRIANGLE",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def TRIANGLE(cls):
                    return cls("Triangle")
            triangleType = schemas.StrSchema
            __annotations__ = {
                "shapeType": shapeType,
                "triangleType": triangleType,
            }

    
    shapeType: MetaOapg.properties.shapeType
    triangleType: MetaOapg.properties.triangleType
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["shapeType"]) -> MetaOapg.properties.shapeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["triangleType"]) -> MetaOapg.properties.triangleType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[schemas.AnyTypeSchema]: ...
    
    def __getitem__(self, name: typing.Union[typing.Literal["shapeType", "triangleType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["shapeType"]) -> MetaOapg.properties.shapeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing.Literal["triangleType"]) -> MetaOapg.properties.triangleType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.AnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing.Literal["shapeType", "triangleType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        shapeType: typing.Union[MetaOapg.properties.shapeType, str, ],
        triangleType: typing.Union[MetaOapg.properties.triangleType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TriangleInterface':
        return super().__new__(
            cls,
            *args,
            shapeType=shapeType,
            triangleType=triangleType,
            _configuration=_configuration,
            **kwargs,
        )
