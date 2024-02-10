from fastapi import APIRouter
from api.endpoints import drinks

api_router = APIRouter()
api_router.include_router(drinks.router, prefix="/drinks", tags=["drinks"])