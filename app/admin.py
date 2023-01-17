from fastapi_admin.app import app as admin_app
from fastapi_admin.exceptions import (
    forbidden_error_exception,
    not_found_error_exception,
    server_error_exception,
    unauthorized_error_exception,
)
from fastapi_admin.resources import Field, Link, Model
from fastapi_admin.widgets import displays, filters, inputs
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.constants import GRAFANA_URL
from app.database.models import Admin, FreeReport, Offer, PaidReport, Payment, User

admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)


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


@admin_app.register
class UserResource(Model):
    label = 'Customers'
    model = User


@admin_app.register
class FreeReportResource(Model):
    label = 'Free Reports'
    model = FreeReport
    filters = [
        filters.Search(name='id', label='Id', search_mode='contains'),
        filters.Enum(
            enum=FreeReport.RequestTypes,
            name='request_type',
            label='Request Type',
            enum_type=str,
            null=True,
        ),
        filters.Search(name='request_info', label='Request Info', search_mode='contains'),
        filters.Datetime(name='created_at', label='CreatedAt'),
    ]
    fields = [
        'id',
        'is_completed',
        'request_type',
        'request_info',
        'created_at',
        # 'json_result',
    ]


@admin_app.register
class PaidReportResource(Model):
    label = 'Paid Reports'
    model = PaidReport
    filters = [
        filters.Search(name='id', label='Id', search_mode='contains'),
        filters.Search(name='user_id', label='Customer Id', search_mode='contains'),
        filters.Search(name='free_report_id', label='Basic Report Id', search_mode='contains'),
        filters.Datetime(name='created_at', label='CreatedAt'),
    ]
    fields = [
        'id',
        'is_completed',
        'user_id',
        'free_report_id',
        'created_at',
        # 'json_result',
    ]


@admin_app.register
class OfferResource(Model):
    label = 'Offers'
    model = Offer


@admin_app.register
class PaymentResource(Model):
    label = 'Payments'
    model = Payment


@admin_app.register
class GrafanaLink(Link):
    label = 'Grafana'
    url = GRAFANA_URL
    icon = 'fas fa-bars'
