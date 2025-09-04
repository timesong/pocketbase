from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CollectionField:
    id: str = ""
    name: str = ""
    type: str = "text"
    system: bool = False
    required: bool = False
    presentable: bool = False
    unique: bool = False
    options: dict[str, Any] = field(default_factory=dict)
    hidden: bool = False
    max: int | None = None
    min: int | None = None
    pattern: str | None = None
    primary_key: bool = False
    auto_generate_pattern: str | None = None
    onCreate: bool = False
    onUpdate: bool = False
    cost: int | None = None
    exceptDomains: list[str] = field(default_factory=list)
    onlyDomains: list[str] = field(default_factory=list)
    maxSelect: int | None = None
    maxSize: int | None = None
    mimeTypes: list[str] = field(default_factory=list)
    protected: bool = False
    thumbs: list[str] | None = None
    convertURLs: bool = False
    onlyInt: bool = False
    values: list[str] = field(default_factory=list)
    cascadeDelete: bool = False
    collectionId: str | None = None
    minSelect: int | None = None
