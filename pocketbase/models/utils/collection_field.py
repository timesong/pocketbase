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

    # Check required and allowed attributes for each field type on initialization
    def __post_init__(self):
        # Allowed attributes for each field type
        type_attr_map = {
            "text": {"primary_key", "auto_generate_pattern", "pattern", "min", "max"},
            "editor": {"maxSize"},
            "number": {"min", "max", "onlyInt"},
            "bool": set(),
            "date": {"min", "max"},
            "select": {"values", "maxSelect", "minSelect"},
            "json": {"maxSize"},
            "url": {"onlyDomains", "exceptDomains"},
            "email": {"onlyDomains"},
            "file": {"maxSize", "maxSelect", "mimeTypes", "protected", "thumbs"},
            "relation": {"collectionId", "cascadeDelete", "maxSelect", "minSelect"},
            "autodate": {"onCreate", "onUpdate"},
            "password": {"cost", "min"}
        }
        # Mapping from API attribute name to dataclass field name
        field_map = {
            "primaryKey": "primary_key",
            "autogeneratePattern": "auto_generate_pattern",
            "pattern": "pattern",
            "maxSize": "maxSize",
            "max": "max",
            "min": "min",
            "onlyDomains": "onlyDomains",
            "exceptDomains": "exceptDomains",
            "maxSelect": "maxSelect",
            "mimeTypes": "mimeTypes",
            "protected": "protected",
            "thumbs": "thumbs",
            "values": "values",
            "collectionId": "collectionId",
            "cascadeDelete": "cascadeDelete",
            "minSelect": "minSelect",
            "onCreate": "onCreate",
            "onUpdate": "onUpdate",
            "onlyInt": "onlyInt",
        }

        allowed = type_attr_map.get(self.type, set())
        # Check if any attribute is set but not allowed for the current type
        for _, attr in field_map.items():
            value = getattr(self, attr, None)
            if value not in (None, [], "", False) and attr not in allowed:
                raise ValueError(f"Attribute '{attr}' is not allowed for field type '{self.type}'")

        # Required attribute checks for select and relation types
        if self.type == "select" and not self.values:
            raise ValueError("'values' is required for field type 'select'")
        if self.type == "relation" and not self.collectionId:
            raise ValueError("'collectionId' is required for field type 'relation'")
