from __future__ import annotations

import datetime
from abc import ABC
from typing import Any, Protocol

from pocketbase.utils import to_datetime


class Model(Protocol):
    id: str
    created: str | datetime.datetime
    updated: str | datetime.datetime

    def load(self, data: dict[str, Any]) -> None: ...

    @property
    def is_new(self) -> bool: ...


class BaseModel(ABC):
    id: str
    created: str | datetime.datetime
    updated: str | datetime.datetime

    def __init__(self, data: dict[str, Any] = {}) -> None:
        super().__init__()
        self.load(data)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}: {self.id}>"

    def __repr__(self) -> str:
        return self.__str__()

    def load(self, data: dict[str, Any]) -> None:
        """Loads `data` into the current model."""
        self.id = data.pop("id", "")
        self.created = to_datetime(data.pop("created", ""))
        self.updated = to_datetime(data.pop("updated", ""))
        
    def to_dict(self) -> dict[str, Any]:
        """Converts the current model to a dictionary."""
        return {
            "id": self.id,
            "created": self.created.isoformat() if isinstance(self.created, datetime.datetime) else self.created,
            "updated": self.updated.isoformat() if isinstance(self.updated, datetime.datetime) else self.updated,
        }

    @property
    def is_new(self) -> bool:
        """Returns whether the current loaded data represent a stored db record."""
        return not self.id
