from fastapi import APIRouter

main_router = APIRouter()

@main_router.get("/", status_code=200)
async def root():
    return {"greeting": "Welcome to the coffee shop service! How may we help you?"}
