import fastapi.params
from fastapi import APIRouter, Depends
from fastapi_admin.depends import get_resources
from fastapi_admin.template import templates
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response
from starlette.status import HTTP_303_SEE_OTHER

from app.admin import admin_app

admin_router = APIRouter()


@admin_app.get('/')
async def home(request: Request, resources: fastapi.params.Depends = Depends(get_resources)) -> Response:
    if not request.cookies.get('access_token'):
        return RedirectResponse(
            url=request.app.admin_path + request.app.login_provider.login_path, status_code=HTTP_303_SEE_OTHER
        )
    return templates.TemplateResponse(
        templates.get_template('layout.html'),
        context={
            'request': request,
            'resources': resources,
            'resource_label': 'Klash',
            'page_pre_title': 'overview',
            'page_title': 'Klash Admin',
        },
    )
