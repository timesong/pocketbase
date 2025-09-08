from __future__ import annotations

from typing import Any

from pocketbase.models.collection import Collection
from pocketbase.services.utils.crud_service import CrudService


class CollectionService(CrudService[Collection]):
    def decode(self, data: dict[str, Any]) -> Collection:
        return Collection(data)

    def base_crud_path(self) -> str:
        return "/api/collections"

    def import_collections(
        self,
        collections: list[str],
        delete_missing: bool = False,
        query_params: dict[str, Any] = {},
    ) -> bool:
        """
        Imports the provided collections.

        If `delete_missing` is `True`, all local collections and schema fields,
        that are not present in the imported configuration, WILL BE DELETED
        (including their related records data)!
        """
        self.client.send(
            self.base_crud_path() + "/import",
            {
                "method": "PUT",
                "params": query_params,
                "body": {
                    "collections": collections,
                    "deleteMissing": delete_missing,
                },
            },
        )
        return True

    def list_collections(
        self,
        filter: str = "",
        sort: str = "",
        query_params: dict[str, Any] = {},
    ) -> list[Collection]:
        """
        获取集合列表，支持 filter 和 sort 参数。
        """
        params = query_params.copy()
        if filter:
            params["filter"] = filter
        if sort:
            params["sort"] = sort

        resp = self.client.send(
            self.base_crud_path(),
            {
                "method": "GET",
                "params": params,
            },
        )
        
        # 假设 resp["collections"] 是集合列表
        return [self.decode(item) for item in resp.get("items", [])]

    def create_collection(self, schema: dict, query_params: dict[str, Any] = {}) -> Collection:
        """
        创建一个新的集合。
        """
        resp = self.client.send(
            self.base_crud_path(),
            {
                "method": "POST",
                "params": query_params,
                "body": schema,
            },
        )
        return self.decode(resp)
