from fastapi import APIRouter

from app.api.tools import health

router = APIRouter()
router.include_router(health.router)
