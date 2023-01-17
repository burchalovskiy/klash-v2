from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.admin import admin_app
from app.api.api import router as api_router
from app.api.tools.admin import admin_router
from app.core.config import get_app_settings
from app.core.events import create_start_app_handler, create_stop_app_handler

settings = get_app_settings()
settings.configure_logging()

app = FastAPI(**settings.fastapi_kwargs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(api_router, prefix=settings.api_prefix)
app.add_event_handler(
    'startup',
    create_start_app_handler(app, settings),
)
app.add_event_handler(
    'shutdown',
    create_stop_app_handler(app),
)

admin_app.include_router(admin_router)
app.router.mount('/admin', admin_app)
