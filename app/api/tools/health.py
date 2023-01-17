from fastapi import APIRouter

from app.core.config import get_app_settings

router = APIRouter()
settings = get_app_settings()


@router.get("/health", tags=["health"], description="Health")
async def health():
    return {
        'commit': settings.vcs_ref,
        'release': settings.release,
    }
