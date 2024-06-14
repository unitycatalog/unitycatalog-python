# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unitycatalog import Unitycatalog, AsyncUnitycatalog
from unitycatalog.types import FunctionInfo, FunctionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unitycatalog) -> None:
        function = client.functions.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {},
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "routine_body": "SQL",
                "routine_definition": "string",
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "properties": "string",
            },
        )
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unitycatalog) -> None:
        function = client.functions.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {
                    "parameters": [
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                    ]
                },
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "return_params": {
                    "parameters": [
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                    ]
                },
                "routine_body": "SQL",
                "routine_definition": "string",
                "routine_dependencies": {
                    "dependencies": [
                        {
                            "table": {"table_full_name": "string"},
                            "function": {"function_full_name": "string"},
                        },
                        {
                            "table": {"table_full_name": "string"},
                            "function": {"function_full_name": "string"},
                        },
                        {
                            "table": {"table_full_name": "string"},
                            "function": {"function_full_name": "string"},
                        },
                    ]
                },
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "comment": "string",
                "properties": "string",
                "external_language": "string",
            },
        )
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unitycatalog) -> None:
        response = client.functions.with_raw_response.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {},
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "routine_body": "SQL",
                "routine_definition": "string",
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "properties": "string",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unitycatalog) -> None:
        with client.functions.with_streaming_response.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {},
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "routine_body": "SQL",
                "routine_definition": "string",
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "properties": "string",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionInfo, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unitycatalog) -> None:
        function = client.functions.retrieve(
            "string",
        )
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unitycatalog) -> None:
        response = client.functions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unitycatalog) -> None:
        with client.functions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionInfo, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.functions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unitycatalog) -> None:
        function = client.functions.list(
            catalog_name="string",
            schema_name="string",
        )
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unitycatalog) -> None:
        function = client.functions.list(
            catalog_name="string",
            schema_name="string",
            max_results=0,
            page_token="string",
        )
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unitycatalog) -> None:
        response = client.functions.with_raw_response.list(
            catalog_name="string",
            schema_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unitycatalog) -> None:
        with client.functions.with_streaming_response.list(
            catalog_name="string",
            schema_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionListResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unitycatalog) -> None:
        function = client.functions.delete(
            "string",
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Unitycatalog) -> None:
        response = client.functions.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Unitycatalog) -> None:
        with client.functions.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(object, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.functions.with_raw_response.delete(
                "",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnitycatalog) -> None:
        function = await async_client.functions.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {},
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "routine_body": "SQL",
                "routine_definition": "string",
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "properties": "string",
            },
        )
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        function = await async_client.functions.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {
                    "parameters": [
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                    ]
                },
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "return_params": {
                    "parameters": [
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                        {
                            "name": "string",
                            "type_text": "string",
                            "type_json": "string",
                            "type_name": "BOOLEAN",
                            "type_precision": 0,
                            "type_scale": 0,
                            "type_interval_type": "string",
                            "position": 0,
                            "parameter_mode": "IN",
                            "parameter_type": "PARAM",
                            "parameter_default": "string",
                            "comment": "string",
                        },
                    ]
                },
                "routine_body": "SQL",
                "routine_definition": "string",
                "routine_dependencies": {
                    "dependencies": [
                        {
                            "table": {"table_full_name": "string"},
                            "function": {"function_full_name": "string"},
                        },
                        {
                            "table": {"table_full_name": "string"},
                            "function": {"function_full_name": "string"},
                        },
                        {
                            "table": {"table_full_name": "string"},
                            "function": {"function_full_name": "string"},
                        },
                    ]
                },
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "comment": "string",
                "properties": "string",
                "external_language": "string",
            },
        )
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {},
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "routine_body": "SQL",
                "routine_definition": "string",
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "properties": "string",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_info={
                "name": "string",
                "catalog_name": "string",
                "schema_name": "string",
                "input_params": {},
                "data_type": "BOOLEAN",
                "full_data_type": "string",
                "routine_body": "SQL",
                "routine_definition": "string",
                "parameter_style": "S",
                "is_deterministic": True,
                "sql_data_access": "CONTAINS_SQL",
                "is_null_call": True,
                "security_type": "DEFINER",
                "specific_name": "string",
                "properties": "string",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionInfo, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        function = await async_client.functions.retrieve(
            "string",
        )
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.functions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionInfo, function, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.functions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionInfo, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.functions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnitycatalog) -> None:
        function = await async_client.functions.list(
            catalog_name="string",
            schema_name="string",
        )
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        function = await async_client.functions.list(
            catalog_name="string",
            schema_name="string",
            max_results=0,
            page_token="string",
        )
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.functions.with_raw_response.list(
            catalog_name="string",
            schema_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionListResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.functions.with_streaming_response.list(
            catalog_name="string",
            schema_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionListResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnitycatalog) -> None:
        function = await async_client.functions.delete(
            "string",
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.functions.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.functions.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(object, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.functions.with_raw_response.delete(
                "",
            )
