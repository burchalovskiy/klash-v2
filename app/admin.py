import os

from fastapi_admin.app import app as admin_app
from fastapi_admin.constants import BASE_DIR
from fastapi_admin.exceptions import (
    forbidden_error_exception,
    not_found_error_exception,
    server_error_exception,
    unauthorized_error_exception,
)
from fastapi_admin.file_upload import FileUpload
from fastapi_admin.resources import Field, Model
from fastapi_admin.widgets import displays, filters, inputs
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.database.models import Admin

admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)

upload = FileUpload(uploads_dir=os.path.join(BASE_DIR, "static", "uploads"))


@admin_app.register
class AdminResource(Model):
    label = 'Admins'
    icon = 'fas fa-home'
    model = Admin
    filters = [
        filters.Search(name='username', label='Name', search_mode='contains', placeholder='Search for username'),
        filters.Date(name='created_at', label='CreatedAt'),
    ]
    fields = [
        'id',
        'username',
        Field(
            name='password',
            label='Password',
            display=displays.InputOnly(),
            input_=inputs.Password(),
        ),
        Field(name='email', label='Email', input_=inputs.Email()),
        'created_at',
        'last_login',
    ]
