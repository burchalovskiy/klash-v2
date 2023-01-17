from contextlib import contextmanager
from unittest.mock import patch


@contextmanager
def mock_request(**kwargs):
    with patch('app.services.BAD.base.BaseBADService._request', **kwargs) as m:
        yield m


@contextmanager
def mock_db(atr, **kwargs):
    with patch('app.services.BAD.classes.{}'.format(atr), **kwargs) as m:
        yield m


@contextmanager
def mock_influx(**kwargs):
    with patch('app.services.analytics.influxdb_client.InfluxClient._emit_event', **kwargs) as m:
        yield m
