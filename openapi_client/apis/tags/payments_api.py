# coding: utf-8

"""
    BVNK API Endpoints

    The BVNK API is designed to facilitate seamless and secure transactions including payments, channels, anddigital wallet transactions.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_v1_pay_summary.get import ApiV1PaySummaryGet
from openapi_client.paths.api_v1_pay_summary.post import ApiV1PaySummaryPost
from openapi_client.paths.api_v1_pay_uuid_summary.get import ApiV1PayUuidSummaryGet
from openapi_client.paths.api_v1_pay_validate.put import ApiV1PayValidatePut


class PaymentsApi(
    ApiV1PaySummaryGet,
    ApiV1PaySummaryPost,
    ApiV1PayUuidSummaryGet,
    ApiV1PayValidatePut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
