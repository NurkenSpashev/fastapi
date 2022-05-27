from fastapi import (
    Depends,
    HTTPException,
    status
)

from typing import (
    List,
    Optional
)

from .. import tables
from ..database import Session, get_session
from ..models.operations_model import (
    OperationCreate,
    OperationType,
    OperationUpdate
)


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, operation_type: Optional[OperationType] = None) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if operation_type:
            query = query.filter_by(type=operation_type)
        return query.all()

    def _get(self, operation_id: int) -> tables.Operation:
        operation = self.session.query(tables.Operation).filter_by(id=operation_id).first()
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def get(self, operation_id: int) -> tables.Operation:
        return self._get(operation_id)

    def create(self, operation_type: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_type.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdate) -> tables.Operation:
        operation = self._get(operation_id)
        for field, value in operation_data:
            print(field, value)
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        operation = self._get(operation_id)
        self.session.delete(operation)
        self.session.commit()
