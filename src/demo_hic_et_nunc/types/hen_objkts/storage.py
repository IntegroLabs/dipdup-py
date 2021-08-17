# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Extra


class Key(BaseModel):
    class Config:
        extra = Extra.forbid

    address: str
    nat: str


class LedgerItem(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Key
    value: str


class Key1(BaseModel):
    class Config:
        extra = Extra.forbid

    operator: str
    owner: str
    token_id: str


class Operator(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Key1
    value: Dict[str, Any]


class TokenMetadata(BaseModel):
    class Config:
        extra = Extra.forbid

    token_id: str
    token_info: Dict[str, str]


class HenObjktsStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    administrator: str
    all_tokens: str
    ledger: List[LedgerItem]
    metadata: Dict[str, str]
    operators: List[Operator]
    paused: bool
    token_metadata: Dict[str, TokenMetadata]
