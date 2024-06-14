# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unitycatalog import Unitycatalog, AsyncUnitycatalog
from unitycatalog.types import TableInfo, TableListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unitycatalog) -> None:
        table = client.tables.create(
            catalog_name="string",
            columns=[{}, {}, {}],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
        )
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unitycatalog) -> None:
        table = client.tables.create(
            catalog_name="string",
            columns=[
                {
                    "name": "string",
                    "type_text": "string",
                    "type_json": "string",
                    "type_name": "BOOLEAN",
                    "type_precision": 0,
                    "type_scale": 0,
                    "type_interval_type": "string",
                    "position": 0,
                    "comment": "string",
                    "nullable": True,
                    "partition_index": 0,
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
                    "comment": "string",
                    "nullable": True,
                    "partition_index": 0,
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
                    "comment": "string",
                    "nullable": True,
                    "partition_index": 0,
                },
            ],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
            comment="string",
            properties={"foo": "string"},
            storage_location="string",
        )
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unitycatalog) -> None:
        response = client.tables.with_raw_response.create(
            catalog_name="string",
            columns=[{}, {}, {}],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unitycatalog) -> None:
        with client.tables.with_streaming_response.create(
            catalog_name="string",
            columns=[{}, {}, {}],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableInfo, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unitycatalog) -> None:
        table = client.tables.retrieve(
            "string",
        )
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unitycatalog) -> None:
        response = client.tables.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unitycatalog) -> None:
        with client.tables.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableInfo, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            client.tables.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unitycatalog) -> None:
        table = client.tables.list(
            catalog_name="string",
            schema_name="string",
        )
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unitycatalog) -> None:
        table = client.tables.list(
            catalog_name="string",
            schema_name="string",
            max_results=0,
            page_token="string",
        )
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unitycatalog) -> None:
        response = client.tables.with_raw_response.list(
            catalog_name="string",
            schema_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unitycatalog) -> None:
        with client.tables.with_streaming_response.list(
            catalog_name="string",
            schema_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableListResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unitycatalog) -> None:
        table = client.tables.delete(
            "string",
        )
        assert_matches_type(object, table, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Unitycatalog) -> None:
        response = client.tables.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(object, table, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Unitycatalog) -> None:
        with client.tables.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(object, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            client.tables.with_raw_response.delete(
                "",
            )


class TestAsyncTables:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnitycatalog) -> None:
        table = await async_client.tables.create(
            catalog_name="string",
            columns=[{}, {}, {}],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
        )
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        table = await async_client.tables.create(
            catalog_name="string",
            columns=[
                {
                    "name": "string",
                    "type_text": "string",
                    "type_json": "string",
                    "type_name": "BOOLEAN",
                    "type_precision": 0,
                    "type_scale": 0,
                    "type_interval_type": "string",
                    "position": 0,
                    "comment": "string",
                    "nullable": True,
                    "partition_index": 0,
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
                    "comment": "string",
                    "nullable": True,
                    "partition_index": 0,
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
                    "comment": "string",
                    "nullable": True,
                    "partition_index": 0,
                },
            ],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
            comment="string",
            properties={"foo": "string"},
            storage_location="string",
        )
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.tables.with_raw_response.create(
            catalog_name="string",
            columns=[{}, {}, {}],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.tables.with_streaming_response.create(
            catalog_name="string",
            columns=[{}, {}, {}],
            data_source_format="DELTA",
            name="string",
            schema_name="string",
            table_type="MANAGED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableInfo, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        table = await async_client.tables.retrieve(
            "string",
        )
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.tables.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableInfo, table, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.tables.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableInfo, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            await async_client.tables.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnitycatalog) -> None:
        table = await async_client.tables.list(
            catalog_name="string",
            schema_name="string",
        )
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        table = await async_client.tables.list(
            catalog_name="string",
            schema_name="string",
            max_results=0,
            page_token="string",
        )
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.tables.with_raw_response.list(
            catalog_name="string",
            schema_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.tables.with_streaming_response.list(
            catalog_name="string",
            schema_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableListResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnitycatalog) -> None:
        table = await async_client.tables.delete(
            "string",
        )
        assert_matches_type(object, table, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.tables.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(object, table, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.tables.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(object, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            await async_client.tables.with_raw_response.delete(
                "",
            )
