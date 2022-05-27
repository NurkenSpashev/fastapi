from pydantic import BaseModel
from datetime import date
from typing import Optional
from decimal import Decimal
from enum import Enum


class OperationType(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class BaseOperation(BaseModel):
    date: date
    type: OperationType
    amount: Decimal
    description: Optional[str]

    class Config:
        orm_mode = True


class Operation(BaseOperation):
    id: int


class OperationCreate(BaseOperation):
    pass


class OperationUpdate(BaseOperation):
    pass
