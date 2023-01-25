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

from app.database.models import Admin, Account, CrossPost, SocialPost
from app.services.constants import SocialNetwork

admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)

upload = FileUpload(uploads_dir=os.path.join(BASE_DIR, "static", "uploads"))


# icon
# https://fontawesomeicons.com/

@admin_app.register
class AdminResource(Model):
    label = 'Admins'
    icon = 'fas fa-home'
    model = Admin
    filters = [
        filters.Search(name='username', label='Name', search_mode='contains', placeholder='Search for username'),
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
        'last_login',
    ]


@admin_app.register
class AccountResource(Model):
    label = 'Accounts'
    icon = 'fa fa-address-book'
    model = Account
    filters = [
        filters.Search(name='title', label='Title', search_mode='contains', placeholder='Search for title'),
        filters.Search(name='login', label='Login', search_mode='contains', placeholder='Search for login'),
    ]
    fields = [
        'id',
        'type',
        'title',
        'login',
        Field(
            name='hashed_password',
            label='Password',
            display=displays.InputOnly(),
            input_=inputs.Password(),
        ),
        'token',
        Field(
            name='user',
            label='User',
            display=displays.Display(),
            input_=inputs.ForeignKey(Admin),
        )
    ]


@admin_app.register
class CrossPostResource(Model):
    label = 'Sent posts'
    icon = 'fa fa-at'
    model = CrossPost
    filters = [
        filters.Datetime(name='send_date', label='Date', placeholder='Search by date')
    ]
    fields = [
        'id',
        'post',
        Field(name='is_send', label='Is sent?', display=displays.Boolean(), input_=inputs.Switch()),
        Field(name='send_date', label='Time', display=displays.DatetimeDisplay(), input_=inputs.DateTime())
    ]


@admin_app.register
class SocialPostResource(Model):
    label = 'Scrab posts'
    icon = 'fa fa-at'
    model = SocialPost
    filters = [
        filters.Datetime(name='send_date', label='Date', placeholder='Search by date')
    ]
    fields = [
        Field(
            name='account',
            label='Account',
            display=displays.Display(),
            input_=inputs.ForeignKey(Account),
        )
    ]
