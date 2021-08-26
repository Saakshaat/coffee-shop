from fastapi import APIRouter
from schemas import order as schemas

from functions import send_msg

order_router = APIRouter()


@order_router.get("/orders/{id_}", response_model=schemas.OrderGet, status_code=200)
async def get_order_status(id_: int):
    """
    Push a message for checking the current order status from the workers.
    Inform the user after getting a response.
    """
    return {"id": id_, "wait_time": 0, "type": "Coffee", "item": "Expresso"}


@order_router.post("/orders", response_model=schemas.OrderGet, status_code=202)
async def create_order(order: schemas.OrderPost):
    publish = send_msg.publish('Expresso - 75', 'new-order', 'order.coffee.make')
    return {"id": 43, "wait_time": 0, "type": order.type, "item": order.item}
