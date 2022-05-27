from fastapi import (
    APIRouter,
    Response,
    status,
    Depends
)
from typing import (
    List,
    Optional
)

from ..models.operations_model import (
    Operation,
    OperationType,
    OperationCreate,
    OperationUpdate
)
from ..services.operation_service import OperationService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(
        operation_type: Optional[OperationType] = None,
        service: OperationService = Depends()
):
    print(operation_type)
    return service.get_list(operation_type=operation_type)


@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate,
        service: OperationService = Depends()
):
    return service.create(operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get(
        operation_id: int,
        service: OperationService = Depends()
):
    return service.get(operation_id)


@router.put('/{operation_id}', response_model=Operation)
def get(
        operation_id: int,
        operation_data: OperationUpdate,
        service: OperationService = Depends()
):
    return service.update(operation_id=operation_id, operation_data=operation_data)


@router.delete('/{operation_id}')
def delete(
        operation_id: int,
        service: OperationService = Depends()
):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
