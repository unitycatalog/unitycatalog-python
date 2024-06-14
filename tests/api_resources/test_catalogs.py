# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unitycatalog import Unitycatalog, AsyncUnitycatalog
from unitycatalog.types import (
    CatalogInfo,
    CatalogListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatalogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.create(
            name="string",
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.create(
            name="string",
            comment="string",
            properties={"foo": "string"},
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unitycatalog) -> None:
        response = client.catalogs.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unitycatalog) -> None:
        with client.catalogs.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(CatalogInfo, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.retrieve(
            "string",
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unitycatalog) -> None:
        response = client.catalogs.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unitycatalog) -> None:
        with client.catalogs.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(CatalogInfo, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.catalogs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.update(
            "string",
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.update(
            "string",
            comment="string",
            new_name="string",
            properties={"foo": "string"},
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Unitycatalog) -> None:
        response = client.catalogs.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Unitycatalog) -> None:
        with client.catalogs.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(CatalogInfo, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.catalogs.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.list()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.list(
            max_results=0,
            page_token="string",
        )
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unitycatalog) -> None:
        response = client.catalogs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unitycatalog) -> None:
        with client.catalogs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(CatalogListResponse, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.delete(
            "string",
        )
        assert_matches_type(object, catalog, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Unitycatalog) -> None:
        catalog = client.catalogs.delete(
            "string",
            force=True,
        )
        assert_matches_type(object, catalog, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Unitycatalog) -> None:
        response = client.catalogs.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(object, catalog, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Unitycatalog) -> None:
        with client.catalogs.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(object, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.catalogs.with_raw_response.delete(
                "",
            )


class TestAsyncCatalogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.create(
            name="string",
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.create(
            name="string",
            comment="string",
            properties={"foo": "string"},
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.catalogs.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.catalogs.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(CatalogInfo, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.retrieve(
            "string",
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.catalogs.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.catalogs.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(CatalogInfo, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.catalogs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.update(
            "string",
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.update(
            "string",
            comment="string",
            new_name="string",
            properties={"foo": "string"},
        )
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.catalogs.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(CatalogInfo, catalog, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.catalogs.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(CatalogInfo, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.catalogs.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.list()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.list(
            max_results=0,
            page_token="string",
        )
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.catalogs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.catalogs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(CatalogListResponse, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.delete(
            "string",
        )
        assert_matches_type(object, catalog, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncUnitycatalog) -> None:
        catalog = await async_client.catalogs.delete(
            "string",
            force=True,
        )
        assert_matches_type(object, catalog, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.catalogs.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(object, catalog, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.catalogs.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(object, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnitycatalog) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.catalogs.with_raw_response.delete(
                "",
            )
