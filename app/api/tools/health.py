from fastapi import APIRouter

from app.core.config import get_app_settings
from app.services.instagram.tasks import task_save_instagram_post

router = APIRouter()
settings = get_app_settings()


@router.get("/health", tags=["health"], description="Health")
async def health():
    await task_save_instagram_post()

    return {
        'commit': settings.vcs_ref,
        'release': settings.release,
    }
