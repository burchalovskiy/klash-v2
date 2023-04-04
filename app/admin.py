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
from fastapi_admin.resources import Dropdown, Field, Model
from fastapi_admin.widgets import displays, filters, inputs
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.database.models import (
    Account,
    Admin,
    CrossPost,
    SocialAction,
    SocialActionLog,
    SocialPost,
    SocialPostURL,
    SocialUser,
)

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
            display=displays.Display(),
            input_=inputs.Password(),
        ),
        'token',
        Field(
            name='user',
            label='User',
            display=displays.Display(),
            input_=inputs.ForeignKey(Admin),
        ),
    ]


@admin_app.register
class Social(Dropdown):
    class CrossPostResource(Model):
        label = 'Cross posts'
        icon = 'fa fa-at'
        model = CrossPost
        filters = [filters.Datetime(name='send_date', label='Date', placeholder='Search by date')]
        fields = [
            'id',
            Field(
                name='post',
                label='Post to',
                display=displays.Display(),
                input_=inputs.ForeignKey(SocialPost),
            ),
            Field(name='is_send', label='Is sent?', display=displays.Boolean(), input_=inputs.Switch()),
            Field(name='send_date', label='Time', display=displays.DatetimeDisplay(), input_=inputs.DateTime()),
        ]

    class SocialPostResource(Model):
        label = 'Scrab posts'
        icon = 'fa fa-at'
        model = SocialPost
        filters = [filters.Datetime(name='send_date', label='Date', placeholder='Search by date')]
        fields = [
            'id',
            Field(
                name='account',
                label='Account',
                display=displays.Display(),
                input_=inputs.ForeignKey(Account),
            ),
            'post_id',
            'caption',
            'post_url',
            Field(
                name='created_at',
                label='created_at',
                display=displays.DateDisplay(),
                input_=inputs.DateTime(),
            ),
        ]

    class SocialUserResource(Model):
        label = 'Users'
        icon = 'fa fa-at'
        model = SocialUser
        filters = [
            filters.Search(
                name='username', label='Username', search_mode='contains', placeholder='Search for username'
            ),
        ]
        fields = [
            'id',
            Field(
                name='account',
                label='By account',
                display=displays.Display(),
                input_=inputs.ForeignKey(Account),
            ),
            'username',
            Field(
                name='actions',
                label='Actions',
                display=displays.Display(),
                input_=inputs.ManyToMany(SocialAction),
            ),
        ]

    class SocialPostURLResource(Model):
        label = 'URLs'
        icon = 'fa fa-at'
        model = SocialPostURL
        fields = [
            'id',
            'content_type',
            'url',
            Field(
                name='post',
                label='Post',
                display=displays.Display(),
                input_=inputs.ForeignKey(SocialPost),
            ),
        ]

    label = "Socials"
    icon = "fas fa-bars"
    resources = [
        CrossPostResource,
        SocialPostResource,
        SocialUserResource,
        SocialPostURLResource,
    ]


@admin_app.register
class SocialAction(Dropdown):
    class SocialActionResource(Model):
        label = 'Actions'
        icon = 'fa fa-at'
        model = SocialAction
        fields = [
            'id',
            'title',
            Field(
                name='is_active',
                label='Enabled',
                display=displays.Boolean(),
                input_=inputs.Switch(),
            ),
            'type',
            'values',
        ]

    class SocialActionLogResource(Model):
        label = 'Logs'
        icon = 'fa fa-at'
        model = SocialActionLog

    label = "Actions"
    icon = "fas fa-bars"
    resources = [
        SocialActionResource,
        SocialActionLogResource,
    ]
