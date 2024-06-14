# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unitycatalog import Unitycatalog, AsyncUnitycatalog
from unitycatalog.types import GenerateTemporaryTableCredentialResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemporaryTableCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unitycatalog) -> None:
        temporary_table_credential = client.temporary_table_credentials.create(
            operation="UNKNOWN_TABLE_OPERATION",
            table_id="table_id",
        )
        assert_matches_type(GenerateTemporaryTableCredentialResponse, temporary_table_credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unitycatalog) -> None:
        response = client.temporary_table_credentials.with_raw_response.create(
            operation="UNKNOWN_TABLE_OPERATION",
            table_id="table_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temporary_table_credential = response.parse()
        assert_matches_type(GenerateTemporaryTableCredentialResponse, temporary_table_credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unitycatalog) -> None:
        with client.temporary_table_credentials.with_streaming_response.create(
            operation="UNKNOWN_TABLE_OPERATION",
            table_id="table_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temporary_table_credential = response.parse()
            assert_matches_type(GenerateTemporaryTableCredentialResponse, temporary_table_credential, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemporaryTableCredentials:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnitycatalog) -> None:
        temporary_table_credential = await async_client.temporary_table_credentials.create(
            operation="UNKNOWN_TABLE_OPERATION",
            table_id="table_id",
        )
        assert_matches_type(GenerateTemporaryTableCredentialResponse, temporary_table_credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnitycatalog) -> None:
        response = await async_client.temporary_table_credentials.with_raw_response.create(
            operation="UNKNOWN_TABLE_OPERATION",
            table_id="table_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temporary_table_credential = await response.parse()
        assert_matches_type(GenerateTemporaryTableCredentialResponse, temporary_table_credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnitycatalog) -> None:
        async with async_client.temporary_table_credentials.with_streaming_response.create(
            operation="UNKNOWN_TABLE_OPERATION",
            table_id="table_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temporary_table_credential = await response.parse()
            assert_matches_type(GenerateTemporaryTableCredentialResponse, temporary_table_credential, path=["response"])

        assert cast(Any, response.is_closed) is True
