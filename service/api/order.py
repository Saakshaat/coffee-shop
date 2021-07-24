from fastapi import APIRouter
from schemas import order as schemas

order_router = APIRouter()


@order_router.get("/order/{id_}", response_model=schemas.OrderGet, status_code=200)
async def get_order_status(id_: int):
    """
    Push a message for checking the current order status from the workers.
    Inform the user after getting a response.
    """
    return {"id": id_, "wait_time": 0}


@order_router.post("/order", response_model=schemas.OrderGet, status_code=202)
async def create_order(order: schemas.OrderPost):
    return {"id": 43, "wait_time": 0}
