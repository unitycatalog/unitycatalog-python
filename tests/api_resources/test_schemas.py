# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unitycatalog import Unitycatalog, AsyncUnitycatalog
from unitycatalog.types import (
    SchemaInfo,
    SchemaListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unitycatalog) -> None:
        schema = client.schemas.create(
            catalog_name="string",
            name="string",
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unitycatalog) -> None:
        schema = client.schemas.create(
            catalog_name="string",
            name="string",
            comment="string",
            properties={"foo": "string"},
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unitycatalog) -> None:
        response = client.schemas.with_raw_response.create(
            catalog_name="string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unitycatalog) -> None:
        with client.schemas.with_streaming_response.create(
            catalog_name="string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaInfo, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unitycatalog) -> None:
        schema = client.schemas.retrieve(
            "string",
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unitycatalog) -> None:
        response = client.schemas.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unitycatalog) -> None:
        with client.schemas.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaInfo, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            client.schemas.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unitycatalog) -> None:
        schema = client.schemas.update(
            "string",
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Unitycatalog) -> None:
        schema = client.schemas.update(
            "string",
            comment="string",
            new_name="string",
            properties={"foo": "string"},
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Unitycatalog) -> None:
        response = client.schemas.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Unitycatalog) -> None:
        with client.schemas.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaInfo, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            client.schemas.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unitycatalog) -> None:
        schema = client.schemas.list(
            catalog_name="string",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unitycatalog) -> None:
        schema = client.schemas.list(
            catalog_name="string",
            max_results=0,
            page_token="string",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unitycatalog) -> None:
        response = client.schemas.with_raw_response.list(
            catalog_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unitycatalog) -> None:
        with client.schemas.with_streaming_response.list(
            catalog_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unitycatalog) -> None:
        schema = client.schemas.delete(
            "string",
        )
        assert_matches_type(object, schema, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Unitycatalog) -> None:
        response = client.schemas.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(object, schema, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Unitycatalog) -> None:
        with client.schemas.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(object, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            client.schemas.with_raw_response.delete(
                "",
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.create(
            catalog_name="string",
            name="string",
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.create(
            catalog_name="string",
            name="string",
            comment="string",
            properties={"foo": "string"},
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.schemas.with_raw_response.create(
            catalog_name="string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.schemas.with_streaming_response.create(
            catalog_name="string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaInfo, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.retrieve(
            "string",
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.schemas.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.schemas.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaInfo, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            await async_client.schemas.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.update(
            "string",
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.update(
            "string",
            comment="string",
            new_name="string",
            properties={"foo": "string"},
        )
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.schemas.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaInfo, schema, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.schemas.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaInfo, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            await async_client.schemas.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.list(
            catalog_name="string",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.list(
            catalog_name="string",
            max_results=0,
            page_token="string",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.schemas.with_raw_response.list(
            catalog_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.schemas.with_streaming_response.list(
            catalog_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnitycatalog) -> None:
        schema = await async_client.schemas.delete(
            "string",
        )
        assert_matches_type(object, schema, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.schemas.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(object, schema, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.schemas.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(object, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `full_name` but received ''"):
            await async_client.schemas.with_raw_response.delete(
                "",
            )
